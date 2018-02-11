from collections import defaultdict
"""
- snd X plays a sound with a frequency equal to the value of X.
- set X Y sets register X to the value of Y.
- add X Y increases register X by the value of Y.
- mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
- mod X Y sets X to the result of X modulo Y).
- rcv X recovers the frequency of the last sound played, but only when the value of X is not zero.
- jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero,

part 1:
What is the value of the recovered frequency (the value of the most recently played sound) 
the first time a rcv instruction is executed with a non-zero value?
"""
def __get__(value, registers):
  try:
    return int(value)
  except ValueError:
    return registers[value]

def __get_instructions():
  with open('input/duet.txt') as f:
    instructions = [instr.strip().split(' ') for instr in f.readlines()]
  return instructions
  
def duet():
  instructions = __get_instructions()
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

# print(duet())

"""
part 2:
- snd X sends the value of X to the other program. 
These values wait in a queue until that program is ready to receive them. 
Each program has its own message queue, so a program can never receive a message it sent.
- rcv X receives the next value and stores it in register X. 
If no values are in the queue, the program waits for a value to be sent to it. 
Programs do not continue to the next instruction until they have received a value. 
Values are received in the order they are sent.

http://adventofcode.com/2017/day/18

Once both of your programs have terminated (deadlock), how many times did program 1 send a value?
"""
def duet_programs():
  instructions = __get_instructions()
  index = [0, 0]
  registers = [defaultdict(int), defaultdict(int)]
  registers[1]['p'] = 1
  queues = [[], []]
  deadlock = [False, False]
  sent_count = 0
  while True:
    insts = [instructions[index[0]], instructions[index[1]]]
    for ind in xrange(2):
      inst = insts[ind]
      i = inst[0]
      if i == 'snd':
        queues[abs(ind - 1)].append(__get__(inst[1], registers[ind]))
        if ind == 1:
          sent_count += 1
      elif i == 'rcv':
        q = queues[ind]
        if len(q):
          registers[ind][inst[1]] = q.pop(0)
        else: # need to wait
          index[ind] -= 1
          deadlock[ind] = True
        if deadlock[0] and deadlock[1]:
          return sent_count
      else:
        x = inst[1]
        y = __get__(inst[2], registers[ind])
        if i == 'set':
          registers[ind][x] = y
        elif i == 'add':
          registers[ind][x] += y
        elif i == 'mul':
          registers[ind][x] *= y
        elif i == 'mod':
          if y:
            registers[ind][x] %= y
        elif i == 'jgz':
          if __get__(x, registers[ind]) > 0:
            index[ind] += y - 1
      index[ind] += 1

print(duet_programs())
  





