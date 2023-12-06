def get_data(test: bool = False) -> list[str]:
  """Read data lines."""
  file_name = "test.txt" if test else "data.txt"
  with open(f"day_4/{file_name}") as f:
    lines = f.read().split("\n")
  return lines


def get_colon_pipe_inds(split_line: list[str]) -> tuple[int, int]:
  """Get colon and pipe inds."""
  for (i, num) in enumerate(split_line):
    if ":" in num:
      colon_ind = i
    elif num == "|":
      pipe_ind = i

  return (colon_ind, pipe_ind)


def count_wins(line: str) -> int:
  """Count numbe of wins in line."""
  split_line = line.split()
  colon_ind, pipe_ind = get_colon_pipe_inds(split_line)
  win_nums = split_line[colon_ind + 1:pipe_ind]
  curr_nums = split_line[pipe_ind + 1:]

  both_nums = [int(i) for i in win_nums if i in curr_nums]
  return len(both_nums)


if __name__ == "__main__":
  lines = get_data(test=False)

  cards = [1 for i in range(len(lines))]
  for (i, line) in enumerate(lines):
    wins = count_wins(line)
    for j in range(wins):
      cards[i + 1 + j] += cards[i]

  print(sum(cards))
