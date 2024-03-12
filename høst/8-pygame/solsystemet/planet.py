import pygame


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
