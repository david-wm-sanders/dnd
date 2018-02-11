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
        r = roll.pop("roll")
        population.append(roll)
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
    res = random.choices(population, weights)[0]
    if "result" in res:
        return res["result"]
    elif "result_diceroll" in res:
        x = dice.roll(res["result_diceroll"])
        return x
    elif "result_template" in res:
        pass
    else:
        raise Exception("What?! No valid result?")


def generate_origins():
    print("Origins:")
    # Roll a race
    race = roll_from_table("race")
    print(f" - You are {race}.")
    # If half-blood race, determine what each of the parents were
    if race in ["a half-elf", "a half-orc", "a tiefling"]:
        if race == "a half-elf":
            parent_races = roll_from_table("halfelfparents")
        elif race == "a half-orc":
            parent_races = roll_from_table("halforcparents")
        elif race == "a tiefling":
            parent_races = roll_from_table("tieflingparents")
        print(f"  - Your parents were {parent_races}.")
    # Roll to discover if parents were known or not
    parents_known = roll_from_table("parents")
    print(f" - You {parents_known} who your parents are or were.")
    # Roll up a birthplace
    birthplace = roll_from_table("birthplace")
    print(f" - You were born {birthplace}.")
    # Roll the number of siblings
    sibling_number = roll_from_table("siblingnumber")
    print(f" - You have {sibling_number} sibling(s).")
    # TODO: Roll sibling gender, age?, occupation, alignment, status,
    #       relationship, et cetera
    family = roll_from_table("family")
    print(f" - You were raised {family}.")


if __name__ == '__main__':
    # restest = []
    # for _ in range(10000):
    #     restest.append(roll_parents())
    # counter = collections.Counter(restest)
    # print(counter.most_common())
    generate_origins()
