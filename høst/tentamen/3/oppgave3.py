


# 3.1
def per_stream(land): 
    utbetaling = 0
    if land == "Norge":
        utbetaling = 0.55
    elif land == "Sverige" or land == "Finland":
        utbetaling = 0.44
    elif land == "Danmark":
        utbetaling = 0.52 
    elif land == "Island":
        utbetaling = 0.62
    else:
        utbetaling = 0.24
    return utbetaling


print(per_stream("Norge"))
print(per_stream("Island"))

# 3.2
def andel_til_artist(antall_streams):
    
    if antall_streams <= 399999:
        andel = 0
    elif antall_streams >= 400000 and antall_streams <= 29999999:
        andel = 0.40
    elif antall_streams >= 30000000:
        andel = 0.70
    return andel

print(andel_til_artist(50000))
print(andel_til_artist(5000000))


# 3.3
def penger_tjent(antall_streams, land):
    tjent = antall_streams * per_stream(land) * andel_til_artist(antall_streams)
    return tjent

print(penger_tjent(5_000_000, "Norge"))
print(penger_tjent(100_000_000, "Island"))


#3.4

artister = [
    ["Taylor Swift",  109_940_000],
    ["The Weeknd",    105_410_000],
    ["Justin Bieber",  83_820_000],
    ["Drake",          81_980_000],
    ["Ariana Grande",  81_800_000]
]

def populære(artistliste):
    populære_artister = []
    for artist in artistliste:
        if artist[1] > 100_000_000:
            populære_artister.append(artist)
    return populære_artister

print(populære(artister))
            

#3.5

artister1 = [
    ["Sígur Ros",        "Island", 1_047_010],
    ["Emma Steinbakken", "Norge",  3_459_239]
]


def royalties(artistliste):
    stor_liste = []
    
    for artist in artistliste:
        ny_liste = []
        penger_tjent_spotify = penger_tjent(artist[2], artist[1])
        ny_liste.append(artist[0])
        ny_liste.append(penger_tjent_spotify)
        stor_liste.append(ny_liste)
    return stor_liste



print(royalties(artister1))