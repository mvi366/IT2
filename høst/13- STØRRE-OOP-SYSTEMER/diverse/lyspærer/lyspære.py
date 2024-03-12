#lyspære
class Lyspære():
    def __init__(self) -> None:
        self._på = False
    def tenn(self):
        self._på = True
    def slukk(self):
        self._på = False
    def er_på(self):
        # returnere true hvis pæren er på og false hvis pæren er av
        return self._på
min_pære = Lyspære()
soverom_pære = Lyspære()
stue_pære = Lyspære()


if __name__ == "__main__":
        
    min_pære.tenn()
    min_pære._på = True
    stue_pære.tenn()

    if stue_pære._på:
        print("pæren i stuen er på")
