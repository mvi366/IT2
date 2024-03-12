from lyspære import Lyspære

class Rom():
    def __init__(self) -> None:
        self._pærer: list[Lyspære] = []

    def legg_til_pære(self, pære):
        self._pærer.append(pære)

    def skru_på_lys(self):
        for pære in self._pærer:
            pære.tenn()

    def __str__(self) -> str:
        return f"rom: {len (self._pærer)}"

    def skru_av_lys(self):
        for pære in self._pærer:
            pære.slukk()
    def skru_av_lys_n(self, n: int):
        self._pærer[n].slukk()
    
    def skru_på_lys_n(self, n: int):
        self._pærer[n].tenn()
        



if __name__ == "__main__":
    print("tester rom.py")
    stue = Rom()
    for i in range(3):
        stue.legg_til_pære(Lyspære())
        
    stue.skru_på_lys()
    print(stue)



