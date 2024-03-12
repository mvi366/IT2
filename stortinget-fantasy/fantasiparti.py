from politiker import Politiker

class Fantasiparti:
    # En spesiell kode som kjøres når et fantasiparti opprettes
    def __init__(self, navn: str, eier: str) -> None:
        self.navn: str = navn
        self.eier: str = eier
        self.poeng: int = 0
        self.saldo: int = 100_000
        self.partileder: Politiker = None
        self.politikere: list[Politiker] = []

    def __str__(self) -> str:
        # en spesiell metode som bestemmer hvordan print skal se ut
        return f"{self.navn} - {self.eier} ({self.poeng}) poeng, {self.saldo} kr"
    
    def kjøp_politiker(self, politiker: Politiker):
        if self.saldo >= politiker.verdi and politiker not in self.politikere:
            self.saldo -= politiker.verdi
            self.politikere.append(politiker)
        else:
            print("FEIL!")
    
    def selg_politiker(self, politiker: Politiker):
        if politiker in self.politikere:
            self.politikere.remove(politiker)
            self.saldo += politiker.verdi
        else:
            print("Feil! politikeren er ikke med i partiet")

    def vis_parti(self):
        print(f"--{self.navn} --")
        print(f"poeng: {self.poeng}")
        print(f"saldo: {self.saldo}")
        print("Medlemmer")
        for politiker in self.politikere:
            print(politiker)
        print() # tom linje

if __name__ == "__main__":
    print("tester Fantasiparti-klassen")
    testparti_1 = Fantasiparti("Apolitisk Testparti", "Test Testesen")
    testparti_2 = Fantasiparti("Politisk testparti", "Stolt jensenberg")
    print(testparti_1)