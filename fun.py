import math

def inverse_captcha(num):
	arr = [int(x) for x in str(num)]
	digit_count = len(arr)
	return sum(arr[n] if arr[n] == arr[n + 1 if n < (digit_count - 1) else 0] else 0 for n in range(digit_count))
# print(inverse_captcha('91212129'))

def inverse_captcha_halfway(num):
	arr = [int(x) for x in str(num)]
	digit_count = len(arr)
	halfway = digit_count / 2
	return sum(arr[n] if arr[n] == arr[n % halfway if n >= halfway else n + halfway] else 0 for n in range(digit_count))
# print(inverse_captcha_halfway(123123))

def spiral_memory(num):
	if num < 2:
		return 0
	square_rooted = math.floor(math.sqrt(num))
	next_odd_square = (square_rooted + 1) if square_rooted % 2 < 1 else (square_rooted + 2)
	previous_odd = next_odd_square - 2
	ring_dist = math.floor(next_odd_square / 2)
	dist = (num - previous_odd ** 2) % (previous_odd + 1)
 	row_distnce = abs(dist - ring_dist)
	steps = row_distnce + ring_dist
	return steps
# print(spiral_memory(57))

