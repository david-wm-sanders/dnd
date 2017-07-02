import functools
import random

adjectives = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Rainbow",
              "Electric", "Ochre", "Puce", "Navy", "Maroon", "Pink", "Peach",
              "Cyan", "Violet", "Brown", "Black", "Gray", "White", "Silver",
              "Gold", "Jumping", "Sleeping", "Running", "Rolling", "Laughing",
              "Singing", "Flying", "Burning", "Swimming", "Crying", "Roaring",
              "Screaming", "Silent", "Petrified", "Hiding", "Hidden", "Lost",
              "Forgotten", "Shiny", "Drowning", "Giant", "Tiny", "Fat",
              "Skinny", "Humorous", "Lonely", "Drunken", "Slimy", "Undead",
              "Dark", "Bright", "Magical", "Enchanted", "Poor", "Wealthy",
              "Lucky", "Unfortunate", "Angry", "Happy", "Sad", "Thieving",
              "Desparate", "Divine", "Arcane", "Profane", "Discrete", "Buried",
              "False", "Foolish", "Flatulent", "Hypnotic", "Haunted", "Special",
              "Fun", "Drab", "Daring", "Stubborn", "Sober", "Talking", "Naked",
              "Suffering", "Cheap", "Smelly", "Easy", "Heroic", "Hovering",
              "Married", "Pious", "Pompous", "Illegal", "Sacred", "Defiled",
              "Spoilt", "Wooden", "Bloody", "Yawning", "Sleepy", "Hungry"]

nouns = ["Dog", "Wolf", "Fox", "Pug", "Cat", "Lion", "Tiger", "Kitten", "Ox",
         "Cow", "Sow", "Bull", "Calf", "Horse", "Stallion", "Mare", "Foal",
         "Owl", "Eagle", "Falcon", "Hawk", "Raven", "Crow", "Gull", "Fish",
         "Whale", "Shark", "Octopus", "Squid", "Goat", "Sheep", "Ewe", "Fly",
         "Imp", "Dragon", "Beetle", "Ant", "Wasp", "Termite", "Wizard", "Worm",
         "Lizard", "Frog", "Toad", "Snake", "Drake", "Unicorn", "Wyvern",
         "Dodo", "Slime", "Roc", "Clam", "Oyster", "Starfish", "Slug", "Snail",
         "Mouse", "Rat", "Beaver", "Rogue", "Elf", "Otter", "Seal", "Eel",
         "Monk", "Rascal", "Gopher", "Tower", "Castle", "Dagger", "Sword",
         "Bow", "Arrow", "Hat", "Boot", "Trophy", "Goose", "Duck", "Boat",
         "Ship", "River", "Falls", "Forest", "Goblin", "Wench", "Wraith",
         "Witch", "Wench", "Lady", "Lord", "Knight", "Page", "Drunk", "Shield",
         "Wand", "Helm", "Flask", "Flagon", "Pint", "Shot"]

titles = ["Bar", "Beer Hall", "Ale House", "Pub", "Lounge", "Brewery",
          "Loft", "Club", "Inn", "Tavern", "Den", "Lodge"]

services = ["Brothel", "Theatre", "Casino", "Baths", "Healing", "Fighing Ring",
            "Drinking Contests", "Exotic Foods", "Library", "Private Booths"]

illegals = ["Gang Hangout", "Death Fights", "Drug Lounge", "Blackmarket",
            "Beast Fights", "Slave Trading", "Soul Eating", "Cannibal Food",
            "Forgery", "Body Swapping"]

uniques = ["1-Way Portal", "Undead Waiters", "No Booze", "Ghost Patrons",
           "Self Filling Mugs", "Sentient Furniture", "Pocket Dimension",
           "Self Playing Band", "Reversed Gravity", "Dungeon Entrance"]


adjective = functools.partial(random.choice, adjectives)
noun = functools.partial(random.choice, nouns)
title = functools.partial(random.choice, titles)

service = functools.partial(random.choice, services)
illegal = functools.partial(random.choice, illegals)
unique = functools.partial(random.choice, uniques)

structures = [f"The {adjective()} {noun()}",
              f"The {adjective()} {noun()} {title()}",
              f"The {noun()} and {noun()}",
              f"The {noun()} and {noun()} {title()}",
              f"The {adjective()} {title()}"]


print(f"{random.choice(structures)}")
print(f"{service()}, {illegal()}, {unique()}")
