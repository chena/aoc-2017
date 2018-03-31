from collections import defaultdict
"""
http://adventofcode.com/2017/day/24

- make a bridge by connecting components via ther ports.
- the first port you use must be of type 0. 
- order of the ports does not matter.
- stength of a bridge is the sum of the port types in each component. 

part 1:
What is the strength of the strongest bridge 
you can make with the components you have available?
"""
mapping = defaultdict(list)
sums = []

class Node:
  def __init__(self, value):
    self.value = value
    self.children = []
    self.used = False

  def add_child(self, child):
    self.children.append(child)

  def mark_used(self):
    self.used = True

  def __str__(self):
    return '({}, {})'.format(self.value[0], self.value[1])

def __all_used__(key):
  for c in mapping[key]:
    if not c.used:
      return False
  return True

def __traverse__(node, addup):
  node.mark_used()
  key = node.value[1]
  addup += key + node.value[0]
  if __all_used__(key):
    sums.append(addup)
    return node
  for c in mapping[key]:
    if not c.used:
      node.add_child(__traverse__(c, addup))
  return node
  
def bridges():
  with open('input/bridges.txt') as f:
    components = [sorted([int(p) for p in comp.split('/')]) for comp in f.readlines()]
  for pair in components:
    left, right = pair
    node = Node(pair)
    mapping[left].append(node)
    mapping[right].append(node)
  # starts at 0
  tree = __traverse__(mapping[0][0], 0)
  # tree2 = __traverse__(mapping[0][1], 0)
  return max(sums)

print(bridges())