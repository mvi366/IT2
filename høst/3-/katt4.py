
while True:
    antall = int(input("hvor mange katter har du?"))
    if antall > 0:
        break #hopper ut av løkken
    print("ugyldig, prøv igjen")


while True:
    antall = int(input("hvor mange katter har du?"))
    if antall < 0 :
        print("ugyldig prlv ignen")
    else:
        break
for _ in range(antall):
    print("mjau")