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


