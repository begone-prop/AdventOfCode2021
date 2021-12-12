#!/usr/bin/env python3

with open('big') as inp:
    data = sorted([int(x) for x in inp.read().strip().split(',')])

dataLen = len(data)
median = data[dataLen // 2]
mean = sum(data) // dataLen

fuel = sum(abs(number - median) for number in data)
fule2 = sum(sum(range(abs(number - mean) + 1)) for number in data)

print(fuel)
print(fule2)
