liste = ["Sauer", "er", "myke", "dyr."]

for i in liste:
    print(i)

tall = [6, -4, 7, -2, 8, -3, 9, -11]
minst = tall[0]
storst = tall[0]

for i in tall:
    if i < minst:
        minst = i


for i in tall:
    if i > storst:
        storst = i

print(minst)
print(storst)
