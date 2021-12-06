#!/usr/bin/env python3

with open('input', 'r') as inp:
    data = [i.strip('\n') for i in inp.readlines()]

numbers = [int(x) for x in data[0].split(',')]

def getBoards(inp):
    result = []
    inpBoards = data[1:]
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

def getColumn(boards, x, y):
    return [column[y] for column in boards[x]]

boards = getBoards(data)
fieldLen = len(boards[0][0])

for idx, number in enumerate(numbers):
    if idx < fieldLen: continue
    for board in boards:
        canditates = set(numbers[:idx])
        for jdx, row in enumerate(board):
            if set(row).issubset(canditates):
                print('True')
                break
