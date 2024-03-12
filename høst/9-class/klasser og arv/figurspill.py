import pygame
from figur import Figur 

class Spiller(Figur):
    def __init__(self, bildesti: str, x: int, y: int, navn) -> None:
        super().__init__(bildesti, x, y)
        self.navn = navn


class Fiende(Figur):
    def __init__(self, bildesti: str, x: int, y: int, navn) -> None:
        super().__init__(bildesti, x, y)
        self.antall_liv = 100

# 1 op

# 1 oppsett
pygame.init()
BREDDE = 500
HOYDE = 500
vindu = pygame.display.set_mode((BREDDE, HOYDE))
FPS = 60
klokke = pygame.time.Clock()


        
while True:
    # 2. håndterer spillet
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    # 3. oppdater spikk
    # 4. tegn
    pygame.display.flip()
    klokke.tick(FPS)