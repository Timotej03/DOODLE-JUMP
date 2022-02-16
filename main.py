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
obrazok = pygame.image.load('doodle.png')
fps = 60

#FONT


cas = pygame.time.Clock()

#obrazovka
obrazovka = pygame.display.set_mode([SIRKA, VYSKA])
pygame.display.set_caption('DOODLE JUMPER')

running = True
while running == True:
    cas.tick(fps)
    obrazovka.fill(pozadie)
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
    pygame.display.flip()
pygame.quit()

