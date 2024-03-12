class Spiller():
    def __init__(self, navn: str) -> None:
        self.navn = navn
        self.antall_kamper = 0

    def hent_navn(self):
        return self.navn

    def hent_antall_kamper(self):
        return self.antall_kamper

    def spill_kamp(self):
        self.antall_kamper += 1

    def sjekk_navn(self, sjekk_navn):
        return sjekk_navn in self.navn
    
    # spiller.py
class Spiller:
    def __init__(self, navn):
        self.navn = navn
        self.antall_kamper = 0

    def hent_navn(self):
        return self.navn

    def hent_antall_kamper(self):
        return self.antall_kamper

    def spill_kamp(self):
        self.antall_kamper += 1

    def sjekk_navn(self, sjekk_navn):
        return sjekk_navn in self.navn
