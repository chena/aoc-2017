"""
A valid passphrase must contain no two words that are anagrams of each other - 
that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

how many passphrases are valid?
"""
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
print(valid_passphrase([['abcde', 'xyz', 'ecdab']]))
# print(valid_passphrase(__parse_passphrase_input__('input/passphrases.txt')))