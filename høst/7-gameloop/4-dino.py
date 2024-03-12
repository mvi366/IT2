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
dino_y = 300


dino_bilde2 = pygame.image.load("bilder/bakgrunn.png").convert_alpha()
dino2_x = 5
dino2_y = 500
dino_y_fart = 0
gravitasjon = 0.1

sirkel1_x = 500
sirkel1_y = 200
sirkel1_farge = "green"

sirkel2_x = 400
sirkel2_y = 400
sirkel2_farge = "green"

while True:
    # 2. håndterer input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    taster = pygame.key.get_pressed()
    if taster[pygame.K_UP]:
        print("pil opp")
        dino_y_fart =-2
        dino_y -= 5

    if dino_y > 200:
        dino_y_fart = 0
    else:
        dino_y_fart += gravitasjon
        dino_y += dino_y_fart
   
    # 3. oppdater spill
    dino_rektangel = pygame.Rect(dino_x,dino_y, 100, 100)
    sirkel1_rektangel = pygame.Rect(sirkel1_x,sirkel1_y,80, 80 )
    sirkel2_rektangel = pygame.Rect(sirkel2_x,sirkel2_y,80, 80 )

    if dino_rektangel.colliderect(sirkel1_rektangel):
        print("over sirkel 1")
        sirkel1_farge = "red"
    
    if dino_rektangel.colliderect(sirkel2_rektangel):
        print("over sirkel 2")
        sirkel2_farge = "red"
        



    # 4. tegn

    vindu.fill("gray")

    vindu.blit(dino_bilde1, (dino_x, dino_y))

    vindu.blit(dino_bilde2, (dino2_x, dino2_y))

    tekst_lykke_til = font.render("Dino", True, "blue")
    
    vindu.blit(tekst_lykke_til, (200, 100))
    pygame.draw.circle(vindu, sirkel1_farge, (sirkel1_x, sirkel1_y), 20)
    pygame.draw.circle(vindu, sirkel2_farge, (sirkel2_x, sirkel2_y), 20)
   


    print("en runde i gameloopen")
    pygame.display.flip()
    klokke.tick(FPS)