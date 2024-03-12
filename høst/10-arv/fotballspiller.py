from figur import Figur
import pygame

class Fotballspiller(Figur):
    def __init__(self, vindu_bredde: int, vindu_høyde: int) -> None:
        super().__init__("bilder/haaland.png")
        self.poeng = 0
        self.bilde = pygame.transform.scale(self.bilde, (200, 200))
        self.ramme = self.bilde.get_rect()
        self.liv = 10

        self.ramme.centerx = vindu_bredde / 2
        self.ramme.bottom = vindu_høyde