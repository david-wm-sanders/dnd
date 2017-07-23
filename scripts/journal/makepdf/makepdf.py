import itertools
import pprint
import markdown
import weasyprint
from collections import defaultdict
from pathlib import Path
from markdown.extensions.toc import TocExtension, slugify as toc_slugify


journal_path = Path(f"../../../campaigns/prydain/pc/durg/journal/")
exclusions = ["1742"]


def get_journal_entries(journal_path, exclusions):
    md_blocks = []
    if not journal_path.exists():
        raise Exception(f"No journal found at '{journal_path}'")
    else:
        print(f"\nOpening journal at '{journal_path}'")
        year_paths = [p for p in journal_path.iterdir() if p.is_dir()]
        for year_path in year_paths:
            print(f"Processing entries for {year_path.name}...")
            month_paths = [p for p in year_path.iterdir() if p.is_dir()]
            for month_path in month_paths:
                month_name = month_path.name.split("_")[1].capitalize()
                print(f" Processing entries for {month_name}...")
                entries = month_path.glob("*.md")
                for entry in entries:
                    entry_name = "/".join(entry.parts[-3:])
                    for exclusion in exclusions:
                        if exclusion in str(entry):
                            print(f"  Entry in '{entry_name}' excluded because '{exclusion}' is in the exclusions list.")
                            md_blocks.append(f"* Excluded '{entry_name}' because '{exclusion}' is in the exclusions list.\n")
                            break
                    else:
                        with entry.open(encoding="utf-8") as f:
                            md = f.read()
                            md_blocks.append(md)
        return md_blocks

def make_toc(md_entries):
    days = list(range(1, 31))
    months = ["jan", "feb", "Trimene", "apr", "may", "jun", "jul", "aug", "sep", "Ennamene", "Dekamene", "dec"]

    print("\nCreating a table of contents...")
    tree = lambda: defaultdict(tree)
    headers = tree()
    for md_entry in md_entries:
        for line in md_entry.splitlines():
            if line.startswith("## "):
                header_id = toc_slugify(line, "-")
                parts = line.split(" ")
                day, month, year = int(parts[1][:-2]), parts[2], int(parts[3])
                headers[year][month][day] = header_id

    toc = ["## Table of Contents\n"]
    for year in headers:
        print(f" Processing {year}...")
        head_columns = "|".join(" " for x in range(1, 31))
        toc.append(f"| {year} |{head_columns}|\n")
        alignment_columns = "|".join(" :-: " for x in range(1, 31))
        toc.append(f"| :-- |{alignment_columns}|\n")
        for month in headers[year]:
            print(f"  Processing {month}...")
            columns = []
            for day in days:
                header_id = headers[year][month][day]
                if type(header_id) is str:
                    columns.append(f" [{day}](#{header_id}) ")
                else:
                    columns.append(f" {day} ")
            link_columns = "|".join(columns)
            toc.append(f"| *{month}* |{link_columns}|\n")
        toc.append("\n")

    # pprint.pprint(toc)
    return toc


title = ["# The Journal of Durg Hammerfell\n"]
md_entries = get_journal_entries(journal_path, exclusions)
toc = make_toc(md_entries)

print("\nJoining markdown chunks into markdown string...")
journal_text = "".join(itertools.chain(title, toc, md_entries))

print("Converting markdown string into HTML...")
html = markdown.markdown(journal_text, extensions=["markdown.extensions.extra", TocExtension(marker="")])
(journal_path / "journal.html").write_text(html)

print("Rendering HTML to journal.pdf...")
pdf_path = journal_path / "journal.pdf"
with pdf_path.open(mode="wb") as f:
    weasyprint.HTML(string=html).write_pdf(f, stylesheets=["journal.css"])
