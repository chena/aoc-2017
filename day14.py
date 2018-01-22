from day10 import to_knot_hash
"""
http://adventofcode.com/2017/day/14
"""
def knot_hashes(key='hxtvlmkl'):
  return [to_knot_hash('{}-{}'.format(key, n)) for n in range(128)]

def square_count():
  total = 0
  for h in knot_hashes():
    binary = [int(d) for d in bin(int(h, 16))[2:]]
    total += sum(binary)
  print(total)

square_count()