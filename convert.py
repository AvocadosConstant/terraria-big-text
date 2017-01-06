# Terraria chat message tags can be used to display items in chat.
# This is done with the format: [i:<unique_item_id>]
# There exist statues in the game that depict alphanumeric characters.
# This program conveniently converts plaintext into statue chat tags.

import sys

# Big 0 Statue Item ID offset by ASCII 0
CONST_BIG_0 = 2702 - ord('0')

# Big A Statue Item ID offset by ASCII A
CONST_BIG_A = 2712 - ord('A')

# Converts a char to the string code for an equivalent big letter statue
def charToBig(c):
  if c.isdigit():
    return "[i:" + str(ord(c) + CONST_BIG_0) + "]"
  if c.isalpha():
    return "[i:" + str(ord(c) + CONST_BIG_A) + "]"
  return c

# Converts a string to the codes for equivalent big letter statues
def strToBig(raw):
  output = ""
  for c in raw.upper():
    output += charToBig(c)
  return output

# Main
if len(sys.argv) > 1:
  print(strToBig(sys.argv[1]))
else:
  print("Enter plaintext:")
  print("Translated:\n" + strToBig(input()))
