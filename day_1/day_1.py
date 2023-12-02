with open("day_1/data/data.txt") as f:
  data = f.read().split()

nums = [str(i) for i in range(10)]
alpha_nums = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine"
]

s = 0
for line in data:
  l_ind_vals = {}
  r_inds_vals = {}

  for (i, str_num) in enumerate(nums):
    l_ind = line.find(str_num)
    r_ind = line.rfind(str_num)

    if l_ind != -1: l_ind_vals[l_ind] = i
    if r_ind != -1: r_inds_vals[r_ind] = i

  for (i, str_num) in enumerate(alpha_nums):
    l_ind = line.find(str_num)
    r_ind = line.rfind(str_num)

    if l_ind != -1: l_ind_vals[l_ind] = i
    if r_ind != -1: r_inds_vals[r_ind] = i

  l_inds_vals = sorted(l_ind_vals.items(), key=lambda x: x[0])
  r_inds_vals = sorted(r_inds_vals.items(), key=lambda x: x[0], reverse=True)

  s += l_inds_vals[0][1] * 10 + r_inds_vals[0][1]

print(s)
