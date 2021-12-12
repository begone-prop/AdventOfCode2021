#!/usr/bin/env python3

import raylib

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


def isNeighbour(i, j, a, b, maxIdx):
    if i + a > maxIdx or j + b > maxIdx:
        return False

    if i + a < 0 or j + b < 0:
        return False

    if a == 0 and b == 0:
        return False

    return True

WIDTH = 1000
HEIGHT = 1000

neigh = range(-1, 2)
flashes = 0

step = 0
maxStep = 10000000000
raylib.InitWindow(WIDTH, HEIGHT, b'Dumb Octopi')

raylib.SetTargetFPS(30)
octopi = readInput('./medium')
fieldLen = len(octopi[0])
offsetX = WIDTH // fieldLen
offsetY = HEIGHT // fieldLen

while not raylib.WindowShouldClose():
    flashed = False
    raylib.BeginDrawing()

    raylib.ClearBackground(raylib.BLACK)
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
                            if isNeighbour(idx, jdx, x, y, len(octopi[0]) - 1):
                                if octopi[idx + x][jdx + y] != -1:
                                    octopi[idx + x][jdx + y] += 1

    for idx, row in enumerate(octopi):
        for jdx, number in enumerate(row):
            if octopi[idx][jdx] == -1:
                raylib.DrawRectangle(offsetX * idx, offsetY * jdx, offsetX, offsetY, raylib.RED)
                octopi[idx][jdx] = 0
            else:
                nf = raylib.ColorAlpha(raylib.RED, 1 / float(octopi[idx][jdx]))
                raylib.DrawRectangle(offsetX * idx, offsetY * jdx, offsetX, offsetY, nf)

    step += 1

    if step >= maxStep:
        break

    raylib.EndDrawing()

raylib.CloseWindow()
# printOctos(octopi)
# print(flashes)
