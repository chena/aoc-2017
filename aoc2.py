def __parse_blocks_input(filename):
  with open(filename) as f:
    content = f.readline()
  return [int(n) for n in content.strip().split()]

def __distribute_blocks__(blocks):
  max_blocks = max(blocks)
  index = blocks.index(max_blocks)
  blocks[index] = 0
  while (max_blocks > 0):
    index = (index + 1) % len(blocks)
    blocks[index] += 1
    max_blocks -= 1

def memory_reallocation(blocks):
  seen = []
  while (blocks not in seen):
    seen.append(blocks[:])
    __distribute_blocks__(blocks)
  return seen
# print(len(memory_reallocation([0, 2, 7, 0])))
# print(len(memory_reallocation(__parse_blocks_input('blocks.txt'))))

def memory_reallocation_again(blocks):
  seen = []
  while (blocks not in seen):
    seen.append(blocks[:])
    __distribute_blocks__(blocks)
  target = blocks[:]
  steps = 0
  while (steps < 1 or blocks != target):
    steps += 1
    __distribute_blocks__(blocks)
  return steps;
# print(memory_reallocation_again([0, 2, 7, 0]))
# print(memory_reallocation_again(__parse_blocks_input('blocks.txt')))

def recursive_circus():
  children = []
  parents = []
  with open('circus.txt') as f:
    content = f.readlines()
  for entry in content:
    parts = entry.split('->')
    if len(parts) > 1:
      children.extend([c.strip() for c  in parts[1].strip().split(',')])
    parents.append(parts[0].split('(')[0].strip())
  return (set(parents) - set(children)).pop()
# print(recursive_circus())

class Node:
  def __init__(self, name, weight=0):
    self.name = name
    self.weight = weight
    self.children = []
    self.parent = None

  def set_weight(self, weight):
    self.weight = weight

  def add_children(self, children):
    if (isinstance(children, list)):
      self.children.extend(children)
    else:
      self.children.append(children)

  def __str__(self):
    return '{} ({})'.format(self.name, self.weight)

def __get_total_weight__(node):
  if not (node.children):
    return node.weight
  return node.weight + sum([__get_total_weight__(n) for n in node.children])

def __construct_tree__(content):
  nodes = {}
  for entry in content:
    parts = entry.split('->')
    parent_parts = parts[0].split('(')
    parent_name = parent_parts[0].strip()
    parent_weight = int(parent_parts[1].strip().replace(')', ''))
    if (parent_name in nodes):
      nodes[parent_name].set_weight(parent_weight)
    else:
      nodes[parent_name] = Node(parent_name, parent_weight)
    if (len(parts) > 1):
      children = [Node(c.strip()) for c in parts[1].strip().split(',')]
      for c in children:
        if (c.name not in nodes):
          nodes[c.name] = c
        nodes[c.name].parent = nodes[parent_name]
      nodes[parent_name].add_children([nodes[c.name] for c in children])
  return nodes

def __find_root__(tree):
  for n in tree.values():
    if not n.parent:
      return n

def __wrong_subtree__(node):
  totals = {}
  for c in node.children:
    total = __get_total_weight__(c)
    if total in totals:
      totals[total].append(c)
    else:
      totals[total] = [c]
  if len(totals) == 1:
    return None
  for t in totals:
    if len(totals[t]) == 1:
      return  totals[t][0]

def recursive_circus_weight():
  with open('circus.txt') as f:
    content = f.readlines()
  tree = __construct_tree__(content)  
  # find root of the tree
  root = __find_root__(tree)
  # identity the wrong subtree
  next_wrong = __wrong_subtree__(root)
  while (next_wrong):
    wrong = next_wrong
    next_wrong = __wrong_subtree__(wrong)
  wrong_weights = __get_total_weight__(wrong)
  # calculate expected weights
  siblings = wrong.parent.children
  for s in siblings:
    if s != wrong:
      correct_weights = __get_total_weight__(s)
      break
  diff = correct_weights - wrong_weights
  return wrong.weight + diff
print(recursive_circus_weight())


