from collections import defaultdict
"""
http://adventofcode.com/2017/day/20

part 1: Which particle will stay closest to position <0,0,0> in the long term?
part 2: How many particles are left after all collisions are resolved?
"""
class Particle:
  def __init__(self, values):
    p, v, a = values
    self.p = self.parse(p)
    self.v = self.parse(v)
    self.a = self.parse(a)

  def parse(self, inp):
    return [int(v) for v in inp.strip().split(',')]

  def distance(self):
    return sum([abs(v) for v in self.p])

  def next(self):
    self.v[0] += self.a[0]
    self.v[1] += self.a[1]
    self.v[2] += self.a[2]
    self.p[0] += self.v[0]
    self.p[1] += self.v[1]
    self.p[2] += self.v[2]
  
  def __str__(self):
    return str(self.p)

def __parse_particles__():
  with open('input/buffer.txt') as f:
    content = f.readlines()
  particles = []
  for line in content:
    values = [v.strip()[2:][1:-1] for v in line.split(', ')]
    particles.append(Particle(values))
  return particles

def particle_closest():
  particles = __parse_particles__()
  count = 0
  while count < 1000:
    count += 1
    distances = [p.distance() for p in particles]
    closest = distances.index(min(distances))
    print closest
    for p in particles:
      p.next()

def particle_eliminate_collisions():
  particles = __parse_particles__()
  count = 0
  while count < 100:
    for p in particles:
      p.next()
    positions = defaultdict(list)
    for par in particles:
      positions[tuple(par.p)].append(par)
    for to_destroy in [pars for pars in positions.values() if len(pars) > 1]:
      for d in to_destroy:
        particles.remove(d)
    print len(particles)
    count += 1

# particle_closest() # part 1
particle_eliminate_collisions() # part 2