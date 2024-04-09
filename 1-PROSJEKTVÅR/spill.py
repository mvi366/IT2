import pygame

# 1 oppsett
pygame.init()
BREDDE = 1000
HOYDE = 600
vindu = pygame.display.set_mode((BREDDE, HOYDE))
FPS = 60
klokke = pygame.time.Clock()

bakgrunn_bilde = pygame.image.load("bilder/baknatt.png").convert_alpha()



# Startposisjonen til bakgrunnen
bakgrunn_x = 0

while True:
    # 2. håndterer spillet
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    # 3. oppdater spillet
    # Flytt bakgrunnen kontinuerlig mot venstre
    bakgrunn_x -= 5
    # Hvis bakgrunnen går ut av skjermen, start på nytt fra høyre side
    if bakgrunn_x <= -BREDDE:
        bakgrunn_x = 0
    
    # 4. tegn
    # Tegn bakgrunnen på nytt for å lage scrolling effekt
    vindu.blit(bakgrunn_bilde, (bakgrunn_x, 0))
    # Tegn den samme bakgrunnen igjen for å fylle resten av skjermen
    vindu.blit(bakgrunn_bilde, (bakgrunn_x + BREDDE, 0))
    
    pygame.display.flip()
    klokke.tick(FPS)

