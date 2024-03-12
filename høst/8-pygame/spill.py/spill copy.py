import pygame

# 1 oppsett
pygame.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

overskrift_font = pygame.font.SysFont("Arial", 32)
overskrift_surface = overskrift_font.render("Elon vs. musk", True, "black")

spiller_surface = pygame.image.load("bilder/viccypro.png").convert_alpha()
spiller_surface = pygame.transform.scale_by(spiller_surface, 0.2)
spiller_rect = spiller_surface.get_rect()
spiller_rect.bottom = HOYDE
spiller_rect.centerx = BREDDE / 2
spiller_fart = 0

fiende_surface = pygame.image.load("bilder/viccypro.png").convert_alpha()
fiende_surface = pygame.transform.scale_by(fiende_surface, 0.2)
fiende_rect = fiende_surface.get_rect()
fiende_rect.top = 100
fiende_rect.centerx = BREDDE / 2
while True:
    # 2. håndterer spillet
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if hendelse.type == pygame.KEYDOWN:
            if hendelse.key == pygame.K_LEFT:
                spiller_fart = - 1
            elif hendelse.key == pygame.K_RIGHT:
                spiller_fart = 1
        if hendelse.type == pygame.KEYUP:
            spiller_fart = 0


    # 3. oppdater spill
    fiende_rect.left -= 1
    print(fiende_rect.left)
    if fiende_rect.right < 0:
        fiende_rect.left = BREDDE
    spiller_rect.left += spiller_fart

    # 4. tegn
    vindu.fill("white")
    vindu.blit(overskrift_surface, (10, 10))
    vindu.blit(spiller_surface, spiller_rect)
    vindu.blit(fiende_surface, fiende_rect)
    vindu.blit(twitter_surface, twitter_rect)

 
    pygame.display.flip()
    klokke.tick(FPS)