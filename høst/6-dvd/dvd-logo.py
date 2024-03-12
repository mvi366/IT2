import pygame
import random
def tilfeldig_farge():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return [r, g, b]


# 1. oppsett (init)
pygame.init() #starter opp pygame
BREDDE = 1200
HOYDE = 600
vindu = pygame.display.set_mode([BREDDE, HOYDE])

klokke = pygame.time.Clock() # oppretter en klokke, denne skal brukes for å begrense spillet til 60fps

x = 20
y = 20
x_fart = 1
y_fart = 1
radius = 50
farge = tilfeldig_farge() # eks [100, 150, 200]
spiller = True
while spiller: #gameloop
    # 2. håndtere input/hendelser
    hendelser = pygame.event.get() # lager en liste med alle hendelsene
    for hendelse in hendelser:
        if hendelse.type == pygame.QUIT:
            spiller = False
    if hendelser:
        print(hendelser)
    # 3. oppdater spill
    x += x_fart
    y += y_fart
    if x > BREDDE or x < 0:
        # treffer vegg på høyre side
        x_fart = x_fart *-1
        farge = tilfeldig_farge()


    if y > HOYDE or y < 0:
        # treffer vegg på brunnen
        y_fart = y_fart *-1
        farge = tilfeldig_farge()

    # 4. tegn (render)
    vindu.fill([0, 0, 0])
    pygame.draw.circle(vindu, farge, [x, y], radius)
    pygame.draw.circle(vindu, [255, 255, 255], [50, 75], 10)
    pygame.draw.circle(vindu, [255, 255, 255], [75, 25], 10)

    klokke.tick(60)
    
    pygame.display.update()
  


