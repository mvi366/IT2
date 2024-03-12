import os
import sys
import json

def rens_terminal():
    if sys.platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# 1. oppsett
# åpner json-filen og putter alt innholdet i variabelen data
print("-- velkommen til pokemon-fantasy --")
with open("representanter.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
pokemons = data["dagensrepresentanter_liste"]
#oppretter liste med politiker-objekter

trener = []
for trener_ordbok in pokemons:
    ny_trener = Trener(trener_ordbok)
    pokemon.append(ny_politiker)

while True:
    rens_terminal()
    print("-- stortinget-fantasy --")
    
    print("1: vis politiker oversikt")
    print("2: avslutt")

    brukervalg = input(">")
  
    if brukervalg == "1":
        print("-- Politikeroversikt --")
        for politiker in politikere:
            print(politiker)
        input("Trykk enter for å gå tilbake til hovedmenyen")
        
    if brukervalg == "2":
        print("avslutter..")
        break

print("takk for nå")