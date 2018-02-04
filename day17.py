"""
A circular buffer repeats this process of stepping forward, inserting a new value, 
and using the location of the inserted value as the new current position a total of 2017 times, 
inserting 2017 as its final operation, and ending with a total of 2018 values (including 0) in the circular buffer.

eg. step 3 times per insert, the circular buffer would begin to evolve like this 
(using parentheses to mark the current position after each iteration of the algorithm):

(0), the initial state before any insertions.
0 (1): (0, 0, 0), and then inserts the first value, 1, after it. 1 becomes the current position.
0 (2) 1: (0, 1, 0), and then inserts the second value, 2, after it. 2 becomes the current position.
0  2 (3) 1: (1, 0, 2), and then inserts the third value, 3, after it. 3 becomes the current position.
And so on:

0  2 (4) 3  1
0 (5) 2  4  3  1
0  5  2  4  3 (6) 1
0  5 (7) 2  4  3  6  1
0  5  7  2  4  3 (8) 6  1
0 (9) 5  7  2  4  3  8  6  1
Eventually, after 2017 insertions, the section of the circular buffer near the last insertion looks like this:

1512  1134  151 (2017) 638  1513  851
Perhaps, if you can identify the value that will ultimately be after the last value written (2017), 
you can short-circuit the spinlock. In this example, that would be 638.

part 1:
What is the value after 2017 in your completed circular buffer?
"""
def spinlock(steps=376, repeat=2018):
  c_buffer = [0]
  position = 0
  for n in xrange(1, repeat):
    position = (position + steps) % n + 1
    c_buffer.insert(position, n)
  return c_buffer[c_buffer.index(repeat - 1) + 1] # part1

"""
part 2:
What is the value after 0 the moment 50000000 is inserted?
"""
def spinlock_zero(steps=376, repeat=50000000):
  position = 0
  after_zero = 0
  for n in xrange(1, repeat):
    position = (position + steps) % n + 1
    if position == 1:
      after_zero = n
  return after_zero # part2

print(spinlock_zero())


