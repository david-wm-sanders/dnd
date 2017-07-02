import collections
import itertools
import random
from csv import DictReader
from pathlib import Path

gems_csv= Path("./gems.csv")

Gem = collections.namedtuple("Gem", "name value")
GemCategory = collections.namedtuple("GemCategory", "weight diev dievmult avgv gems")

gem_categories = {}
with gems_csv.open() as csvf:
    reader = DictReader(csvf)
    for row in reader:
        category = int(row["category"])
        weight = int(row["weight"])
        diev = row["diev"]
        dievmult = int(row["dievmult"])
        avgv = int(row["avgv"])
        gems = row["gems"].split(", ")
        gc = GemCategory(weight, diev, dievmult, avgv, gems)
        gem_categories[category] = gc

population = list(gem_categories.keys())
cweights = list(itertools.accumulate(gem_categories[category].weight for category in population))

def check_weights():
    print("Checking weights...")
    counter = collections.Counter(random.choices(population, cum_weights=cweights, k=1000))
    print(counter.most_common())

def d(x):
    return random.randint(1, x)

def make_random_gem():
    x = random.choices(population, cum_weights=cweights)[0]
    gc = gem_categories[x]
    name = random.choice(gc.gems)
    diev = gc.diev
    y, x = diev.split("d")
    value = sum(d(int(x)) for i in range(int(y))) * gc.dievmult
    return Gem(name, value)


if __name__ == '__main__':
    check_weights()
    for i in range(5):
        gem = make_random_gem()
        print(f"{gem.name}: {gem.value}gp")
