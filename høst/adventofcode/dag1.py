fil = open("input.txt")
data = fil.read()
linjer = data.split("\n")

print(linjer)

sum = 0
for linje in linjer: 
    tall = []
    for bokstav in linje:
        if bokstav.isdigit():
            #print("er tall", bokstav)
            tall.append(bokstav)
        #print(bokstav)
   # print("ny linje")
    print(tall)
    først_og_sist = tall[0] + tall[-1]
    print(først_og_sist)
    sum += int(først_og_sist)

print(sum)
    