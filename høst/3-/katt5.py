def main():
    antall = hent_nummer()
    print_mjau(antall)

def hent_nummer():
    while True:
        antall = int(input("skriv et positivt tall:"))
        if antall > 0:
            return antall 
        print("ugyldig tall")


def print_mjau(antall):
    print("mjau\n" * antall, end="")



main()