import math

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

print(spiral_memory(57))

