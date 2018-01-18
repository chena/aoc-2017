"""
part 1:
For each row, determine the difference between the largest value and the smallest value; 
the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8
The first row's largest and smallest values are 9 and 1, and their difference is 8.
The second row's largest and smallest values are 7 and 3, and their difference is 4.
The third row's difference is 6.
In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.
"""
def __parse_checksum_input__(filename):
  with open(filename) as f:
    content = f.readlines()
  rows = []
  for line in content:
    rows.append([int(n) for n in line.strip().split()])
  return rows

def corruption_checksum(rows):
  diffs = []
  for r in rows:
    min_val = r[0]
    max_val = r[0]
    for n in range(1, len(r)):
      if (r[n] < min_val):
        min_val = r[n]
      elif (r[n] > max_val):
        max_val = r[n]
    diffs.append(max_val - min_val)
  return sum(diffs)
# print(corruption_checksum([[5, 1, 9, 5],[7, 5, 3],[2, 4, 6, 8]]))
# print(corruption_checksum(__parse_checksum_input__('input/checksum_input.txt')))

"""
part 2:
find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5
In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
In the second row, the two numbers are 9 and 3; the result is 3.
In the third row, the result is 2.
In this example, the sum of the results would be 4 + 3 + 2 = 9.
"""
def corruption_checksum_divisible(rows):
  divs = []
  for r in rows:
    s = sorted(r, reverse=True)
    end = len(s) - 1
    for n in range(end):
      index = end
      while n < index and s[n] % s[index] != 0:
        index -= 1
      if (n < index):
        divs.append(s[n] / s[index])
        break;
  return sum(divs);
print(corruption_checksum_divisible([[5, 9, 2, 8],[9, 4, 7, 3],[3, 8, 6, 5]]))
# print(corruption_checksum_divisible(__parse_checksum_input__('input/checksum_input.txt')))