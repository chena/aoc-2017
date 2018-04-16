"""
http://adventofcode.com/2017/day/25

- A tape which contains 0 repeated infinitely to the left and right.
- A cursor, which can move left or right along the tape and read or write values at its current position.
- A set of states, each containing rules about what to do based on the current value under the cursor.

part 1:
What is the diagnostic checksum after the required number of steps?
"""
def turing_machine():
  with open('input/turing_small.txt') as f:
    instructions = f.read().split('\n\n')
  first = instructions[0]
  steps = int(first[(first.index('after ') + 6):first.index(' steps.')])
  rules = [map(str.strip, i.split('\n')) for i in instructions[1:]]
  rule_mapping = {}
  for rule in rules:
    rule_mapping[rule[0].split(' ')[-1][:-1]] = [
      (int(rule[2].split(' ')[-1][:-1]), rule[3].split(' ')[-1][:-1], rule[4].split(' ')[-1][:-1]),
      (int(rule[6].split(' ')[-1][:-1]), rule[7].split(' ')[-1][:-1], rule[8].split(' ')[-1][:-1])
    ]
  tape = [0]
  cursor = 0
  state = 'A'
  move = {'right': 1, 'left': -1}
  for step in xrange(0, steps):
    rule  = rule_mapping[state]
    current_value = tape[cursor] 
    new_value, next_move, next_state = rule[current_value]
    tape[cursor] = new_value
    cursor = cursor + move[next_move]
    if cursor < 0:
      tape.insert(0, 0)
      cursor = 0
    elif cursor >= len(tape):
      tape.append(0)
      cursor = len(tape) - 1
    state = next_state
    # print tape
  return sum(tape)

print(turing_machine())