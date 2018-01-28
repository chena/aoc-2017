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

def __check_neighbors__(i, j, rows, visited):
  # return early if already visited or cell is zero
  if (i, j) in visited or not rows[i][j]:
    return
  # track visit
  visited.add((i, j))
  # recursively check all neighbors
  if i > 0:
    __check_neighbors__(i-1, j, rows, visited)
  if j > 0:
    __check_neighbors__(i, j-1, rows, visited)
  if i < 127:
    __check_neighbors__(i+1, j, rows, visited)
  if j < 127:
    __check_neighbors__(i, j+1, rows, visited)


def region_count():
  rows = []
  for h in knot_hashes():
    binary = bin(int(h, 16))[2:]
    binary = '0' * (128 - len(binary)) + binary
    r = [int(d) for d in binary]
    rows.append(r)
  count = 0
  visited = set()
  for i in xrange(128):
    for j in xrange(128):
      # skip if already visited or cell is zero
      if (i, j) in visited or not rows[i][j]:
        continue
      # increment region
      count += 1
      __check_neighbors__(i, j, rows, visited)
  return count

#square_count()
print(region_count())