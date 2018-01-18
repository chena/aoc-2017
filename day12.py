"""
part 1:
Each program has one or more programs with which it can communicate, and they are bidirectional; 
if 8 says it can communicate with 11, then 11 will say it can communicate with 8.

You need to figure out how many programs are in the group that contains program ID 0.

For example, suppose you go door-to-door like a travelling salesman and record the following list:

0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
In this example, the following programs are in the group that contains program ID 0:

- Program 0 by definition.
- Program 2, directly connected to program 0.
- Program 3 via program 2.
- Program 4 via program 2.
- Program 5 via programs 6, then 4, then 2.
- Program 6 via programs 4, then 2.
Therefore, a total of 6 programs are in this group; all but program 1, which has a pipe that connects it to itself.

How many programs are in the group that contains program ID 0?
"""
def __check_connections__(program_id, connections, group):
  for c in connections[program_id]:
    if c in group:
      continue
    group.add(c)
    __check_connections__(c, connections, group)

def __get_connetions__():
  with open('input/programs.txt') as f:
    content = f.readlines()
  connections = {}
  programs = [p.strip() for p in content]
  arrow = '<->'
  for p in programs:
    parts = p.split(arrow)
    program = int(parts[0].strip())
    connections[program] = [int(l) for l in parts[1].strip().split(', ')]
  return connections

def digital_plumber_zero_group():
  connections = __get_connetions__()
  # traverse through each program and check its connections
  # keep track of the programs with a set
  zero_group = {0}
  __check_connections__(0, connections, zero_group)
  return len(zero_group)
# print(digital_plumber_zero_group())


"""
part 2:
A group is a collection of programs that can all communicate via pipes either directly or indirectly. 
The programs you identified just a moment ago are all part of the same group. 
Now, they would like you to determine the total number of groups.

In the example above, there were 2 groups: 
one consisting of programs 0,2,3,4,5,6, and the other consisting solely of program 1.

How many groups are there in total?
"""
def digital_plumber_group_count():
  connections = __get_connetions__()
  # traverse through each program mark the group it belongs to
  groupings = {}
  for p in connections:
    if p in groupings:
      continue
    group = {p}
    __check_connections__(p, connections, group)
    for member in group:
      groupings[member] = p
  return len(set(groupings.values()))
print(digital_plumber_group_count())