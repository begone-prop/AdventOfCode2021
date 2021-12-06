#!/usr/bin/env python3

with open('input', 'r') as inp:
    data = [i.strip('\n') for i in inp.readlines()]
# Part 1 trivial solution O(n*m)
dataLen = len(data)
bitLen = len(data[0])
freq = [0] * len(data[0])
tresh = dataLen // 2

for row in data:
    for idx, digit in enumerate(row):
        if  digit == '1': freq[idx] += 1

gamma = ''.join(list(map(lambda x: '1' if x > tresh else '0', freq)))
epsilon = ''.join(['0' if y == '1' else '1' for y in gamma])
##print(int(gamma, 2) * int(epsilon, 2))
#print(gamma)

# Part Two
candidates = data
oxygen = []

for idx in range(bitLen):
    cur = 0
    for number in candidates:
        if number[idx] == '1': cur += 1

    mostCommon = '1' if cur >= len(candidates) // 2 else '0'

    for number in candidates:
        if number[idx] == mostCommon:
            oxygen.append(number)

    if len(oxygen) == 1: break
    candidates = oxygen
    oxygen = []

print(oxygen)
print(int(''.join(oxygen), 2))
