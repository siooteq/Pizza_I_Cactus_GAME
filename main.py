#stage 1: game start
#stage 2: game rules
#stage 3: game in play
#stage 4: game is over

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
        self.x_cord = 330 #initial values of coordinates
        self.y_cord = 330
        self.image = pygame.transform.scale(pygame.image.load("pawl0.png"), (2*55, 2*74))  # wczytywanie grafiki
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 5 #prędkość
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self, keys):
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            if self.x_cord < r_x - self.width - 35:
                self.x_cord += self.speed
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            if self.x_cord > 0 + 35:
                self.x_cord -= self.speed
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]):
            if self.y_cord < r_y - self.height - 10:
                self.y_cord += self.speed
        if (keys[pygame.K_w] or keys[pygame.K_UP]):
            if self.y_cord > 0 + 40:
                self.y_cord -= self.speed

        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Pizza:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("pizza0.png"), (40, 40))  # wczytywanie grafiki
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = randint(40,r_x - self.width -40)
        self.y_cord = randint(40,r_y - self.height -40)
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


class Cactus:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("kaktus0.png"), (2 * 40, 2 * 63))  # wczytywanie grafiki
        self.x_cord = 40
        self.y_cord = 40
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))



###########################################################   Main   ##############################################


def main():
    stage = 4
    clock = 0
    pizzas = []
    cacti = []  #(more than one cactus)
    player = Player()
    score = 0
    run = True
    ###############################################   loading images   ###########################################
    rules = pygame.image.load("zasady.png")
    start = pygame.image.load("gamestart.png")
    road = pygame.image.load("droga.png")
    gameover = pygame.image.load("gameover.png")
    score_text = pygame.font.Font.render(pygame.font.SysFont("arial", 24), f"Wynik: {score}", True, (0, 0, 0))


    while run:
        clock += pygame.time.Clock().tick(60) / 1000 #max 60 fps (refreshing loop)
        #print(clock)
        keys = pygame.key.get_pressed()  # values from keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # stage 1: game start
        # stage 2: game rules
        # stage 3: game in play
        # stage 4: game is over

        if stage == 1: #game start
            window.blit(start, (0, 0))
            if keys[pygame.K_SPACE]:
                stage = 3
            elif keys[pygame.K_r]:
                stage = 2
        if stage == 2: #game rules
            window.blit(rules, (0, 0))
            if keys[pygame.K_SPACE]:
                stage = 3
            elif keys[pygame.K_ESCAPE]:
                stage = 1
###################################################   Animation   ##############################################
        if stage == 3: #game in play
            window.blit(road, (0, 0))  # road
            if clock >= 2:
                clock = 0
                pizzas.append(Pizza())
                cacti.append(Cactus())
            for pizza in pizzas:
                pizza.tick()
            for cactus in cacti:
                cactus.tick()
            for pizza in pizzas:
                if player.hitbox.colliderect(pizza.hitbox):
                    pizzas.remove(pizza)
                    score += 1
            player.tick(keys)
            player.draw()
            for pizza in pizzas:
                pizza.draw()
            for cactus in cacti:
                cactus.draw()
            for cactus in cacti:
                if player.hitbox.colliderect(cactus.hitbox):
                    #delay
                    stage = 4
                    cacti.remove(cactus)
            score_text = pygame.font.Font.render(pygame.font.SysFont("arial", 24), f"Wynik: {score}", True, (0, 0, 0))
            window.blit(score_text, (50, 5))

##############################################   End of Animation   ##############################################
        if stage == 4: #game is over
            window.blit(gameover, (0, 0))
            score_text = pygame.font.Font.render(pygame.font.SysFont("arial", 40), f"Twój wynik to: {score}", True, (105, 5, 22))
            window.blit(score_text, (124, 80))
            if keys[pygame.K_SPACE]:
                stage = 3

        pygame.display.update()

if __name__ == "__main__":
    main()
