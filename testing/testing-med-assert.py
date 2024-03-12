
# assert 3 > 2 #sjekk at 3 er større enn 2
# assert 2 > 3 # feilmelding fordi det ikke stemmer

# test drevet utvikling med assert

## eksempel en funksjon som tester om tall er partall
def partall(tall: int):
    if tall % 2 == 0:
        return True
    else:
        return False
    
#for i in range(0, 1000, 2):
#    assert partall(i) == True
assert partall(2) == True 
assert partall(1) == False 
assert partall(-2) == True
assert partall(-1) == False