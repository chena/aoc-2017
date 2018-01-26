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

def region_coount():
  used_squares = []
  # generate matrix
  for h in knot_hashes():
    binary = [int(d) for d in bin(int(h, 16))[2:]]
    used_square = [i for i in range(len(binary)) if binary[i] > 0]
    used_squares.append(used_square)
  # for i in range()


region_coount()
#square_count()