import sys

CONST_BIG_0 = 2702
CONST_BIG_A = 2712

def charToBig(c):
  val = ord(c)
  if c.isdigit():
    return "[i:" + str(val - ord('0') + CONST_BIG_0) + "]"
  if c.isalpha():
    return "[i:" + str(val - ord('A') + CONST_BIG_A) + "]"
  return c

def strToBig(raw):
  output = ""
  for c in raw.upper():
    output += charToBig(c)
  return output

print(strToBig(sys.argv[1]))
