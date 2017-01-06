def charToBig(c):
  val = ord(c)
  if val >= ord('0') and val <= ord('9'):
    return "[i:" + str(val - ord('0') + 2702) + "]"
  if val >= ord('A') and val <= ord('Z'):
    return "[i:" + str(val - ord('A') + 2712) + "]"
  return c

def strToBig(raw):
  output = ""
  for c in raw.upper():
    output += charToBig(c)
  return output

loop = True
while loop:
  print("\nEnter your string to be converted:")
  raw = input()

  print("Your converted text is:")
  print(strToBig(raw))
