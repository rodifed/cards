import numpy
import random

def dec(binary):
    color = binary[:3]
    number = binary[3:]
    cv = [4, 2, 1]
    nv = [2 ** (i) for i in range(len(number))]
    number_ = 0
    color_ = 0
    for id, c in enumerate(color):
        color_ += c * cv[id]
    for id, n in enumerate(number):
        number_ += n * nv[id]
    return color_, number_

def sort(ns):
    if len(ns) > 1:
        a = sum(ns) / len(ns)
        e = [n for n in ns if n == a]
        b = [n for n in ns if n > a]
        s = [n for n in ns if n < a]
        return sort(s) + e + sort(b)
    elif len(ns) == 1:
        return ns
    else:
        return []

def main(binary): 
    cards = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
    }
    classes = {
        0: "red",
        1: "black",
        2: "blue",
        3: "purple",
        4: "gold"
    }
    for b in binary:
        co, nu = dec(b)
        cards[co].append(nu)
    for c in [0, 1, 2, 3, 4]:
        cards[c] = sort(cards[c])
    return cards

cards_ = []
for i in range(1, 64):
    int_ = random.randint(1, 64)
    cards_.append(bin(int_)[2:].zfill(7))

cards = []

for id, card in enumerate(cards_):
    cards.append([int(i) for i in list(card)])

cards = main(cards)
for class_ in cards:
    print(class_, cards[class_])

