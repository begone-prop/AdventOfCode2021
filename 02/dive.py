#!/usr/bin/env python3
import sys

depth = 0
horiz = 0

with open('input', 'r') as inp:
    commands = [i.strip('\n') for i in inp.readlines()]

tups = []
for com in commands:
    tup = com.split()
    tups.append((tup[0], int(tup[1])))

for direc in tups:
    if direc[0] == 'forward':
        horiz += direc[1]

    if direc[0] == 'up':
        depth -= direc[1]

    if direc[0] == 'down':
        depth += direc[1]

print(f'{depth * horiz = }')

depth2 = 0
horiz2 = 0
aim = 0

for direc in tups:
    if direc[0] == 'forward':
        horiz2 += direc[1]
        depth2 += (aim * direc[1])

    if direc[0] == 'up':
        aim -= direc[1]

    if direc[0] == 'down':
        aim += direc[1]

print(f'{horiz2 * depth2 = }')
