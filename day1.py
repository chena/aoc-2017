"""
part 1:
find the sum of all digits that match the next digit in the list. 
The list is circular, so the digit after the last digit is the first digit in the list.

For example:

1122 produces a sum of 3 (1 + 2)
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit matches the next.
91212129 produces 9.
"""
def inverse_captcha(num):
	arr = [int(x) for x in str(num)]
	digit_count = len(arr)
	return sum(arr[n] if arr[n] == arr[(n + 1) / digit_count] else 0 for n in range(digit_count))
# print(inverse_captcha('91212129'))

"""
part 2:
consider the digit halfway around the circular list.

For example:

1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
1221 produces 0, because every comparison is between a 1 and a 2.
123425 produces 4, because both 2s match each other, but no other digit has a match.
123123 produces 12.
12131415 produces 4.
"""
def inverse_captcha_halfway(num):
	arr = [int(x) for x in str(num)]
	digit_count = len(arr)
	halfway = digit_count / 2
	return sum(arr[n] if arr[n] == arr[n % halfway if n >= halfway else n + halfway] else 0 for n in range(digit_count))
print(inverse_captcha_halfway(123123))