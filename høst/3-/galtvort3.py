hus = {
    "hermine": "gryffing",
    "harry": "gryffing",
    "draco": "smygard"
}

print(hus["hermine"])

for elev in hus:
    print(elev, hus[elev], sep=": ")
    print(f"{elev} ({hus[elev]})")
    