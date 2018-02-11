import collections
import itertools
import json
import random
from pathlib import Path

import dice


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
    print(f">> {sum(weights)}")
    return population, weights


def roll_from_table(table_name):
    population, weights = load_roll_data(table_name)
    result = random.choices(population, weights)
    return result[0]


def generate_origins():
    race = roll_from_table("race")
    parents_known = roll_from_table("parents")
    birthplace = roll_from_table("birthplace")
    print("Origins:")
    print(f" - You are {race}.")
    if race in ["a half-elf", "a half-orc", "a tiefling"]:
        if race == "a half-elf":
            parent_races = roll_from_table("halfelfparents")
        elif race == "a half-orc":
            parent_races = roll_from_table("halforcparents")
        elif race == "a tiefling":
            parent_races = roll_from_table("tieflingparents")
        print(f"  - Your parents were {parent_races}.")
    print(f" - You {parents_known} who your parents are or were.")
    print(f" - You were born {birthplace}.")


if __name__ == '__main__':
    # restest = []
    # for _ in range(10000):
    #     restest.append(roll_parents())
    # counter = collections.Counter(restest)
    # print(counter.most_common())
    generate_origins()
