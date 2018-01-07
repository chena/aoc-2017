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

# print(hex_ed(['se', 'sw', 'se', 'sw', 'sw']))
# print(hex_ed())

def __check_connections__(program_id, links, group):
  for c in links[program_id]:
    if c in group:
      continue
    group.add(c)
    __check_connections__(c, links, group)

def digital_plumber():
  with open('input/programs.txt') as f:
    content = f.readlines()
  links = {}
  programs = [p.strip() for p in content]
  arrow = '<->'
  for p in programs:
    parts = p.split(arrow)
    program = int(parts[0].strip())
    links[program] = [int(l) for l in parts[1].strip().split(', ')]
  # traverse through each program and check its connections
  # keep track of the programs with a set
  zero_group = {0}
  __check_connections__(0, links, zero_group)
  return len(zero_group)
print(digital_plumber())
