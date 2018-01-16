"""
http://adventofcode.com/2017/day/10
"""
def __reverse__(lst, start_index, end_index):
  size = len(lst)
  if (start_index == end_index):
    return lst
  if (start_index < end_index):
    swap_count = (end_index - start_index + 1) / 2
  else:
    swap_count = (size - start_index + end_index + 1) / 2
  for n in range(swap_count):
    temp = lst[start_index]
    lst[start_index] = lst[end_index]
    lst[end_index] = temp
    start_index = (start_index + 1) % size
    end_index = (end_index - 1) % size

# lst = [0, 1, 2, 3, 4, 5]
# __reverse__(lst, 4, 1)
# print(lst)

# input 76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229
def knot_hash(lengths=[3, 4, 1, 5], size=5, rounds=1):
  numbers = range(size)
  index = 0
  skip_size = 0
  for r in range(rounds):
    for n in lengths:
      end_index = (index + n) % size
      if n > 0:
        end_index -= 1
        __reverse__(numbers, index, end_index)
      index = (end_index + (0 if n < 1 else 1) + skip_size) % size
      skip_size += 1
  return numbers
# print(knot_hash())
# print(knot_hash([76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229], 256))

def kont_hash_ascii(lengths='3,4,1,5', size=5):
  lengths = [ord(c) for c in lengths]
  lengths.extend([17, 31, 73, 47, 23])
  numbers = knot_hash(lengths, size, 64)
  result = []
  for n in range(16):
    start = n * 16
    end = start + 16 
    r = reduce(lambda x, y: x ^ y, numbers[start:end])
    h = hex(r)[2:]
    result.append(('0' if len(h) < 2 else '') + h)
  return ''.join(result)
print(kont_hash_ascii('76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229', 256))