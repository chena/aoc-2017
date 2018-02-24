"""
http://adventofcode.com/2017/day/21
"""
START = ['.#.', '..#', '###']
RUNS = 5

def __flip__(rule):
  flips = []
  # horizontal flip
  flips.append([r[::-1] for r in list(rule)])
  # vertical flip
  vflip = list(rule)
  temp = rule[0]
  vflip[0] = vflip[len(vflip) - 1]
  vflip[len(vflip) - 1] = temp
  flips.append(vflip)
  return flips

def __rotate__(rule):
  rotates = []
  # rotate three times
  r = list(rule)
  for n in xrange(3):
    cols = [[row[x][::-1] for row in r] for x in xrange(len(r))]
    r = list([''.join(c[::-1]) for c in cols])
    rotates.append(r)
  return rotates

def fractal_art():
  with open('input/pixel.txt') as f:
    rules = [[p.split('/') for p in r.strip().split(' => ')] for r in f.readlines()]
  # for each rule, find all its transformations and extned the rules
  rule_mapping = {}
  for r in rules:
    left, right = r
    rule_mapping[tuple(left)] = right
    for r in __flip__(left):
      rule_mapping[tuple(r)] = right
    for r in __rotate__(left):
      rule_mapping[tuple(r)] = right
  # start iterations
  pattern = START
  for n in xrange(RUNS):
    length = len(pattern)
    print('length', length)
    d = 2 if (length % 2 == 0) else 3
    split_count = length / d
    print('split count', split_count)
    for n in xrange(split_count):
      if tuple(pattern) not in rule_mapping:
        combos = __rotate__(pattern)
        combos.extend(__flip__(pattern))
        for c in combos:
          if tuple(c) in rule_mapping:
            pattern = rule_mapping[tuple(c)]
            print pattern
            break

fractal_art()
# print [tuple(r) for r in __rotate__(START)]
# print [tuple(r) for r in __flip__(START)]
