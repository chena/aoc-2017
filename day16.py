import string
"""
There are sixteen programs in total, named a through p. They start by standing in a line: a stands in position 0, b stands in position 1, and so on until p, which stands in position 15.

The programs' dance consists of a sequence of dance moves:

* Spin, written sX, makes X programs move from the end to the front, but maintain their order otherwise. (For example, s3 on abcde produces cdeab).
* Exchange, written xA/B, makes the programs at positions A and B swap places.
* Partner, written pA/B, makes the programs named A and B swap places.

For example, with only five programs standing in a line (abcde), they could do the following dance:

s1, a spin of size 1: eabcd.
x3/4, swapping the last two programs: eabdc.
pe/b, swapping programs e and b: baedc.
After finishing their dance, the programs end up in order baedc.

part 1:
In what order are the programs standing after their dance?
"""
def dance(moves, programs):
  for m in moves:
    d = m[0]
    if d == 's':
      # move to front
      n = int(m[1:])
      spin = programs[-n:]
      spin.extend(programs[:len(programs)-n])
      programs = spin
    elif d == 'x':
      # swapping positions
      pos1, pos2 = [int(p) for p in m[1:].split('/')]
      temp = programs[pos1]
      programs[pos1] = programs[pos2]
      programs[pos2] = temp
    else:
      # swapping programs
      pr1, pr2 = [p for p in m[1:].split('/')]
      pos1 = programs.index(pr1)
      pos2 = programs.index(pr2)
      programs[pos1] = pr2
      programs[pos2] = pr1
  return programs

"""
part 2:
In what order are the programs standing after their billion (1000000000) dances?
"""
def dance_repeat(count=16, moves=[], repeat=1000000000):
  programs = list(string.ascii_lowercase[:count])
  if not moves:
    with open('input/dance.txt') as f:
      moves = f.readline().strip().split(',')
  seen_moves = []
  for i in xrange(repeat):
    m = ''.join(programs)
    if m in seen_moves:
      print('seen {} after {} iterations'.format(m, i))
      return ''.join(seen_moves[repeat % i])
    seen_moves.append(m)
    programs = dance(moves, programs)
  return ''.join(programs)

# print(dance_repeat(5, ['s1','x3/4','pe/b'], 1))
print(dance_repeat())
