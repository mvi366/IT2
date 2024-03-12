class Spiller():
    def __init__(self, navn) -> None:
        self.kamper = 0
        self.navn = navn

    def spill_kamp(self):
        self.kamper += 1

    def hent_navn(self):
        return self.navn
    
    def hent_kamper(self):
        return self.kamper

    def sjekk_navn(self, navn: str):
        #returner true hvis spillerene innrholder ett av navnene
        if navn in self.navn:
            return True
        else: return False
