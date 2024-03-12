
poeng = 0


print("Velkommen til Quiz")
print("Hva er hovedstaden i Danmark?")
print("svaralternativer: A: Oslo, B: København, C: Amsterdam")
svar = input("ditt svar: ")
if svar == "B" or svar == "b":
    print("Riktig")
    poeng += 1
    print("nå har du", poeng, "poeng")
else: 
    print("feil svar")
    print("nå har du", poeng, "poeng")