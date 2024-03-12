
personer = [

    {
        "navn": "thor"
        "alder": 33
    },
    {
        "navn": "ravi"
        "alder": 39
    },
    {
        "navn":"ingrid"
        "alder": 21
    }


]

sortert_personer = sorted(personer, key=lambda person:person["alder"])
topp_2 = sortert_personer[:2]
print(topp_2)