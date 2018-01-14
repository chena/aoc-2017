def reverse_string_oneline(input):
  return input[::-1]

def reverse_string_inplace(input):
  start = 0
  end = len(input) - 1
  input = list(input)
  while start < end:
    temp = input[start]
    input[start] = input[end]
    input[end] = temp
    start += 1
    end -= 1
  return ''.join(input)

def reverse_string_recursive(input):
  if len(input) < 2:
    return input
  return input[-1] + reverse_string_recursive(input[:-1])


to_reverse = 'alice'
print(reverse_string_oneline(to_reverse))
print(reverse_string_inplace(to_reverse))
print(reverse_string_recursive(to_reverse))