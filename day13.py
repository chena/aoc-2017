from copy import deepcopy
"""
http://adventofcode.com/2017/day/13
"""
def __move_packets__(packets):
  for rr in packets.values():
    if rr[2]:
      rr[0] -=1
    else:
      rr[0] += 1
    if rr[0] == 0 or rr[0] == rr[1] - 1:
      rr[2] = not rr[2]
  # print packets

def packet_scanner(packets, max_depth):  
  severity = 0
  for d in range(max_depth + 1):
    if d in packets:
      r =  packets[d]
      if r[0] == 0:
        severity += d * r[1]
    __move_packets__(packets)
  return severity

def packet_scan_check(packets, max_depth, delay=0):
  for n in range(delay):
    __move_packets__(packets)

  caught = False
  for d in range(max_depth + 1):
    if d in packets:
      r =  packets[d]
      if r[0] == 0:
        caught = True
        break
    __move_packets__(packets)
  return caught

def packet_scanner_delay(file='input/packets_small.txt'):
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
  # increment delay until severity becomes 0
  delay = 0
  severity = 0
  while True:
    # print delay
    if not packet_scan_check(deepcopy(packets), max_depth, delay):
      break
    else:
      delay += 1
  return delay

print(packet_scanner_delay())