
def initials(phrase):
  phraseList = phrase.split()
  myAcronym = []

  for word in phraseList:
    myAcronym.append(word[0].upper())

  return "".join(myAcronym)

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS