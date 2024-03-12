
class Pokemon:
    def __init__(self, pokemon_ordbok: dict) -> None:
        self.fornavn: str = pokemon_ordbok["fornavn"]
        self.etternavn: str = pokemon_ordbok["etternavn"]
        self.kjønn: str = "kvinne" if pokemon_ordbok["kjoenn"] == 1 else "mann"
        self.fylke: str = pokemon_ordbok["fylke"]["navn"]
        self.parti: str = pokemon_ordbok["parti"]["navn"]
        self.komiteer = [komite["navn"] for komite in trener_ordbok["komiteer_liste"]]
        self.ukepoeng: list[int] = []
        self.verdi: int = 1000
 
    def __str__(self) -> str:
        # bestemmer hvordan en trener skal printes
        return f"{self.etternavn}, {self.etternavn} ({self.parti})"
    
    def gi_ukepoeng(self, poeng: int) -> None:
        self.ukepoeng.append(poeng)
    def vis_parti(self):
        print(f"--{self.navn} --")
        print(f"poeng: {self.poeng}")
        print(f"saldo: {self.saldo}")
        print("Medlemmer")
        for trener in self.trenere:
            print(trener)
        print() # tom linje

if __name__ == "__main__":
    print("tester trener klassen")
    