import re

from dataclasses import dataclass
from math import lcm


with open("data.txt") as f:
  data = f.read().split("\n")

path = list(data[0])


def get_nodes(names, all_nodes):
  nodes = {}
  for n in all_nodes:
    if n.name in names:
      nodes[n.name] = n
  return nodes


@dataclass
class Node:
  name: str
  left: str
  right: str

  def populate(self, all_nodes):
    nodes = get_nodes([self.left, self.right], all_nodes)
    self.left = nodes[self.left]
    self.right = nodes[self.right]


node_re = re.compile(r"\w{3}")
nodes = [Node(*node_re.findall(line)) for line in data[2:]]
for n in nodes:
  n.populate(nodes)


curr_nodes = [n for n in nodes if n.name[-1] == "A"]

# Find individual node times. Will get all zs on lcm.
node_times = []

for curr_node in curr_nodes:
    i = 0

    cont = True
    while cont:
        for direct in path:
            curr_node = curr_node.left if direct == "L" else curr_node.right

            if curr_node.name[-1] == "Z":
                node_times.append(i + 1)
                cont = False
                break

            i += 1

print(lcm(*node_times))
