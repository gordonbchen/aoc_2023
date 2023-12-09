import numpy as np


with open("data.txt") as f:
    data = [
        np.array([int(i) for i in line.split()])
        for line in f.read().split("\n")
    ]


s = 0
for hist in data:
    nums = [hist]
    while (nums[-1] != 0).any():
        nums.append(np.diff(nums[-1]))
    
    next_val = sum(level[-1] for level in nums)
    s += next_val

print(s)
