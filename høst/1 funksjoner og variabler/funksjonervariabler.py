print("hei på deg") # en innebygd funksjin som printer "hei på deg" i terminalen
input("hva heter du") # en innebygd funksjon som printer argumentet og lar brukeren skrive inn noe og returnerer det brukeren skriver inn

#argumenter
print("hei på deg") #funksjonen kan ta imot argumenter imellom parantesene

print("hei", "verden", end="  ", sep="!")

#strings
## strings skrives mellom anførselstegn

def si_hei(til):
    print("hei", til)

def spør_om_navn():
    navn = input("hva navn")
    return navn

spør_om_navn()
si_hei("thor")