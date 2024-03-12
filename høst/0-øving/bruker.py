def lag_brukernavn(navn):
    smaa = navn.lower()
    fullt_navn = smaa.split()
    return fullt_navn[0] + fullt_navn[1][0]

#print(lag_brukernavn(input("hva er navnene")))

def lag_epost(navn, skole):
    smaa = navn.lower()
    fullt_navn = smaa.split()
    skolesmaa = skole.lower()

    return fullt_navn[0] + fullt_navn[1][0] + "@" + skolesmaa + ".viken.no"


skole = input("hvilken skole")
navn = input("hva er navnene")

print(lag_epost(navn, skole) )

