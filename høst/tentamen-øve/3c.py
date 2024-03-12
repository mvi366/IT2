def fjern_utsolgte(handleliste, utsolgte):
    ny_liste = []
    for vare in handleliste:
        if vare not in utsolgte:
            ny_liste.append(vare)
    return ny_liste


print(fjern_utsolgte(["melk", "brus", "pasta"], ["kaffe", "brus"]))

