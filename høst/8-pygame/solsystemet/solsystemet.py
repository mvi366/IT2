import pygame
from planet import Planet
class Planet:
    def __init__(self, x, y, r, bilde):
        self.x = x
        self.y = y
        self.r = r
        self.surface = pygame.image.load(bilde)
        self.surface = pygame.transform.scale(self.surface, (2 * self.r, 2* self.r))
        # self.surface = pygame.image.load("bilder/"+ bilde +)
    def tegn(self, vindu):
        vindu.blit(self.surface, (self.x, self.y))
        # pygame.draw.circle(vindu, "red", (self.x, self.y), self.r)

# 1. oppsett

pygame.init()
BREDDE = 1000
HOYDE = 400
vindu = pygame.display.set_mode((BREDDE, HOYDE))
FPS = 60
klokke = pygame.time.Clock()


planeter = [
    Planet( -600, -200, 400, "bilder/sun.png"),
    Planet(100, 200, 50, "bilder/earth.png"),
    Planet(250, 200, 80, "bilder/jupiter.png") ,
    Planet(400, 200, 70, "bilder/saturn.png") ,
    Planet( 600, 200, 64, "bilder/uranus.png"),
    Planet(700, 200, 50, "bilder/mars.png") ,
    Planet(800, 200, 70, "bilder/neptune.png") ,
    Planet( 900, 200, 94, "bilder/venus.png")

]

#jorda = Planet(100, 200, 50, "bilder/earth.png") # oppretter et objekt av klassen planet
#jupiter = Planet(250, 200, 60, "bilder/jupiter.png") # oppretter et objekt av klassen planet
#saturn = Planet(400, 200, 70, "bilder/saturn.png") 
#uranus = Planet( 600, 200, 64, "bilder/uranus.png")
while True:
    # 2. håndterer input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    # 3. oppdater spikk
    # 4. tegn
    for p in planeter:
        p.tegn(vindu)
    # pygame.draw.circle(vindu, "red", (jorda.x, jorda.y), jorda.r)
    # pygame.draw.circle(vindu, "red", (jupiter.x, jupiter.y), jupiter.r)



    pygame.display.flip()
    klokke.tick(FPS)
