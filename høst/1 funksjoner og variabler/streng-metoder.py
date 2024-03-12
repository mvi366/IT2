#input er en funksjon som tar inn et argument og returnerer det brukerer skriver inn

navn = input("hva heter du? (fornavn og etternavn)")
#navn er en variabel som inneholder en string
print(navn)

fornavn, etternavn = navn.split(" ")
fornavn = fornavn.capitalize()

# print hallo, navn i terminalen
print("hallo", fornavn)
print("ditt fulle navn er:", navn)
navn = navn.title()



