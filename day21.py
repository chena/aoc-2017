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
  for n in xrange(3):
    r = list(rule)
    cols = [[row[x][::-1] for row in r] for x in xrange(len(r))]
    r = list([''.join(c[::-1]) for c in cols])
    rotates.append(r)
  return rotates

def __extend_mapping__(pattern, rule_mapping): 
    combos = __rotate__(pattern)
    combos.extend(__flip__(pattern))
    for c in combos:
      if tuple(c) in rule_mapping:
        rule_mapping[tuple(pattern)] = rule_mapping[tuple(c)]

def __on_count__(block):
  return sum([sum([1 if c == '#' else 0 for c in r]) for r in block])

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
  # check if initial pattern is in the rule
  pattern = START
  __extend_mapping__(pattern, rule_mapping)
  # start iterations
  for n in xrange(RUNS):
    new_grid = []
    d = 2 if (len(pattern) % 2 == 0) else 3
    for y in xrange(0, len(pattern), d):
      # prepare rows to extend from transformation
      extended_rows = [[] for i in xrange(d + 1)]
      for x in xrange(0, len(pattern), d):
        subpattern = [pattern[y+r][x:x+d] for r in xrange(d)]
        if tuple(subpattern) not in rule_mapping:
          __extend_mapping__(subpattern, rule_mapping)
        mapped_pattern = rule_mapping[tuple(subpattern)]
        for i, r in enumerate(mapped_pattern):
          extended_rows[i].extend(list(r))
      new_grid.extend([''.join(r) for r in extended_rows])
    pattern = new_grid
  print __on_count__(pattern)

fractal_art()
