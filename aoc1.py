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
# print(corruption_checksum_divisible([[5, 9, 2, 8],[9, 4, 7, 3],[3, 8, 6, 5]]))
# print(corruption_checksum_divisible(__parse_checksum_input__('input/checksum_input.txt')))

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

def __parse_passphrase_input__(filename):
	with open(filename) as f:
		content = f.readlines()
	rows = []
	for line in content:
		rows.append([w for w in line.strip().split()])
	return rows

def valid_passphrase(passphrases):
	valid_count = 0
	for p in passphrases:
		m = {}
		for w in p:
			w = ''.join(sorted(w))
			if w in m:
				m[w] += 1
			else:
				m[w] = 1
		if sum(m.values()) == len(m.keys()):
			valid_count += 1
		print(m)
	return valid_count
# print(valid_passphrase([['abcde', 'xyz', 'ecdab']]))
# print(valid_passphrase(__parse_passphrase_input__('input/passphrases.txt')))

def __parse_maze_input__(filename):
	with open(filename) as f:
		content = f.readlines()
	return [int(n) for n in content]

def maze_of_twisty(maze):
	steps = 0
	index = 0
	while (index < len(maze)):
		move_forward = maze[index]
		if (move_forward >= 3):
			maze[index] -= 1
		else:
			maze[index] += 1
		index += move_forward
		steps += 1
	return steps
# print(maze_of_twisty([0, 3, 0, 1, -3]))
print(maze_of_twisty(__parse_maze_input__('input/maze.txt')))

