class Elev:
    """
    en klasse for elever på vgs
    
    attributter
        navn (str): navnet til eleven
        alder (int): alderen til eleven
        klasse( str): bokstavklassen til eleven (eks: STG)
        fag (list(str)): liste med fagene eleven tar

    metoder
        legg_til_fag (fag: str): legger et fag til i faglisten
        fjern_fag (fag: str): fjernet et fag fra fsglisten
        vis_info (): printer ut info om eleven
    """
    def __init__(self, navn: str, alder: int, klasse: str) -> None:
        self.navn: str = navn
        self.alder: int = alder
        self.klasse: str = klasse
        self.fag: list[str] = []
    def legg_til_fag(self, fag: str):
        self.fag.append(fag)
    
    def fjern_fag(self, fag: str):
        self.fag.remove(fag)
    
    def vis_info(self):
        print(f"{self.navn} ({self.alder})")


meg_selv = Elev("thor", 33, "STG")