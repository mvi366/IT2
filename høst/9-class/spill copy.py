import pygame, random

# klasser

class Matbit:
    def __init__(self):
        self.bilde = pygame.image.load("bilder/stemme.png").convert_alpha()
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = random.randint(0, BREDDE)
        self.ramme.centery = random.randint(0, HOYDE)
    def tegn(self,vindu):
        vindu.blit(self.bilde, self.ramme)

class Celle:
    def __init__(self, navn: str, radius: int, bildesti: str):
        self.navn = navn
        self.radius = radius
        self.bilde_orginal = pygame.image.load(bildesti).convert_alpha()
        self.bilde = pygame.transform.scale(self.bilde_original, (self.radius * 2, self.radius * 2))
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = x
        self.ramme.centery = y


    def beveg(self, mus_x: int, mus_y: int):
        self.ramme.centerx = mus_x
        self.ramme.centery = mus_y

        if mus_x > self.ramme.centerx:
            self.ramme.centerx += 1
        elif mus_x < self.ramme.centerx:
            self.ramme.centerx -= 1

        if mus_y > self.ramme.centery:
            self.ramme.centery += 1
        elif mus_y < self.ramme.centery:
            self.ramme.centery -= 1


    
    def spis(self):
        print("spis")
        self.radius += 1
        self.bilde = pygame.transform.scale(self.bilde_original, (self.radius * 2, self.radius *2))
        gammel_x = self.ramme.centerx
        gammel_y = self.ramme.centery
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = gammel_x
        self.ramme.centery = gammel_y


    def tegn(self, vindu):
        vindu.blit(self.bilde, self.ramme)




# 1 oppsett
pygame.init()
BREDDE = 600
HOYDE = 600
vindu = pygame.display.set_mode((BREDDE, HOYDE))
FPS = 60
klokke = pygame.time.Clock()

ap = Celle("AP", 50, "bilder/jonas.png", 100, 200)
sv = Celle("SV", 25, "bilder/kristi.png", 500, 400)


matbiter = []

for _ in range(10):
    matbiter.append(Matbit())

while True:
    # 2. håndterer spillet
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    mus_x, mus_y = pygame.mouse.get_pos()

    # 3. oppdater spikk
    ap.beveg(mus_x, mus_y)
   
    for i in range (len(matbiter)-1, -1, -1):
        if ap.ramme.colliderect(matbit[i].ramme):
            ap.spis()
            # slette matbiten

    # 4. tegn
    vindu.fill("white")
    ap.tegn(vindu)
    sv.tegn(vindu)

    for matbit in matbiter:
        matbit.tegn(vindu)
    pygame.display.flip()
    klokke.tick(FPS)