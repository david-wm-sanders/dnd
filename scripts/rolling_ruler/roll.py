import random
import statistics
import sys

def d(x):
    return random.randint(1, x)

def droplow_4d6():
    dice = [d(6), d(6), d(6), d(6)]
    dice.sort()
    dice = dice[1::]
    return sum(dice)

def droplow_4d6_rr1():
    dice = []
    while not len(dice) == 4:
        x = d(6)
        if x != 1:
            dice.append(x)
    dice.sort()
    dice = dice[1::]
    return sum(dice)

def strict_3d6():
    return sum([d(6), d(6), d(6)])

def sixplus_2d6():
    return sum([6, d(6), d(6)])

def sixplus_droplow_3d6():
    dice = [d(6), d(6), d(6)]
    dice.sort()
    dice = dice[1::]
    return sum(dice) + 6

def droplow2_5d6():
    dice = [d(6), d(6), d(6), d(6), d(6)]
    dice.sort()
    dice = dice[2::]
    return sum(dice)

rule_map = {"droplow_4d6": droplow_4d6,
            "droplow_4d6_rr1": droplow_4d6_rr1,
            "strict_3d6": strict_3d6,
            "sixplus_2d6": sixplus_2d6,
            "sixplus_droplow_3d6": sixplus_droplow_3d6,
            "droplow2_5d6": droplow2_5d6}


def roll_stats(rolling_rule):
    return [rolling_rule() for x in range(6)]

points = {3: -5,  4: -4,   5: -3,   6: -2,
          7: -1,  8: 0,    9:1,     10: 2,
          11: 3,  12: 4,   13: 5,   14: 7,
          15: 9,  16: 11,  17: 14,  18: 17}

def calc_point_buy_eq(stats):
    return sum(points[x] for x in stats)


def main_roll_stats(rolling_rule):
    rule = rule_map.get(rolling_rule, None)
    if rule:
        stats = roll_stats(rule)
        pbe = calc_point_buy_eq(stats)
        print("Ability Scores: {0}, pbe = {1}".format(stats, pbe))
    else:
        print("Rolling rule '{0}' not found.".format(rolling_rule))

def main_calc_avg(rolling_rule):
    rule = rule_map.get(rolling_rule, None)
    if rule:
        pbes = (calc_point_buy_eq(roll_stats(rule)) for x in range(100000))
        avg = statistics.mean(pbes)
        print("Average pbe for rolling rule '{0}' is {1}".format(rolling_rule, avg))
    else:
        print("Rolling rule '{0}' not found.".format(rolling_rule))

def main_check27(rolling_rule):
    rule = rule_map.get(rolling_rule, None)
    if rule:
        xlt27, xeq27, xgt27 = 0, 0, 0
        pbes = (calc_point_buy_eq(roll_stats(rule)) for x in range(100000))
        for pbe in pbes:
            if pbe < 27:
                xlt27 += 1
            elif pbe == 27:
                xeq27 += 1
            elif pbe > 27:
                xgt27 += 1
            else:
                print("Natural 1 on Tinkering skill check!")
        print(f"pbe>27: {xgt27/1000:4.1f}%,  pbe=27: {xeq27/1000:4.1f}%,  pbe<27: {xlt27/1000:4.1f}%  for rolling rule '{rolling_rule}'")
    else:
        print("Rolling rule '{0}' not found.".format(rolling_rule))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main_roll_stats("droplow_4d6")
    elif len(sys.argv) >= 2:
        if sys.argv[1] == "roll":
            rolling_rule = sys.argv[2] if len(sys.argv) >= 3 else "droplow_4d6"
            main_roll_stats(rolling_rule)
        elif sys.argv[1] == "avg":
            rolling_rule = sys.argv[2] if len(sys.argv) >= 3 else "all"
            if rolling_rule == "all":
                for rolling_rule in list(rule_map.keys()):
                    main_calc_avg(rolling_rule)
            else:
                main_calc_avg(rolling_rule)
        elif sys.argv[1] == "check27":
            rolling_rule = sys.argv[2] if len(sys.argv) >= 3 else "all"
            if rolling_rule == "all":
                for rolling_rule in list(rule_map.keys()):
                    main_check27(rolling_rule)
            else:
                main_check27(rolling_rule)
        else:
            print("Natural 1 on Usage skill check!")
    else:
        print("Natural 1 on Usage skill check!")
