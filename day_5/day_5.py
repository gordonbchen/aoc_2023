import re


# Types.
range_t = tuple[int, int]
map_t = list[int]
level_maps_t = list[map_t]


def get_ranges_maps(test: bool = False) -> tuple[list[range_t], list[level_maps_t]]:
  """Read seed ranges and maps."""
  file_name = "test.txt" if test else "data.txt"
  with open(file_name) as f:
    data = f.read().split("\n\n")

  num_re = re.compile(r"\d+")
  get_nums = lambda line: [int(i) for i in num_re.findall(line)]

  seed_nums = get_nums(data[0])
  ranges = [(s, s + l) for (s, l) in zip(seed_nums[::2], seed_nums[1::2])]

  maps = [
    [get_nums(line) for line in lines.split("\n")[1:]]
    for lines in data[1:]
  ]

  print(ranges)
  print(maps)

  return ranges, maps


def apply_map(r: range_t, m: map_t) -> list[range_t]:
  """Apply a map to a range."""
  # Unpack values.
  r_s, r_e = r

  dest_s, src_s, l = m
  dest_e, src_e = dest_s + l, src_s + l

  if (r_s <= src_s) and (r_e >= src_e):
    # src in range.
    rs = [(r_s, src_s), (dest_s, dest_e), (src_e, r_e)]

  elif (src_s <= r_s) and (src_e >= r_e):
    # range in src.
    rs = [(dest_s + (r_s - src_s), dest_e - (src_e - r_e))]

  elif (src_s <= r_s) and (src_e >= r_s):
    # src on left.
    rs = [(dest_s + (r_s - src_s), dest_e), (src_e, r_e)]

  elif (src_s <= r_e) and (src_e >= r_e):
    # src on right. 
    rs = [(r_s, src_s), (dest_s, dest_e - (src_e - r_e))]

  else:
    return [r]
  
  return [i for i in rs if i[0] != i[1]]  # remove empty ranges.
  

def apply_level_maps(ranges: list[range_t], level_maps: level_maps_t) -> list[range_t]:
  """Apply level maps to ranges."""
  new_ranges = ranges.copy()

  for m in level_maps:
    for r in ranges:
      new_rs = apply_map(r, m)
      new_ranges += new_rs

      if r in new_ranges:
        new_ranges.remove(r)

  return new_ranges


if __name__ == "__main__":
  ranges, maps = get_ranges_maps(test=False)

  for level_maps in maps:
    ranges = apply_level_maps(ranges, level_maps)

  print(ranges)

  min_loc = ranges[0][0]
  for i in ranges[1:]:
    min_loc = min(min_loc, i[0])
  print(min_loc)
