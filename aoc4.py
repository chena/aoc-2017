class Coordinate:
	movements = {
		'nw': (-1, 1),
		'n': (0, 2),
		'ne': (1, 1),
		'se': (1, -1),
		's': (0, -2),
		'sw': (-1, -1)
	}
	
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move(self, direction):
		movement = self.movements[direction]
		self.x += movement[0]
		self.y += movement[1]

	def __str__(self):
		return '({}, {})'.format(self.x, self.y)

def hex_ed(paths=[]):
	if not paths:
		with open('hex_ed.txt') as f:
			content = f.readline().strip()
		paths = content.split(',')
	# start moving
	location = Coordinate(0, 0)
	for direction in paths:
		location.move(direction)
	print('final location is: {}'.format(location))
	# calculate shortest distance
	x_distance = abs(location.x)
	y_distance = abs(location.y)
	return x_distance if x_distance > y_distance else (x_distance + y_distance) / 2

print(hex_ed(['se', 'sw', 'se', 'sw', 'sw']))
# print(hex_ed())
