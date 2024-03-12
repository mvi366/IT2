import pygame

# 1. oppsett
pygame.init()

BREDDE = 1000
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
liten_font = pygame.font.SysFont("Arial", 12)


dino_bilde1 = pygame.image.load("bilder/dino1.png").convert_alpha()
dino_x = 300


while True:
    # 2. håndterer input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    taster = pygame.key.get_pressed()
    if taster[pygame.K_RIGHT]:
        print("pil høyre")
        dino_x += 1
    if taster[pygame.K_LEFT]:
        print("pil venstre")
        dino_x -= 1
    if taster[pygame.K_ESCAPE]:
        pygame.quit()

    # 3. oppdater spill
    # 4. tegn

    vindu.fill("gray")

    vindu.blit(dino_bilde1, (dino_x, 500))
    tekst_lykke_til = font.render("Dino", True, "blue")
    
    vindu.blit(tekst_lykke_til, (200, 100))
    pg.draw
   


    print("en runde i gameloopen")
    pygame.display.flip()
    klokke.tick(FPS)

