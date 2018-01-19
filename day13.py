"""
http://adventofcode.com/2017/day/13
"""
def packet_scanner(file='input/packets.txt'):
  with open(file) as f:
    content = [p.strip() for p in f.readlines() if p]
  # packets maps the depth to the current position, the range,
  # and the direction of scanning of each layer 
  # (False if going down, True if going up)
  packets = {}
  max_depth = None
  for p in content:
    parts = p.split(':')
    depth = int(parts[0].strip())
    packets[depth] = [0, int(parts[1].strip()), False]
    max_depth = depth
  severity = 0
  for d in range(max_depth + 1):
    if d in packets:
      r =  packets[d]
      if r[0] == 0:
        severity += d * r[1]
    for rr in packets.values():
      if rr[2]:
        rr[0] -=1
      else:
        rr[0] += 1
      if rr[0] == 0 or rr[0] == rr[1] - 1:
        rr[2] = not rr[2]
  return severity

print(packet_scanner())