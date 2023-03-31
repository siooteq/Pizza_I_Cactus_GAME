#stage 1: game start
#stage 2: game rules
#stage 3: game in play
#stage 4: game is over
#stage 5: choose player Men
#stage 6: choose player Woman

import time
import pygame
from random import randint
pygame.init()
############################Resolution#####################################
r_x = 480
r_y = 640
resolution = (r_x, r_y)
window = pygame.display.set_mode(resolution)
###########################################################################

class Player:
    def __init__(self):

        self.image = pygame.transform.scale(pygame.image.load("pawl0.png"), (82, 111))  # wczytywanie grafiki
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5 #prędkość
        self.hitbox = self.mask.get_rect()
        #self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.x_cord = 190  # initial values of coordinates
        self.y_cord = 40
        self.hitbox.x = self.x_cord
        self.hitbox.y = self.y_cord

    def tick(self, keys):
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            if self.x_cord < r_x - self.width - 35:
                self.x_cord += self.speed
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            if self.x_cord > 0 + 35:
                self.x_cord -= self.speed
        # if (keys[pygame.K_s] or keys[pygame.K_DOWN]):
        #     if self.y_cord < r_y - self.height - 10:
        #         self.y_cord += self.speed
        # if (keys[pygame.K_w] or keys[pygame.K_UP]):
        #     if self.y_cord > 0 + 40:
        #         self.y_cord -= self.speed

        #self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.hitbox = self.mask.get_rect()
        self.hitbox.x = self.x_cord
        self.hitbox.y = self.y_cord

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


# def losowe_liczby():
#     liczba1 = randint(0, 2)*150 + 60
#     liczba2 = randint(0, 2)*150 + 60
#     liczba3 = randint(0, 2)*150 + 60
#     wystapienie = randint(0, 1)
#     while liczba3 == liczba1:
#         liczba3 = randint(0, 2)*150 + 60
#     while liczba2 == liczba1:
#         liczba2 = randint(0, 2)*150 + 60
#     if wystapienie == 1:
#         liczba2 = 600
#     return liczba1, liczba2, liczba3

def losowe_liczby():
    liczba1 = randint(0, 2) * 150 + 60
    liczba2 = randint(0, 2) * 150 + 60
    liczba3 = randint(0, 2) * 150 + 60

    # Zapobiegamy sytuacji, w której wylosowane liczby są sobie równe
    while liczba2 == liczba1:
        liczba2 = randint(0, 2) * 150 + 60
    while liczba3 == liczba2 or liczba3 == liczba1:
        liczba3 = randint(0, 2) * 150 + 60

    # Zmieniamy wartość liczby 2 z prawdopodobieństwem 50%
    if randint(0, 3) == 1:
        liczba2 = 600

    return liczba1, liczba2, liczba3

class Pizza:
    def __init__(self, x_c):
        if x_c >= 0:
            self.x_cord = x_c
        else:
            self.x_cord = 0
        self.image = pygame.transform.scale(pygame.image.load("pizza0.png"), (60, 60))  # wczytywanie grafiki
        self.mask = pygame.mask.from_surface(self.image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.y_cord = 650
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Cactus:
    def __init__(self, x_c):
        if x_c >=0:
            self.x_cord = x_c
        else:
            self.x_cord = 0
        self.image = pygame.transform.scale(pygame.image.load("kaktus0.png"), (60, 90))  # wczytywanie grafiki
        self.mask = pygame.mask.from_surface(self.image)
        self.y_cord = 650
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

###########################################################   Main   ##############################################

def main():
    flag = False
    flag2 = False
    stage = 1
    clock = 0
    pizzas = []
    cacti = []  #(more than one cactus)
    cacti_lu = [] #additional cacti for level up
    player = Player()
    playera = Player()
    playera.image = pygame.transform.scale(pygame.image.load("paula0.png"), (82, 111))  # wczytywanie grafiki
    score = 0
    run = True
    sex = 0
    level = 2
    level2 = 4
    timer = 1.5
    licznik = 0
    x_cactus1 = 0
    x_cactus2 = 0
    x_pizza = 0
    ###############################################   loading images   ###########################################
    choose = pygame.image.load("choose.png")
    rules = pygame.image.load("zasady.png")
    start = pygame.image.load("gamestart.png")
    road = pygame.image.load("droga.png")
    gameover = pygame.image.load("gameover.png")
    score_text = pygame.font.Font.render(pygame.font.SysFont("arial", 24), f"Wynik: {score}", True, (0, 0, 0))
    level_up = pygame.font.Font.render(pygame.font.SysFont("arial", 96), "LEVEL UP!", True, (0, 0, 0))


    while run:
        clock += pygame.time.Clock().tick(120) / 1000 #max 60 fps (refreshing loop)
        #print(clock)
        keys = pygame.key.get_pressed()  # values from keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if stage == 1: #game start
            if not (keys[pygame.K_SPACE]):
                flag = True
            window.blit(start, (0, 0))
            if keys[pygame.K_SPACE] and flag == True:
                stage = 5
                flag = False
            if keys[pygame.K_r]:
                stage = 2
        #time.sleep(1)
        if stage == 2: #game rules
            if not (keys[pygame.K_SPACE]):
                flag = True
            window.blit(rules, (0, 0))
            if keys[pygame.K_SPACE] and flag == True:
                stage = 5
                flag = False
            elif keys[pygame.K_ESCAPE]:
                stage = 1
###################################################   Animation   ##############################################
        if stage == 3: #game in play
            if sex == 1:
                player.image = pygame.transform.scale(pygame.image.load("pawl0.png"), (82, 111))  # wczytywanie grafiki
            elif sex == 2:
                player.image = pygame.transform.scale(pygame.image.load("paula0.png"), (82, 111))  # wczytywanie grafiki
            window.blit(road, (0, 0))  # road

            if clock >= timer:
                clock = 0
                x_cactus1, x_cactus2, x_pizza = losowe_liczby()
                pizzas.append(Pizza(x_pizza))
                cacti.append(Cactus(x_cactus1))
                if score >= level2:
                    cacti_lu.append(Cactus(x_cactus2))
            for pizza in pizzas:
                pizza.tick()
                pizza.y_cord += -level
            for cactus in cacti:
                cactus.tick()
                cactus.y_cord += -level
            for cactus_lu in cacti_lu:
                cactus_lu.tick()
                cactus_lu.y_cord += -level
            for pizza in pizzas:
                if player.hitbox.colliderect(pizza.hitbox):
                    if player.mask.overlap(pizza.mask, (pizza.x_cord - player.x_cord, pizza.y_cord - player.y_cord)):
                        pizzas.remove(pizza)
                        score += 1
            player.tick(keys)
            player.draw()
            for pizza in pizzas:
                pizza.draw()
            for cactus in cacti:
                cactus.draw()
            if score >= level2:
                for cactus_lu in cacti_lu:
                    cactus_lu.draw()

            for cactus in cacti:
                if player.hitbox.colliderect(cactus.hitbox):
                    if player.mask.overlap(cactus.mask, (cactus.x_cord - player.x_cord, cactus.y_cord - player.y_cord)):
                        time.sleep(0.5) #delay 0.5s
                        stage = 4
                        player.x_cord = 190 # new coordinates for new game
                        player.y_cord = 40
                        cacti.remove(cactus)

            if score >= level2:
                for cactus_lu in cacti_lu:
                    if player.hitbox.colliderect(cactus_lu.hitbox):
                        if player.mask.overlap(cactus_lu.mask, (cactus_lu.x_cord - player.x_cord, cactus_lu.y_cord - player.y_cord)):
                            time.sleep(0.5) #delay 0.5s
                            stage = 4
                            player.x_cord = 190 # new coordinates for new game
                            player.y_cord = 40
                            cacti_lu.remove(cactus_lu)
            score_text = pygame.font.Font.render(pygame.font.SysFont("arial", 24), f"Wynik: {score}", True, (255, 0, 0))
            rect = pygame.Rect(0, 0, 480, 38)
            pygame.draw.rect(window, (0, 0, 0), rect)
            window.blit(score_text, (50, 5))
            if score == 2:
                window.blit(level_up, (43, 270))
                level = 4
                timer = 1
            if score == level2:
                window.blit(level_up, (43, 270))


##############################################   End of Animation   ##############################################
        if stage == 4: #game is over
            cacti.clear()
            pizzas.clear()
            window.blit(gameover, (0, 0))
            score_text = pygame.font.Font.render(pygame.font.SysFont("arial", 40), f"Twój wynik to: {score}", True, (105, 5, 22))
            window.blit(score_text, (124, 80))
            if keys[pygame.K_SPACE]:
                    stage = 3
                    score = 0
        if stage == 5: #choose Men
            if not (keys[pygame.K_SPACE]):
                flag = True
            if not (keys[pygame.K_d] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_a]):
                flag2 = True

            window.blit(choose, (0, 0))
            player.x_cord = 200
            player.y_cord = 320
            player.draw()
            if ((keys[pygame.K_d] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_a]) and flag2 == True):
                stage = 6
                flag2 = False
            elif keys[pygame.K_SPACE] and flag == True:
                stage = 3
                flag = False
                player.x_cord = 190
                player.y_cord = 40
                sex = 1

        if stage == 6: #choose Woman
            if not (keys[pygame.K_SPACE]):
                flag = True
            if not (keys[pygame.K_d] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_a]):
                flag2 = True

            window.blit(choose, (0,0))
            playera.x_cord = 200
            playera.y_cord = 320
            playera.draw()
            if ((keys[pygame.K_d] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_a]) and flag2 == True):
                stage = 5
                flag2 = False
            elif (keys[pygame.K_SPACE]) and flag == True:
                stage = 3
                flag = False
                playera.x_cord = 190
                playera.y_cord = 40
                sex = 2

        pygame.display.update()

if __name__ == "__main__":
    main()
