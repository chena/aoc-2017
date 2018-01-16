from collections import defaultdict

"""
part 1:
Each instruction consists of several parts: 
the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. 
If the condition fails, skip the instruction without modifying the register. 
The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
c is increased by -20 (to -10) because c is equal to 10.
After this process, the largest value in any register is 1.

What is the largest value in any register after completing the instructions in your puzzle input?

part 2:
What is the highest value held in any register during this process
"""
def register():
  with open('input/register.txt') as f:
    instructions = f.readlines()
  registers = defaultdict(int)
  # all registers start out zero
  highest = 0
  for line in instructions:
    parts = line.split('if')
    # parse condition
    cond_inst = parts[1].strip()
    cond_parts = cond_inst.split(' ')
    cond_r = cond_parts[0]
    condition = ' '.join(cond_parts[1:]).strip()
    check = eval('{} {}'.format(registers[cond_r], condition))
    # parse instruction if condition is true
    if check:
      inst = parts[0].strip()
      dec = inst.split('dec')
      if (len(dec) > 1):
        reg = dec[0].strip()
        result = registers[reg] - int(dec[1])
      else:
        inc = inst.split('inc')
        reg = inc[0].strip()
        result = registers[reg] + int(inc[1])
      registers[reg] = result
      if (result > highest):
        highest = result
  # part 1
  # return max(registers.values())
  # part 2
  return highest
print(register())




