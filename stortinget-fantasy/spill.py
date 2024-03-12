import os
import sys
from politiker import Politiker
from fantasiparti import Fantasiparti
import json

def rens_terminal():
    if sys.platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# 1. oppsett
# åpner json-filen og putter alt innholdet i variabelen data
print("-- velkommen til stortinget-fantasy --")
with open("representanter.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
representanter = data["dagensrepresentanter_liste"]
#oppretter liste med politiker-objekter

politikere = []
for politiker_ordbok in representanter:
    ny_politiker = Politiker(politiker_ordbok)
    politikere.append(ny_politiker)


print("--- velkommen til Stortinget fantasy ----")
print()
print("hva skal partiet hete?")
navn = input("> ")
print("hva heter eieren av partiet?")
eier = input("> ")
spillerparti = Fantasiparti(navn, eier)


print()
print("Et nytt politisk parti er stiftet!")
print("trykk enter for å starte spillet")
input()


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
        print(" mitt parti"):
        spillerparti.vis_parti
        
    if brukervalg == "3":
        print("avslutter..")
        break

print("takk for nå")