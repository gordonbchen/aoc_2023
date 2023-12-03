import re


def read_data() -> list[str]:
    """Read data"""
    with open("day_3/data/data.txt") as f:
        data = f.read().split()
    
    return data


def is_part_num(match: re.Match, n_line: int, lines: list[str]) -> bool:
    """Num is a part num if touching non-period symbol."""
    span = match.span()

    upper_line = max(n_line - 1, 0)
    lower_line = min(n_line + 1, len(lines) - 1)
    for line in lines[upper_line : lower_line + 1]:

        left_ind = max(span[0] - 1, 0)
        right_ind = min(span[1], len(line) - 1)
        for char in line[left_ind : right_ind + 1]:
            if (not char.isdigit()) and (char != "."):
                return True

    return False


if __name__ == "__main__":
    lines = read_data()

    num_regex = re.compile("\d+")

    part_sum = 0
    for (n_line, line) in enumerate(lines):
        for match in num_regex.finditer(line):
            if is_part_num(match, n_line, lines):
                part_sum += int(match.group())

    print(part_sum)
