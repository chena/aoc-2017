from collections import defaultdict
"""
- snd X plays a sound with a frequency equal to the value of X.
- set X Y sets register X to the value of Y.
- add X Y increases register X by the value of Y.
- mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
- mod X Y sets X to the result of X modulo Y).
- rcv X recovers the frequency of the last sound played, but only when the value of X is not zero.
- jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero,

What is the value of the recovered frequency (the value of the most recently played sound) 
the first time a rcv instruction is executed with a non-zero value?
"""
def __get__(value, registers):
  try:
    return int(value)
  except ValueError:
    return registers[value]

def duet():
  with open('input/duet.txt') as f:
    instructions = [instr.strip().split(' ') for instr in f.readlines()]
  sound = 0
  index = 0
  registers = defaultdict(int)
  while index < len(instructions) - 1:
    inst = instructions[index]
    i = inst[0]
    if i == 'snd':
      sound = __get__(inst[1], registers)
    elif i == 'rcv':
      if __get__(inst[1], registers) != 0:
        print registers
        return sound
    else:
      x = inst[1]
      y = __get__(inst[2], registers)
      if i == 'set':
        registers[x] = y
      elif i == 'add':
        registers[x] += y
      elif i == 'mul':
        registers[x] *= y
      elif i == 'mod':
        if y:
          registers[x] %= y
      elif i == 'jgz':
        if __get__(x, registers) > 0:
          index += y - 1
    index += 1

print(duet())


