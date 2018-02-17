"""
http://adventofcode.com/2017/day/19/input

     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
"""
DIRECTIONS = {'|': 'updown', '-': 'side'}

def tubes():
	with open('input/route.txt') as f:
		content = f.readlines()
	puzzle = [r.replace('\n', '') for r in content]
	current = '|'
	i = 0
	j = puzzle[0].index(current)
	d = 'down'
	letters = []
	steps = 0
	while current != ' ':
		steps += 1
		if d == 'down':
			i += 1
		elif d == 'up':
			i -= 1
		elif d == 'right':
			j += 1
		elif d == 'left':
			j -= 1
		current = puzzle[i][j]
		if current.isalpha():
			letters.append(current)
		elif current == '+': # turn
			if d in ['down', 'up']: # turn left or right
				d = 'left' if puzzle[i][j - 1] != ' ' else 'right'
			else: # turn up or down
				d = 'up' if puzzle[i - 1][j] != ' ' else 'down'
	# return ''.join(letters) # part 1
	return steps # part 2

print(tubes())