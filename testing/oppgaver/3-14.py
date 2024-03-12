
while True:

    navn = input("hva er navnet ditt")
    splittet_navn = navn.split(" ")
    antall_navn = len(splittet_navn)
    if antall_navn >= 2:    
        siste_navn = splittet_navn[-1]
        print(f"din mail er {splittet_navn[0]}{siste_navn[0]}@afk.no")
        break
    else:
        print("ugyldig unput. må være minst to navn")
        
