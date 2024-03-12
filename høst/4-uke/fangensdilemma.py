def beregn_score(valg_spiller1, valg_spiller2):
    poeng_spiller1 = 0
    poeng_spiller2 = 0

    if valg_spiller1 == "samarbeid" and valg_spiller2 == "samarbeid":
        poeng_spiller1 = 3
        poeng_spiller2 = 3
    elif valg_spiller1 == "samarbeid" and valg_spiller2 == "svik":
        poeng_spiller1 = 0
        poeng_spiller2 = 5
    elif valg_spiller1 == "svik" and valg_spiller2 == "samarbeid":
        poeng_spiller1 = 5
        poeng_spiller2 = 0
    elif valg_spiller1 == "svik" and valg_spiller2 == "svik":
        poeng_spiller1 = 1
        poeng_spiller2 = 1

    return [poeng_spiller2, poeng_spiller1]


def spill_snilt(motspiller):
    antall_samarbeid = motspiller.count("svik")
    antall_svik 




        
