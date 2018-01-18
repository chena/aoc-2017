"""
part 1:
The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to 
the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
You have the path the child process took. 
Starting where he started, you need to determine the fewest number of steps required to reach him. 
(A "step" means to move from the hex you are in to any adjacent hex.)

For example:

ne,ne,ne is 3 steps away.
ne,ne,sw,sw is 0 steps away (back where you started).
ne,ne,s,s is 2 steps away (se,se).
se,sw,se,sw,sw is 3 steps away (s,s,sw).

part 2:
How many steps away is the furthest he ever got from his starting position?
"""
class Coordinate:
  movements = {
    'nw': (-1, 1),
    'n': (0, 2),
    'ne': (1, 1),
    'se': (1, -1),
    's': (0, -2),
    'sw': (-1, -1)
  }
  
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def move(self, direction):
    movement = self.movements[direction]
    self.x += movement[0]
    self.y += movement[1]

  def __str__(self):
    return '({}, {})'.format(self.x, self.y)

def __distance__(location):
  x_distance = abs(location.x)
  y_distance = abs(location.y)
  return x_distance if x_distance > y_distance else (x_distance + y_distance) / 2

def hex_ed(paths=[]):
  if not paths:
    with open('input/hex_ed.txt') as f:
      content = f.readline().strip()
    paths = content.split(',')
  # start moving
  location = Coordinate(0, 0)
  steps = []
  for direction in paths:
    location.move(direction)
    steps.append(__distance__(location))
  print('final location is: {}'.format(location))
  return max(steps)

print(hex_ed(['se', 'sw', 'se', 'sw', 'sw']))
# print(hex_ed())