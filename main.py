#DOODLE JUMP
import pygame
pygame.init()

#konstanty
biela = (255, 255, 255)
cierna = (0, 0, 0)
siva = (128, 128, 128)
SIRKA = 400
VYSKA = 500
pozadie = biela
hrac = pygame.transform.scale(pygame.image.load('doodle.png'), (60, 50))
fps = 60

#FONT
############
cas = pygame.time.Clock()
#premenné
hrac_x = 170
hrac_y = 400
ostrovceky = [[165, 480, 70, 10 ]]

#obrazovka
obrazovka = pygame.display.set_mode([SIRKA, VYSKA])
pygame.display.set_caption('DOODLE JUMPER')

running = True
while running == True:
    cas.tick(fps)
    obrazovka.fill(pozadie)
    obrazovka.blit(hrac, (hrac_x, hrac_y))
    ostrovy = []
    for i in range(len(ostrovceky )):
        ostrov = pygame.draw.rect(obrazovka, cierna, ostrovceky[i])
        ostrovy.append(ostrovy)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:



           running = False
    pygame.display.flip()
pygame.quit()

