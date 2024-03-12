# et program som fortsetter helt til bruker har skrevet riktig input


år = 2024 # oppretter variabelen år slik at år får verdien 2024

while True: # while løkke som kjører hele tiden
    try:  # forsøk å kjør koden
        alder = int(input("hvor gammel blir du i år?")) # oppretter variabelen alder, som får verdien av det brukeren skriver inn.
        break # hopper ut av løkker
    except: # hvis koden ikke funker vil dette skje
        print("ugyldig input. input må være et tall") # print "ugyldig unput" hvis koden ikke funker
fødselsår = år - alder # finner fødselsår ved å ta året minus alderen brukeren blir i år.
print(f" du er født i {fødselsår}") # printer når brukeren ble født