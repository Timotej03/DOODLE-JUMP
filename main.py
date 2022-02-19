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
#############################################

cas = pygame.time.Clock()

#premenné
hrac_x = 170
hrac_y = 400
ostrovceky = [[165, 480, 70, 10],[85, 370, 70,10],[265, 370, 70, 10], [165, 250, 70, 10],[85, 180, 70,10],[265, 370, 70, 10], [265, 40, 70, 10]]
skok = False
zmena_y = 0

#obrazovka
obrazovka = pygame.display.set_mode([SIRKA, VYSKA])
pygame.display.set_caption('DOODLE JUMPER')

# kolízie
def kolizie(rect_list, j):
    global hrac_x
    global hrac_y
    global zmena_y
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([hrac_x, hrac_y + 60, 90, 6])and skok == False and zmena_y >0:
            skok = True
    return j


#pohyb hraca y
def pohyb_hraca(y_poz):
    global skok
    global zmena_y
    vyska_skoku = 10
    gravitacia = .4
    if skok:
        zmena_y = -vyska_skoku
        skok = False
    y_poz += zmena_y
    zmena_y += gravitacia
    return y_poz

running = True
while running == True:
    cas.tick(fps)
    obrazovka.fill(pozadie)
    obrazovka.blit(hrac, (hrac_x, hrac_y))
    ostrovy = []

    for i in range(len(ostrovceky)):
        ostrov = pygame.draw.rect(obrazovka, cierna, ostrovceky[i], 0, 4)
        ostrovy.append(ostrovy)

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
    skok = kolizie(ostrovy, skok)
    hrac_y = pohyb_hraca(hrac_y)



    pygame.display.flip()
pygame.quit()

