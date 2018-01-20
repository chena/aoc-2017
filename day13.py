from copy import deepcopy
"""
http://adventofcode.com/2017/day/13
* Chinese room theorem
"""
def packet_scan_severity(packets):
  severity = 0
  for depth, length in packets.items():
    if depth % (2 * (length - 1)) == 0:
      severity += depth * length
  return severity

def packet_scan_check(packets, delay=0):
  for depth, length in packets.items():
    if (depth + delay) % (2 * (length - 1)) == 0:
      return False
  return True

def cross_firewall(file='input/packets.txt'):
  with open(file) as f:
    content = [p.strip() for p in f.readlines() if p]
  packets = {}
  for p in content:
    depth, length = p.split(': ')
    packets[int(depth)] = int(length)
  # part 1: calculate severity
  # return packet_scan_severity(packets)
  # part 2: increment delay until scan check passes
  delay = 0
  while not packet_scan_check(packets, delay):
    delay += 1
  return delay

print(cross_firewall())