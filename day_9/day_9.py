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
    
    next_val = (
        nums[0][0]
        - sum(level[0] for level in nums[1::2])
        + sum(level[0] for level in nums[2::2])
    )
    s += next_val

print(s)
