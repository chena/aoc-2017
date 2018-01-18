"""
part 1:
The characters represent groups - sequences that begin with { and end with }. 
Within a group, there are zero or more other things, separated by commas: either another group or garbage. 
Since groups can contain other groups, a } only closes the most-recently-opened unclosed group - that is, they are nestable. 
Your puzzle input represents a single, large group which itself contains many smaller ones.

Sometimes, instead of a group, you will find garbage. 
Garbage begins with < and ends with >. Between those angle brackets, almost any character can appear, including { and }. 
Within garbage, < has no special meaning.
Any character that comes after ! should be ignored, including <, >, and even another !.

Here are some self-contained pieces of garbage:

<>, empty garbage.
<random characters>, garbage containing random characters.
<<<<>, because the extra < are ignored.
<{!>}>, because the first > is canceled.
<!!>, because the second ! is canceled, allowing the > to terminate the garbage.
<!!!>>, because the second ! and the first > are canceled.
<{o"i!a,<{i<a>, which ends at the first >.
Here are some examples of whole streams and the number of groups they contain:

{}, 1 group.
{{{}}}, 3 groups.
{{},{}}, also 3 groups.
{{{},{},{{}}}}, 6 groups.
{<{},{},{{}}>}, 1 group (which itself contains garbage).
{<a>,<a>,<a>,<a>}, 1 group.
{{<a>},{<a>},{<a>},{<a>}}, 5 groups.
{{<!>},{<!>},{<!>},{<a>}}, 2 groups (since all but the last > are canceled).
Your goal is to find the total score for all groups in your input. 
Each group is assigned a score which is one more than the score of the group that immediately contains it. (The outermost group gets a score of 1.)

{}, score of 1.
{{{}}}, score of 1 + 2 + 3 = 6.
{{},{}}, score of 1 + 2 + 2 = 5.
{{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
{<a>,<a>,<a>,<a>}, score of 1.
{{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.

part 1:
What is the total score for all groups in your input?

part 2:
Count all of the characters within the garbage. 
The leading and trailing < and > don't count, nor do any canceled characters or the ! doing the canceling.

<>, 0 characters.
<random characters>, 17 characters.
<<<<>, 3 characters.
<{!>}>, 2 characters.
<!!>, 0 characters.
<!!!>>, 0 characters.
<{o"i!a,<{i<a>, 10 characters.

"""
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
    with open('input/stream.txt') as f:
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
print(stream_score(stream_processing()))
# print(stream_processing())