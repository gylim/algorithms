from random import random

def knuth(vect):
    denom = 0
    champion = ""
    for word in vect:
        denom += 1
        if 1/denom > random():
            champion = word
    return print(champion)

def RandomWord(words):
    if ".txt" in words:
        with open(words, "r") as myfile:
            vect = myfile.read().split()
            return knuth(vect)
    else:
        vect = words.split()
        return knuth(vect)

RandomWord("words.txt")