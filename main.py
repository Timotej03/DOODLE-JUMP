#DOODLE JUMP
import random
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
cas = pygame.time.Clock()
skore = 0
najvyssie_skore = 0
koniec_hry = False


#FONT
font = pygame.font.Font('freesansbold.ttf', 16)



#premenné
hrac_x = 170
hrac_y = 400
ostrovceky = [[165, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [165, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [265, 40, 70, 10]]
skok = False
zmena_y = 0
zmena_x = 0
rychlost_hraca = 3

#obrazovka
obrazovka = pygame.display.set_mode([SIRKA, VYSKA])
pygame.display.set_caption('DOODLE JUMPER')

# kolízie
def kolizie(rect_list, j):
    global hrac_x
    global hrac_y
    global zmena_y
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([hrac_x + 20, hrac_y + 60, 35, 6]) and skok == False and zmena_y > 0:
            j = True
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

#pohyb platforirm v priebehu hry
def aktualizovane_ostrovceky(moj_list, y_poz, x_poz, zmena):
    global skore
    if y_poz < 250 and zmena_y < 0:
        for i in range(len(moj_list)):
            moj_list[i][1] -= zmena
        else:
            pass
        for item in range(len(moj_list)):
            if moj_list[item][i] > 500:
                moj_list[item] = [random.randint(0, 330), random.randint(-50, -10), 70, 10]
                skore += 1
        return moj_list



running = True
while running == True:
    cas.tick(fps)
    obrazovka.fill(pozadie)
    obrazovka.blit(hrac, (hrac_x, hrac_y))
    ostrovy = []
    skore_text = font.render('NAJVYŠŠIE SKÓRE: ' + str(najvyssie_skore), True, cierna, pozadie)
    obrazovka.blit(skore_text, (320, 20))
    najvyssie_skore_text = font.render('SKÓRE: ' + str(skore), True, cierna, pozadie)
    obrazovka.blit(najvyssie_skore_text, (280, 0))


    for i in range(len(ostrovceky)):
        ostrov = pygame.draw.rect(obrazovka, cierna, ostrovceky[i], 0, 4)
        ostrovy.append(ostrovy)

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE and koniec_hry:
               koniec_hry = False
               skore = 0
               hrac_y = 400
               hrac_x = 170
               pozadie = biela
               ostrovceky = [[165, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [165, 260, 70, 10],
                             [85, 150, 70, 10], [265, 150, 70, 10], [265, 40, 70, 10]]
           if event.key == pygame.K_a:
               zmena_x = - rychlost_hraca
           if event.key == pygame.K_d:
               zmena_x = - rychlost_hraca
       if event.type == pygame.KEYUP:
           if event.key == pygame.K_a:
               zmena_x = 0
           if event.key == pygame.K_d:
               zmena_x = 0

    skok = kolizie(ostrovy, skok)
    hrac_x += zmena_x

    if hrac_y < 440:
        hrac_y = pohyb_hraca(hrac_y)
    else:
        koniec_hry = True
        zmena_y = 0
        zmena_x = 0



    ostrovceky = aktualizovane_ostrovceky(ostrovceky, hrac_x, hrac_y)

    if hrac_x < -20:
        hrac_x = -20
    elif hrac_x > 330:
        hrac_x = 330

    if zmena_x > 0:
        hrac = pygame.transform.scale(pygame.image.load('doodle.png'), (60, 50))
    elif zmena_x < 0:
        hrac = pygame.transform.flip(pygame.transform.scale(pygame.image.load('doodle.png'), (60, 50)), 1, 0)

    if skore > najvyssie_skore:
        najvyssie_skore = skore

    pygame.display.flip()
pygame.quit()

