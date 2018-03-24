from collections import defaultdict
"""
- set X Y sets register X to the value of Y.
- sub X Y decreases register X by the value of Y.
- mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
- jnz X Y jumps with an offset of the value of Y, but only if the value of X is not zero.

part 1:
how many times is the mul instruction invoked?
"""
registers = defaultdict(int)

"""
- register starts at 1
"""
registers['a'] = 1

def __get__(value):
  try:
    return int(value)
  except ValueError:
    return registers[value]

def __get_instructions__():
  with open('input/coprocessor.txt') as f:
    instructions = [instr.strip().split(' ') for instr in f.readlines()]
  return instructions

def coprocessor():
  instructions = __get_instructions__()
  mcount = 0
  index = 0
  while index < len(instructions):
    (a, x, y) = instructions[index]
    if a == 'set':
      registers[x] = __get__(y)
    elif a == 'sub':
      registers[x] -= __get__(y)
    elif a == 'mul':
      registers[x] *= __get__(y)
      mcount += 1
    elif a == 'jnz':
      if __get__(x) != 0:
        index += __get__(y)
        continue
    index += 1
  return mcount

def debug_h():
  h = 0
  for i in xrange(107900, 124900 + 1, 17):
    for j in xrange(2, i):
        if i % j == 0:
            h += 1
            break
  return h

# print(coprocessor())
print(debug_h())


