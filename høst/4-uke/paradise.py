# TROSKAPSTESTEN simulering


def main():
    pott = 0
    print("velkommen til troskapstesten")
    for i in range(10):
        pott += 10000
        print(f"runde {i + 1}: {pott}, -")
        if not snill_spiller(pott):
            print("snill spiller kastet kulen")
            break
        elif annen_spiller(pott) == False:
            print("slem spiller kastet kulen")
            break

def snill_spiller(beløp):
    return True # beholder kulen

def slem_spiller(beløp):
    return False

def annen_spiller(beløp):
    if beløp >= 50000:
        return False
    else:
        return True
    
main()