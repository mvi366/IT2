


def fjern_falske_brukere(brukerliste, nokkelord): 
    ekte_brukere = []
    for bruker in brukerliste:
        if nokkelord not in bruker:
            ekte_brukere.append(bruker) 
    return ekte_brukere

print(fjern_falske_brukere(["thorc", "ravim", "fredrikg"], "fred"))


