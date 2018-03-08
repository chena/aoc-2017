"""
http://adventofcode.com/2017/day/22

Nodes are either clean (.) or infected (#)
- If the current node is infected, it turns to its right. Otherwise, it turns to its left.
- If the current node is clean, it becomes infected. Otherwise, it becomes cleaned.
- The virus carrier moves forward one node in the direction it is facing.

part 1:
After 10000 bursts of activity, how many bursts cause a node to become infected?
"""
DIRECTIONS = ['up', 'right', 'down', 'left']

def __extend_grid__(grid):
  new_grid = []
  extended = ['.'] * 10
  extended.extend(['.'] * len(grid))
  extended.extend(['.'] * 10)
  for n in xrange(10):
    new_grid.append(list(extended))
  for r in grid:
    new_row = ['.'] * 10
    new_row.extend(r)
    new_row.extend(['.'] * 10)
    new_grid.append(new_row)
  for n in xrange(10):
    new_grid.append(list(extended))
  return new_grid

def __turn__(current_dir, to_turn):
  if to_turn == '-':
    return current_dir
  if to_turn == 'reverse':
    return DIRECTIONS[(DIRECTIONS.index(current_dir) + 2) % len(DIRECTIONS)]
  d = 1 if to_turn == 'right' else -1
  return DIRECTIONS[(DIRECTIONS.index(current_dir) + d) % len(DIRECTIONS)]

def __get_grid__():
  with open('input/virus.txt') as f:
    grid = [list(l.strip()) for l in f.readlines()]
  return grid

def virus():
  grid = __get_grid__()
  x = len(grid[0]) / 2
  y = len(grid) / 2
  current = grid[x][y]
  direction = 'up'
  infected_count = 0
  for n in xrange(10000):
    infected = current == '#'
    to_turn = 'right' if infected else 'left'
    direction = __turn__(direction, to_turn)
    if current == '.':
      infected_count += 1
    grid[x][y] = '.' if infected else '#'
    if direction == 'up':
      x -= 1
    elif direction == 'right':
      y += 1
    elif direction == 'down':
      x += 1
    else: # left
      y -= 1
    if x < 0 or x >= (len(grid[0]) - 1) or y < 0 or y >= (len(grid) - 1):
      grid = __extend_grid__(grid)
      x += 10
      y += 10
    current = grid[x][y]
  return infected_count

"""
part 2:
- Clean nodes become weakened.
- Weakened nodes become infected.
- Infected nodes become flagged.
- Flagged nodes become clean.

1. decide direction
- clean, it turns left.
- weakened, it does not turn, and will continue moving in the same direction.
- infected, it turns right.
- flagged, it reverses direction, and will go back the way it came.
2. modify state
3. move forward one node 

Given your actual map, after 10000000 bursts of activity, how many bursts cause a node to become infected?
"""
def virus_evolved():
  grid = __get_grid__()
  states = ['.', 'W', '#', 'F']
  states_map = {'.': 'left', 'W': '-', '#': 'right', 'F': 'reverse'}
  x = len(grid[0]) / 2
  y = len(grid) / 2
  current = grid[x][y]
  direction = 'up'
  infected_count = 0
  for n in xrange(10000000):
    infected = current == '#'
    to_turn = states_map[current]
    direction = __turn__(direction, to_turn)
    if current == 'W':
      infected_count += 1
    grid[x][y] = states[(states.index(current) + 1) % len(states)]
    if direction == 'up':
      x -= 1
    elif direction == 'right':
      y += 1
    elif direction == 'down':
      x += 1
    else: # left
      y -= 1
    if x < 0 or x >= (len(grid[0]) - 1) or y < 0 or y >= (len(grid) - 1):
      grid = __extend_grid__(grid)
      x += 10
      y += 10
    current = grid[x][y]
  return infected_count

print(virus_evolved())
