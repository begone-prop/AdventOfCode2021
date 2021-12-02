#!/usr/bin/env python3

if __name__ == '__main__':
    with open('input', 'r') as i:
        inp = i.readlines()

    nums = [int(i) for i in inp]

    counter = 0
    for idx in range(len(nums)):
        if idx == 0: continue
        if(nums[idx] > nums[idx - 1]):
            counter += 1

    # newCounter = 0
    # for idx in range(len(nums)):
        # if idx == 0: continue
        # try: nn = nums[idx + 2]
        # except IndexError: nn = 0
        # if(nums[idx - 1] < nn):
            # newCounter += 1

    print(counter)
    #print(newCounter)
