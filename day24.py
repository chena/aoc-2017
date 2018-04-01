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

part 2:
What is the strength of the longest bridge you can make?
"""
mapping = defaultdict(list)
sums = []
briges_strength = defaultdict(list) # mapped by length to its strength

class Node:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child):
    if not child in self.children:
      self.children.append(child)

  def __str__(self):
    return '({}, {})'.format(self.value[0], self.value[1])

def __all_used__(key, current_path):
  for c in mapping[key]:
    if not c in current_path:
      return False
  return True

def __traverse__(node, current_path, current_port):
  current_path.append(node)
  f, s = node.value
  key = f if f != current_port else s
  if __all_used__(key, current_path):
    # print 'current path: ', [n.value for n in current_path]
    s = sum([sum(n.value) for n in current_path])
    briges_strength[len(current_path)].append(s)
    return node
  for c in mapping[key]:
    if not c in current_path:
      node.add_child(__traverse__(c, current_path[:], key))
  return node

def __print_mapping__():
  for c in mapping:
    print '{}: {}'.format(c, [n.value for n in mapping[c]])

def __print_tree__(node):
  print('----------tree---------')
  queue = []
  queue.append(node)
  while len(queue) > 0:
    node = queue.pop(0)
    print(node.value, ' c count: ', len(node.children))
    for c in node.children:
      queue.append(c)

def bridges():
  with open('input/bridges.txt') as f:
    components = [map(int, comp.split('/')) for comp in f.readlines()]
  for pair in components:
    left, right = pair
    node = Node(pair)
    mapping[left].append(node)
    if (left != right):
      mapping[right].append(node)
  tree = __traverse__(mapping[0][0], [], 0)
  # return max([max(b) for b in briges_strength.values()]) # part1
  return max(briges_strength[max(briges_strength.keys())]) # part 2

print(bridges())

