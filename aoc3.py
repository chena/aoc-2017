from collections import defaultdict

def register():
  with open('register.txt') as f:
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

