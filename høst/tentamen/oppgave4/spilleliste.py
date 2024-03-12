from sang import Sang


class Spilleliste():
    def __init__(self, navn) -> None:
        self.navn = navn
        self.sanger = []

    def legg_til_sang(self, sang):
        self.sanger.append(sang)

    def lengde(self):
        return len(self.sanger)
    

    def spill_alle(self):
        for sang in self.sanger:
            sang.spill()
    
    def tittel_i_liste(self, tittel):
        
        for sang in self.sanger:
            if sang.tittel == tittel:
                return True
        for sang in self.sanger:
            if sang.tittel != tittel:
                return False   

         

    def artistliste(self, artist):
        sanger_artist = []
        for sang in self.sanger:
            if sang.artist == artist:
                sanger_artist.append(sang)
        return sanger_artist


sang1 = Sang("Jackie Down The Line", "Fontaines DC")
sang2 = Sang("Oslo vet", "Evig Ferie")
sang3 = Sang("Seint i går", "Evig Ferie")

spilleliste1 = Spilleliste("Norske favoritter")
spilleliste1.legg_til_sang(sang1)
spilleliste1.legg_til_sang(sang2)
spilleliste1.legg_til_sang(sang3)

print(spilleliste1.lengde())
spilleliste1.spill_alle()

print(spilleliste1.tittel_i_liste("sang1"))

print(spilleliste1.artistliste("Evig Ferie"))



            
        
