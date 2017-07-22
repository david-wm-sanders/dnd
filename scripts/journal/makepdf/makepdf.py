import markdown
import weasyprint
from pathlib import Path

# name = input("Character name: ")
# journal_path = Path(f"../../../campaigns/prydain/pc/{name}/journal/")

journal_path = Path(f"../../../campaigns/prydain/pc/durg/journal/")

# if not journal_path.exists():
#     raise Exception(f"No journal found for a character named '{name}'")

exclusions = ["1742"]
md_blocks = ["# The Journal of Durg Hammerfell\n"]

print(f"\nOpening journal at '{journal_path}'")
year_paths = [p for p in journal_path.iterdir() if p.is_dir()]
for year_path in year_paths:
    print(f"Processing entries for {year_path.name}...")
    # md_blocks.append(f"## {year_path.name}\n")
    month_paths = [p for p in year_path.iterdir() if p.is_dir()]
    for month_path in month_paths:
        month_name = month_path.name.split("_")[1].capitalize()
        print(f" Processing entries for {month_name}...")
        # md_blocks.append(f"## {month_name}\n")
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

print("\nCollating markdown blocks into journal text...")
journal_text = "".join(md_blocks)

print("Converting journal text into HTML...")
html = markdown.markdown(journal_text, extensions=['markdown.extensions.extra'])
# (journal_path / "journal.html").write_text(html)

print("Rendering HTML to journal.pdf...")
pdf_path = journal_path / "journal.pdf"
with pdf_path.open(mode="wb") as f:
    weasyprint.HTML(string=html).write_pdf(f, stylesheets=["journal.css"])
