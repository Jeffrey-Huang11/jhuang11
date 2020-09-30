# Write a program that will print the name of a randomly-selected student from team (orpheus, rex, or endymion)
# Made by Jeffrey Huang, Dragos Lup, Ryan Ma
# Import random to use 'random.choice' function, which goes through a list and randomly selects an element
import random

KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDY', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}

print(random.choice(random.choice(list(KREWES.values()))))
# Gets the values (groups) from KREWES, declares them as lists, randomly chooses a list, then randomly chooses a name, prints