import re


def read_data(test: bool) -> list[str]:
    """Read input."""
    file_name = "test.txt" if test else "data.txt"

    with open(f"day_3/data/{file_name}") as f:
        data = f.read().split()
    
    return data


def get_upper_lower_inds(ind: int, lst: list) -> tuple[int, int]:
    """Get bounded upper and lower inds."""
    upper = max(ind - 1, 0)
    lower = min(ind + 1, len(lst) - 1)
    return (upper, lower)


def is_part_num(match: re.Match, n_line: int, lines: list[str]) -> bool:
    """Num is a part num if touching non-period symbol."""
    span = match.span()

    upper_line, lower_line = get_upper_lower_inds(n_line, lines)
    for line in lines[upper_line : lower_line + 1]:

        left_ind = max(span[0] - 1, 0)
        right_ind = min(span[1], len(line) - 1)
        for char in line[left_ind : right_ind + 1]:
            if (not char.isdigit()) and (char != "."):
                return True

    return False


def get_gear_part_nums(
    gear_match: re.Match,
    n_line: int,
    lines: list[str]
) -> list[int]:
    """Get part numbers adjacent to gear."""
    upper_line, lower_line = get_upper_lower_inds(n_line, lines)
    adj_lines = lines[upper_line : lower_line + 1]

    num_re = re.compile("\d+")

    gear_part_nums = []

    for (n_adj_line, adj_line) in enumerate(adj_lines):
        for num_match in num_re.finditer(adj_line):
            num_adj_gear = gear_match.start() in range(num_match.start() - 1, num_match.end() + 1)
            if is_part_num(num_match, n_adj_line, adj_lines) and num_adj_gear:
                gear_part_nums.append(int(num_match.group()))

    return gear_part_nums

if __name__ == "__main__":
    lines = read_data(test=False)

    gear_re = re.compile("\*")

    gear_ratio_sum = 0
    for (n_line, line) in enumerate(lines):
        for gear_match in gear_re.finditer(line):
            gear_part_nums = get_gear_part_nums(gear_match, n_line, lines)
            if len(gear_part_nums) == 2:
                gear_ratio_sum += gear_part_nums[0] * gear_part_nums[1]

    print(gear_ratio_sum)
