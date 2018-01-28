"""
http://adventofcode.com/2017/day/15

Generator A starts with 883
Generator B starts with 879

part 1: count matches after 40000000 pairs
part 2: count matches after 5m pairs that meet each generator's criteria
"""
A_FACTOR = 16807
B_FACTOR = 48271
DIVIDER = 2147483647
ITERATIONS = 5000000
A_MULTIPLIER = 4
B_MULTIPLIER = 8

def generators_match(a=883, b=879):
  matches = 0
  for i in xrange(ITERATIONS):
    a = a * A_FACTOR % DIVIDER
    while (a % A_MULTIPLIER > 0):
      a = a * A_FACTOR % DIVIDER
    b = b * B_FACTOR % DIVIDER
    while (b % B_MULTIPLIER > 0):
      b = b * B_FACTOR % DIVIDER
    a_binary = bin(a)[2:]
    b_binary = bin(b)[2:]
    a_bits = len(a_binary)
    b_bits = len(b_binary)
    bits = max(a_bits, b_bits)
    a_binary = '0' * (bits - a_bits) + a_binary
    b_binary = '0' * (bits - b_bits) + b_binary
    if (a_binary[-16:] == b_binary[-16:]):
      matches += 1
  return matches

print(generators_match())
  