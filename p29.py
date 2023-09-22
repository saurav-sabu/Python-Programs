# Python Program to shuffle deck of cards

import random

deck = [(x,y) for x in range(1,14) for y in ["Spade","Club","Hearts","Diamond"]]

random.shuffle(deck)
print(deck)

for i in deck:
    print(f"{i[0]} of {i[1]}")