# algoritme 1 høyeste tall i en liste

def høyeste(liste: list(int)):
    høyest = liste[0]
    for tall in liste:
        if tall > høyest:
            høyest = tall
    return høyest


# algoritme 2

def gjennomsnitt(liste: list(int)):
    total = 0
    antall = 0
    for tall in liste:
        total = total + tall
        antall += 1
    return total, antall


def nest_høyest(liste: list(int)):
    nest_høyest = 


def n_høyeste(liste: list[int], n: int):
    høyeste_n = []
    for i in range(n):
        høyest = høyeste(liste)
        liste.remove(høyest)
        høyeste_n.append(høyest)

    return høyeste_n

print(n_høyeste([1, 2,3,4,5,6,-5,-6]), 2)
