elever = [
    {"navn": "hermine", "hus": "griffing", "patronus": "oter"},
    {"navn": "harry", "hus": "griffing", "patronus": "hjort"},
    {"navn": "ronny", "hus": "griffing", "patronus": "hund"},
    {"navn": "draco", "hus": "smygard", "patronus": None}
]

for elev in elever:
    print(elev)


for elev in elever:
    print(elev["navn"], elev["hus"], elev["patronus"])

