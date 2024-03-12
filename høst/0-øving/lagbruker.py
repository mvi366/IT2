navn = input("hva er navnene?")

def lag_brukernavn(navn):
    brukernavn = navn.lower()
    brukernavn = brukernavn.split(" ")
    return brukernavn[0] + brukernavn[1][0]

print(lag_brukernavn)