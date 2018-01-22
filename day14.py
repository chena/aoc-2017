"""
http://adventofcode.com/2017/day/14
"""
def disk_defragmentation(key='hxtvlmkl'):
  out = open('output/disk_defrag.txt', 'w')
  for n in range(128):
    out.write('{}-{}\n'.format(key, n))

def square_count():
  with open('output/knot_hashes.txt') as f:
    hashes = f.readlines()
  total = 0
  for h in hashes:
    binary = [int(d) for d in bin(int(h, 16))[2:]]
    total += sum(binary)
  print(total)

square_count()