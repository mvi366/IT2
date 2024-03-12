import random 

#gameloop-mønsteret

# 1. oppsett

magisk_tall = random.randint(1,10)
antall_forsøk = 0
# gameloop:
spill = True

while spill:
    # 2. håndterer input
    brukerinput = input("hva er d magiske tallet?")
    if brukerinput == "avslutt":
        break
    tall = int(brukerinput)

    # 3. oppdater spill
    antall_forsøk += 1

    # 4. tegn (print)
    if tall > magisk_tall:
        print("for høyt")
    elif tall < magisk_tall:
        print("for lavt")
    else:
        print(f"riktig. antall forsøk: {antall_forsøk}")

        break