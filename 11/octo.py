#!/usr/bin/env python3

def readInput(fileName: str) -> list[list[int]]:
    result = []
    with open(fileName, 'r') as inp:
        data = [i.strip('\n') for i in inp.readlines()]

    rowLength = len(data[0])
    for row in data:
        result.append([int(row[i]) for i in range(rowLength)])

    return result

def printOctos(octos) -> None:
    for row in octos:
        print(row)

octopi = readInput('input')
neigh = range(-1, 2)
simulate = True
flashed = False
flashes = 0
firstSync = -1

step = 0
maxStep = 20000

def isNeighbour(i, j, a, b, maxIdx):
    if i + a > maxIdx - 1 or j + b > maxIdx - 1:
        return False

    if i + a < 0 or j + b < 0:
        return False

    if a == 0 and b == 0:
        return False

    return True

while simulate:
    for idx, row in enumerate(octopi):
        for jdx, number in enumerate(row):
            octopi[idx][jdx] += 1
            if number == 9:
                flashed = True

    while flashed:
        flashed = False
        for idx, row in enumerate(octopi):
            for jdx, number in enumerate(row):
                if number > 9:
                    octopi[idx][jdx] = -1
                    flashed = True
                    flashes += 1
                    for x in neigh:
                        for y in neigh:
                            if isNeighbour(idx, jdx, x, y, len(octopi[0])):
                                if octopi[idx + x][jdx + y] != -1:
                                    octopi[idx + x][jdx + y] += 1

    for idx, row in enumerate(octopi):
        for jdx, number in enumerate(row):
            if octopi[idx][jdx] == -1:
                octopi[idx][jdx] = 0

    step += 1

    if sum([sum(row) for row in octopi]) == 0:
        firstSync = step
        break

    if step >= maxStep:
        simulate = False

printOctos(octopi)
print(flashes)
print(firstSync)
