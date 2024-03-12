import pygame
from fotballspiller import Fotballspiller
from ball import Ball


# 1. Oppsett
pygame.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
liten_font = pygame.font.SysFont("Arial", 12)
spiller = Fotballspiller(BREDDE, HOYDE)
ball = Ball(BREDDE)

ball = []

for _ in range(10):
    ball.append(Ball())


while True:
    # 2. Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    taster = pygame.key.get_pressed()
    if taster[pygame.K_LEFT]:
        spiller.flytt(-1) 
    if taster[pygame.K_RIGHT]:
        spiller.flytt(1)
    

    if taster[pygame.K_ESCAPE]:
        pygame.quit()
        
    if spiller.ramme.colliderect(ball.ramme):
        spiller.poeng += 1
        
    # 3. Oppdater spill
    ball.fall(HOYDE)
    for i in range (len(matbiter)-1, -1, -1):
        if ap.ramme.colliderect(matbit[i].ramme):
            ap.spis()
            # slette matbiten

    
    # 4. Tegn
    vindu.fill("black")
    tekst_lykke_til = font.render("poengsum:", spiller.poeng, True, "white")
    vindu.blit(tekst_lykke_til, (50, 10))
    spiller.tegn(vindu)
    ball.tegn(vindu)

    pygame.display.flip()
    klokke.tick(FPS)

     
    # 4. tegn
    vindu.fill("white")
    ap.tegn(vindu)
    sv.tegn(vindu)

    for matbit in matbiter:
        matbit.tegn(vindu)