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

    statement = j["statement"]
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
    # print(f">> {sum(weights)}")
    return statement, population, weights


def roll_from_table(table_name, vpre=None, vpst=None, indent=1):
    statement, population, weights = load_roll_data(table_name)
    r = random.choices(population, weights)[0]
    values = vpre if vpre else []
    if "result" in r:
        values.append(r["result"])
    elif "result_diceroll" in r:
        x = dice.roll(r["result_diceroll"])
        values.append(x)
    elif "result_template" in r:
        pass
    else:
        raise Exception("What?! No valid result?")
    if vpst:
        values.extend(vpst)
    # Print the statement
    print(f"{'':<{indent}}- {statement.format(*values)}")
    if "subrolls" in r:
        for subroll in r["subrolls"]:
            table = subroll["table"]
            values_pre, values_pst = None, None
            if "data" in subroll:
                values_pre = subroll["data"].get("pre", None)
                values_pst = subroll["data"].get("pst", None)
            z = roll_from_table(table, values_pre, values_pst, indent=indent+1)


def generate_origins():
    print("Origins:")
    roll_from_table("race")
    roll_from_table("parents")
    roll_from_table("birthplace")
    roll_from_table("siblingnumber")
    # print(f" - You have {sibling_number} sibling(s).")
    # TODO: Roll sibling gender, age?, occupation, alignment, status,
    #       relationship, et cetera
    # Roll a family
    roll_from_table("family")
    # print(f" - You were raised {family}.")


if __name__ == '__main__':
    # restest = []
    # for _ in range(10000):
    #     restest.append(roll_parents())
    # counter = collections.Counter(restest)
    # print(counter.most_common())
    generate_origins()
