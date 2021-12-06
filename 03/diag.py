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

print(f'Part 1: {int(gamma, 2) * int(epsilon, 2)}')

# Part Two
def filterBits(data, fieldLen, bit):
    candidates = data
    result = []

    filt = bit
    nofilt = '0' if bit == '1' else '1'
    for idx in range(fieldLen):
        count = len(candidates)
        threshold = count // 2
        freq = sum([int(line[idx]) for line in candidates])
        common = filt if freq > threshold else nofilt
        if freq * 2 == count: common = filt

        result = [bit for bit in candidates if bit[idx] == common]

        if len(result) == 1: break
        candidates = result
        result = []

    return int("".join(result), 2)

oxygen = filterBits(data, bitLen, '1')
co2 = filterBits(data, bitLen, '0')
print(f'Part 2: {oxygen * co2}')
