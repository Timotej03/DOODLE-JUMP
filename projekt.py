#DOODLE JUMP
import random
import pygame
from pygame import mixer
pygame.init()
mixer.init()

#konstanty
biela = (255, 255, 255)
cierna = (0, 0, 0)
siva = (128, 128, 128)
SIRKA = 400
VYSKA = 500
pozadie = biela
hrac = pygame.transform.scale(pygame.image.load('doodle-removebg-preview.png'), (60, 50))
fps = 60
cas = pygame.time.Clock()
skore = 0
najvyssie_skore = 0
posledne_skore = 0
koniec_hry = False

#FONT
font = pygame.font.Font('freesansbold.ttf', 16)

#HUDBA
mixer.music.load("Dream Speedrun Music.mp3")
mixer.music.play()
mixer.music.set_volume(0.7)

#premenné
hrac_x = 170
hrac_y = 400
ostrovceky = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]
skok = False
zmena_y = 0
zmena_x = 0
rychlost_hraca = 3
super_skok = 2
posledny_skok = 0

#obrazovka
obrazovka = pygame.display.set_mode([SIRKA, VYSKA])
pygame.display.set_caption('DOODLE JUMPER')

# kolízie
def kolizie(rect_list, j):
    global hrac_x
    global hrac_y
    global zmena_y
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([hrac_x + 20, hrac_y + 60, 45, 5]) and skok == False and zmena_y > 0:
            j = True
    return j

#pohyb hraca y
def pohyb_hraca(y_pos):
    global skok
    global zmena_y
    vyska_skoku = 10
    gravitacia = .4
    if skok:
        zmena_y = -vyska_skoku
        skok = False
    y_pos += zmena_y
    zmena_y += gravitacia
    return y_pos

#pohyb platforiem v priebehu hry
def aktualizovane_ostrovceky(moj_list, y_pos, zmena):
    global skore
    if y_pos < 250 and zmena < 0:
        for i in range(len(moj_list)):
            moj_list[i][1] -= zmena
    else:
        pass
    for item in range(len(moj_list)):
        if moj_list[item][1] > 500:
            moj_list[item] = [random.randint(10, 320), random.randint(-50, -10), 70, 10]
            skore += 1
    return moj_list

running = True
while running == True:
    cas.tick(fps)
    obrazovka.fill(pozadie)
    obrazovka.blit(hrac, (hrac_x, hrac_y))
    ostrovy = []
    skore_text = font.render('NAJVYŠŠIE SKÓRE:' + str(najvyssie_skore), True, cierna, pozadie)
    obrazovka.blit(skore_text, (280, 0))
    najvyssie_skore_text = font.render('SKÓRE: ' + str(skore), True, cierna, pozadie)
    obrazovka.blit(najvyssie_skore_text, (320, 20))

    skore_text = font.render('Super skoky (Medzerník): ' + str(super_skok), True, cierna, pozadie)
    obrazovka.blit(skore_text, (10, 10))
    if koniec_hry:
        koniec_hry_text = font.render('HRA SKONČILA STLAČ MEDZERNÍK PRE POKRAČOVANIE!', True, cierna, pozadie)
        obrazovka.blit(koniec_hry_text, (170, 80))


    for i in range(len(ostrovceky)):
        ostrov = pygame.draw.rect(obrazovka, cierna, ostrovceky[i], 0, 3)
        ostrovy.append(ostrov)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and koniec_hry:
                koniec_hry = False
                skore = 0
                hrac_x = 170
                hrac_y = 400
                pozadie = biela
                posledne_skore = 0
                super_skok = 2
                posledny_skok = 0
                ostrovceky = [[175, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10],
                              [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]
            if event.key == pygame.K_SPACE and not koniec_hry and super_skok > 0:
                super_skok -= 1
                zmena_y = -15
            if event.key == pygame.K_a:
                zmena_x = -rychlost_hraca
            if event.key == pygame.K_d:
                zmena_x = rychlost_hraca
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

    ostrovceky = aktualizovane_ostrovceky(ostrovceky, hrac_y, zmena_y)

    if hrac_x < -20:
        hrac_x = -20
    elif hrac_x > 330:
        hrac_x = 330

    if zmena_x > 0:
        hrac = pygame.transform.scale(pygame.image.load('doodle-removebg-preview.png'), (65, 70))
    elif zmena_x < 0:
        hrac = pygame.transform.flip(pygame.transform.scale(pygame.image.load('doodle-removebg-preview.png'), (65, 70)), 1, 0)

    if skore > najvyssie_skore:
        najvyssie_skore = skore

    if skore - posledne_skore > 20:
        posledne_skore = skore
        pozadie = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

    if skore - posledny_skok > 50:
        posledny_skok = skore
        super_skok += 1

    pygame.display.flip()
pygame.quit()