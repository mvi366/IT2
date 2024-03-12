from random import*
n = int(input("hvor mange terninger vil du kaste?"))

resultater = []

def kast_terninger(n):
    for i in range(n):
        terningkast = randint(1,6)
        resultater.append(terningkast)
        
    return terningkast



print(kast_terninger(n))
print(resultater)
