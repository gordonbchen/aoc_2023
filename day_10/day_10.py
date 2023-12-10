import numpy as np


# Read data.
with open("data.txt") as f:
    data = np.array([list(i) for i in f.read().split()])
print(data)

# Find start pos.
start_pos_np = np.where(data == "S")
start_pos = (start_pos_np[0][0], start_pos_np[1][0])
print(start_pos)

# Create dist array.
big_num = (2 ** 31) - 1  # sign, 32 bits.
dists = np.full_like(data, fill_value=big_num, dtype=np.int32)
dists[*start_pos] = 0
print(dists)

# Create pos diff arrays for each pipe char (start, end).
up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)

pos_diffs = {
    "S": [up, down, left, right],
    "-": [left, right],
    "|": [up, down],
    "F": [down, right],
    "7": [left, down],
    "J": [up, left],
    "L": [right, up]
}

# Iterate through pipes.
exp_heads = {start_pos}
while True:
    new_exp_heads = set()

    for head_pos in exp_heads:
        moves = pos_diffs[data[*head_pos]]
        for move in moves:
            new_pos = (head_pos[0] + move[0], head_pos[1] + move[1])

            # Check if new pos has correct pipe char.
            new_pipe = data[*new_pos]

            if new_pipe == ".":
                # Went to ground. Stop exploring.
                continue

            new_moves = pos_diffs[new_pipe]
            opp_move = (move[0] * -1, move[1] * -1)  # Reverse previous move.

            if opp_move not in new_moves:
                # Pipe was not valid. Stop exploring.
                continue

            # Check if new min dist, then add new head.
            old_dist = dists[*new_pos]
            new_dist = dists[*head_pos] + 1

            if new_dist < old_dist:
                # Update dist.
                dists[*new_pos] = new_dist

                # Add head to explore.
                new_exp_heads.add(new_pos)

    # Stop exploring old heads, explore new heads.
    exp_heads = new_exp_heads

    if len(exp_heads) == 0:
        # No more heads to explore.
        break

print(dists)

max_dist = dists[dists != big_num].max()
print(f"Max dist: {max_dist}")
