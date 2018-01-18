"""
part 1:
One program at the bottom supports the entire tower. 
It's holding a large disc, and on the disc are balanced several more sub-towers. 
At the bottom of these sub-towers, standing on the bottom disc, are other programs, each holding their own disc, and so on. 
At the very tops of these sub-sub-sub-...-towers, many programs stand simply keeping the disc below them balanced but with no disc of their own.

You offer to help, but first you need to understand the structure of these towers. 
You ask each program to yell out their name, their weight, and (if they're holding a disc) the names of the programs immediately above them balancing on that disc. 
You write this information down (your puzzle input). Unfortunately, in their panic, they don't do this in an orderly fashion; by the time you're done, you're not sure which program gave which information.

For example, if your list is the following:

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
...then you would be able to recreate the structure of the towers that looks like this:

                gyxo
              /     
         ugml - ebii
       /      \     
      |         jptl
      |        
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |             
      |         ktlj
       \      /     
         fwft - cntj
              \     
                xhth

What is the name of the bottom program?
"""
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


"""
part 2:
For any program holding a disc, each program standing on that disc forms a sub-tower. 
Each of those sub-towers are supposed to be the same weight, or the disc itself isn't balanced. 
The weight of a tower is the sum of the weights of the programs in that tower.

In the example above, this means that for ugml's disc to be balanced, gyxo, ebii, and jptl must all have the same weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its disc and all programs above it must each match. This means that the following sums must all be the same:

ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the other two. Even though the nodes above ugml are balanced, ugml itself is too heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the towers balanced. If this change were made, its weight would be 60.

Given that exactly one program is the wrong weight, what would its weight need to be to balance the entire tower?

"""
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
  with open('input/circus.txt') as f:
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