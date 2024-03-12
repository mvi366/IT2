


class Person:
    """
        Klasse for en person.

        Parametre: 
            fornavn (str): Personens fornavn
            etternavn (str): Personens etternavn
            fodselsdato (int): personened fodelsdato
    """
    def __init__(self, navn: str, etternavn: str, fodselsar: int):
        self.navn = navn
        self.etternavn = etternavn
        self.fodselsar = fodselsar


    def beregn_alder(self):
        return 2023 - self.fodselsar

    def vis_info(self):
        print(f"{self.navn} {self.etternavn} ({self.beregn_alder()})")

class Lærer(Person):
    def __init__(self, navn: str, etternavn: str, fodselsar: int, fag: str):
        super().__init__(navn, etternavn, fodselsar)
        self.fag = fag
class Elev(Person):
    def __init__(self, navn: str, etternavn: str, fodselsar: int, klassetrinn: str):
        super().__init__(navn, etternavn, fodselsar)
        self.klassetrinn = klassetrinn

class Rektor(Person):
    def __init__(self, navn: str, etternavn: str, fodselsar: int, skole: str):
        super().__init__(navn, etternavn, fodselsar)
        self.skole = skole


eva = Lærer("eva", "coward", 1960, "matte")
camilla = Elev("camilla", "coward", 1999, 3)

person1 = Person("sibbila", "hanssen", 2005)
person2 = Person("julie", "johansen", 2005)
person3 = Person("thor", "christian", 1999)


print(person1.navn)

print(person1.beregn_alder())
person2.vis_info()