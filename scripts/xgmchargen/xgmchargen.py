import collections
import itertools
import json
import random
from pathlib import Path


data_p = Path(__file__).parent / Path("data")


def load_roll_data(table_name):
    population, weights = [], []

    table_p = data_p / f"{table_name}.json"
    with table_p.open(mode="r", encoding="utf-8") as f:
        j = json.load(f)

    dice = j["dice"]
    for roll in j["rolls"]:
        population.append(roll["result"])
        r = roll["roll"]
        if "-" in r:
            rl, ru = r.split("-")
            rl, ru = int(rl), int(ru)
            w = (ru - rl + 1) / dice
            weights.append(w)
        else:
            weights.append(1 / dice)

    # print(list(zip(population, weights)))
    # print(sum(weights))
    return population, weights


def roll_parents():
    table_name = "parents"
    population, weights = load_roll_data(table_name)
    result = random.choices(population, weights)
    print("Parents:")
    print(f" - You {result[0]} who your parents are or were.")
    return result[0]


def roll_birthplace():
    table_name = "birthplace"
    population, weights = load_roll_data(table_name)
    result = random.choices(population, weights)
    print("Birthplace:")
    print(f" - You were born {result[0]}.")
    return result[0]


if __name__ == '__main__':
    # restest = []
    # for _ in range(10000):
    #     restest.append(roll_parents())
    # counter = collections.Counter(restest)
    # print(counter.most_common())
    roll_parents()
    roll_birthplace()
