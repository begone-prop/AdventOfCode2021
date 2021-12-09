#!/usr/bin/env python3

with open('input', 'r') as inp:
    data = [i.strip('\n') for i in inp.readlines()]

numbers = [int(x) for x in data[0].split(',')]

def getBoards(inp):
    result = []
    inpBoards = inp[1:]
    dataLen = len(inpBoards)
    tempBoard = []

    for idx, line in enumerate(inpBoards):
        inBoard = False if not len(line) else True

        if inBoard:
            tempBoard.append([int(x) for x in line.split()])

        if not inBoard or idx + 1 == dataLen:
            if len(tempBoard):
                result.append(tempBoard)
            tempBoard = []

    return result


def play(bingoBoards, draws):
    for number in draws:
        for idx, board in enumerate(bingoBoards):
            for jdx, row in enumerate(board):
                for zdx, element in enumerate(row):
                    if element == number:
                        bingoBoards[idx][jdx][zdx] = -1
                        if sum(row) == -fieldLen or sum([rw[jdx] for rw in board]) == -fieldLen:
                            return number, idx
    return -1, -1

boards = getBoards(data)
lookup = getBoards(data)

fieldLen = len(boards[0][0])
num, index = play(boards, numbers)

s = 0

for a, b in zip(boards[index], lookup[index]):
    for x, y in zip(a, b):
        if x != -1: s += y

print(s, num, s * num)
