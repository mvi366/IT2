

class Sang():
    def __init__(self, tittel, navn) -> None:
        self.tittel = tittel
        self.artist = navn
        self.avspillinger = 0
    

    def spill(self):
        print(f"spiller {self.tittel} - {self.artist}")
        self.avspillinger += 1

    def sjekk_tittel(self, tittel):
        
        if self.tittel == tittel:
            return True
        else:
            return False
    def sjekk_artist(self, artist):
        if self.artist == artist:
            return True
        else:
            return False
    def __repr__(self) -> str:
        return f"{self.artist} - {self.tittel}"
        
sang1 = Sang("Jackie Down The Line", "Fontaines DC")
sang2 = Sang("SANG2", "artist2")
sang3 = Sang("SANG3", "artist2")
sang1.spill()
print(sang1.sjekk_tittel("Jackie Down The Line"))
print(sang1.sjekk_artist("Fontaines DC"))


