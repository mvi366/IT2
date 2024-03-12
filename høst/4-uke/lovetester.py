navn1 = input("hva er det første navnet?")
navn2 = input("hva er det andre navnet?")
bosted1 = input("hvor bor navn1")
bosted2 = input("hvor bor navn2")
alder1 = int(input("hva er alderen til den første?"))
alder2 = int(input("hva er alderen til den andre?"))
navn1 = navn1.lower()
navn2 = navn2.lower()

lengde1 = len(navn1)
lengde2 = len(navn2)

første1 = navn1[0]
første2 = navn2[0]


if lengde1 == lengde2:
    match = 60
elif første1 == første2:
    match = 40
else: 
    match = 15

if bosted1 == bosted2:
    match = match *1.5

if alder1 < alder2 / 2 + 7 or alder2 < alder1 / 2 + 7:
    match = match / 2
elif alder1 == alder2:
    match = match * 1.1

if "t" in navn1 or "a" in navn1 or "t" in navn2 or "a" in navn2:
    match = match +2 
if ("s" in navn1 and "e" in navn1 and "e" not in navn2) or ("s" in navn2 and "e" in navn2 and "e" not in navn1):
    match = match + 15
if navn1[0] not in navn2:
    match = match - 20

print(match,"%")