import random

def main():
    print("velkommen til troskapstesten")
    spiller1 = 0
    spiller2 = 0
    for i in range(500):
        resultat = spill(usikker, halveis)
        spiller1 += resultat[0]
        spiller2 += resultat[1]
        
        
    print(resultat)

def snill(beløp):
    # en funksjon for en snill strategi
    return "behold"

def slem(beløp):
    # en funksjon for en snill strategi
    return "kast"

def halveis(beløp):
    if beløp >= 50000:
        return "kast"
    else:
        return "behold"

def veldigusikker(beløp):
    tilfeldig_tall = random.randint(1, 100)
    if tilfeldig_tall <= 50:
        return "behold"
    else:
        return "kast"


def usikker(beløp):
    # en funksjon for en spiller som 30% av gangene kaster kulen når beløpet er under 50000
    # og kaster kulen 70% av gangene når beløpet er 50000 eller mer
    tilfeldig_tall = random.randint(1,100)
    if beløp < 50000:
        if tilfeldig_tall <= 30:
            return "kast"
        else:
            return "behold"
    else: 
        if tilfeldig_tall <= 70:
            return "kast"
        else:
            return "behold"

def spill(strategi1, strategi2):
    #funksjonen returnerer en liste med gevinsten til hver spiller
    # f eks [10000, 0] eller [10000, 15000] osv
    pott = 0
    for i in range(30):
        pott += 10000 
        if strategi1(pott) == "kast":
            return [pott, 0]
        elif strategi2(pott) == "kast":
            return [0, pott]
    return [pott / 2, pott / 2]
main()