import pygame

class Figur:
    def __init__(self, bildesti: str, x: int, y: int) -> None:
        self.bilde = pygame.image.load(bildesti)
        self.ramme = self.bilde.get_rect()
        self.ramme.x = x
        self.ramme.y = y


    def tegn(self, vindu):
        vindu.blit(self.bilde, self.ramme)