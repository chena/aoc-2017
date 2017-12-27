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
# print(register())

def stream_score(streams):
  scores = []
  index = 0
  groups = list(streams)
  while groups:
    if groups[index] == '{':
      scores.append(index + 1)
      index += 1
    else: # closing
      groups.pop(index)
      groups.pop(index - 1)
      index -= 1
  return sum(scores)

def stream_processing(content=None):
  if not content:
    with open('stream.txt') as f:
      content = f.readline().strip()
  ignore_next = '!'
  garbage_open = '<'
  garbage_close = '>'
  group_open = '{'
  group_close = '}'
  score = 0
  garbage_mode = False
  scores_stack = {}
  garbage_stack = {}
  skip = False
  cleaned = ''
  garbage_count = 0
  
  for c in content:
    if skip:
      skip = False
    elif c == ignore_next:
      skip = True
    elif c == garbage_close:
      garbage_mode = False
    elif garbage_mode:
      garbage_count += 1
      continue
    elif c == garbage_open:
      garbage_mode = True
    elif c in [group_open, group_close]:
      cleaned += c
  return cleaned

# streams = stream_processing('{{<!!>},{<!!>},{<!!>},{<!!>}}')
# print(streams)
# print(stream_score(stream_processing()))
print(stream_processing())
