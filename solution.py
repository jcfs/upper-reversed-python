aString = "Michelle ma belle these are words that go together well"

bString = ""
for index, word in enumerate(aString.split(" ")):
  if (index % 2 == 0):
    bString += word.upper()
  else:
    bString += word[::-1]
  bString += " "

#remove last character which is a space
#don't know if this is needed, since the example output has the space there
bString = bString[:-1]

print bString
