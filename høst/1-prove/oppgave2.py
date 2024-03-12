iso = input("hva er datoen i ISO-format?")
li = [iso.split("-")]
year = li[0][0]
month = li[0][1]
day = li[0][2]

norsk = day+"."+month+"."+year


print(norsk)