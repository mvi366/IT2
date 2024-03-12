temp = float(input("hva er temp din?"))

if temp >= 36.5 and temp <= 37.5:
    print("normal temp")
elif temp < 36.5:
    print("lavere enn normal")
elif temp > 37.5:
    print("høyere enn normal")