import re
import math


with open("data.txt") as f:
  data = f.read().split("\n")

def get_num(line): 
  num_re = re.compile("\d+")
  num = "".join(num_re.findall(line))
  return int(num)
  
time = get_num(data[0])
dist = get_num(data[1])

print(time)
print(dist)

# 0 = speed^2 - time(speed) + dist
# speed = (time +- sqrt((time^2) - 4(dist))) / 2
min_speed = (time - math.sqrt((time**2) - (4*dist))) / 2
max_speed = (time + math.sqrt((time**2) - (4*dist))) / 2

min_speed = math.ceil(min_speed)
max_speed = math.floor(max_speed)

print(min_speed)
print(max_speed)

error_margin = max_speed - min_speed + 1
print(error_margin)
