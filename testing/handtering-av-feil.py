# et program som finner fødselsår basert på alder
år = 2024
try:
    alder = int(input("hvor gammel blir du i år"))
    fødselsår = år - alder
    print(f"du er født i {fødselsår}")
except:
    print("Ugyldig input. input må være et tall")


print("koden fortsetter..")


# et annet eksempel
try:
    tall = int(input("skriv et tall:"))
except:
    print("ugyldig input. setter 'tall' til 10")
    tall = 10

print(tall) #tall er 10 hvis brukeren ikke skriver inn et tall i input