#stage 1: game start
#stage 2: game rules
#stage 3: game in play
#stage 4: game is over
#stage 5: choose player Men
#stage 6: choose player Woman
#stage 7: enter a nickname
#stage 8: Leaderboard

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
        self.speed = 8 #prędkość
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


def position():
    pos1 = randint(0, 2) * 150 + 60
    pos2 = randint(0, 2) * 150 + 60
    pos3 = randint(0, 2) * 150 + 60

    # Zapobiegamy sytuacji, w której wylosowane liczby są sobie równe
    while pos2 == pos1:
        pos2 = randint(0, 2) * 150 + 60
    while pos3 == pos2 or pos3 == pos1:
        pos3 = randint(0, 2) * 150 + 60

    # Zmieniamy wartość liczby 2 z prawdopodobieństwem 10%
    if randint(0, 9) == 1:
        pos2 = 600

    return pos1, pos2, pos3

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

class TextInput:
    def __init__(self, x, y, width, height, maxlength = -1, empty=""):
        self.x_cord = x
        self.y_cord = y
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont("bookmanoldstyle", 26)
        self.text = ""
        self.empty = empty
        self.empty_image = pygame.font.Font.render(self.font, self.empty, True, (90, 90, 90))
        self.maxlength = maxlength
        self.confirm = 1


    def tick(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.confirm == 1:
                    if event.key == pygame.K_RETURN:
                        self.confirm = 2
                        return self.text

                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1] #delete last sign
                    elif len(self.text) < self.maxlength or self.maxlength == -1: #if -1 there is no limit
                        if event.unicode.isprintable():
                            self.text += event.unicode


    def draw(self, window):
        if self.confirm == 1:
            pygame.draw.rect(window, (148, 30, 32), (self.x_cord-4, self.y_cord-4, self.width+8, self.height+8), border_radius=10)
            pygame.draw.rect(window, (255, 255, 255), (self.x_cord, self.y_cord, self.width, self.height), border_radius=10)
            if self.text:
                font_image = pygame.font.Font.render(self.font, self.text, True, (0,0,0))
                window.blit(font_image, (self.x_cord + 5, self.y_cord + 5))
            else:
                window.blit(self.empty_image, (self.x_cord + 5, self.y_cord + 5))
        if self.confirm == 2:
            pygame.draw.rect(window, (148, 30, 32), (self.x_cord - 4, self.y_cord - 4, self.width + 8, self.height + 8),
                             border_radius=10)
            pygame.draw.rect(window, (255, 255, 255), (self.x_cord, self.y_cord, self.width, self.height),
                             border_radius=10)
            font_image = pygame.font.Font.render(self.font, self.text, True, (0, 255, 100))
            window.blit(font_image, (self.x_cord + 5, self.y_cord + 5))

###########################################################   Main   ##############################################

def main():
    leader = []
    sorted_leader = []
    eh = 1
    file = open("scoreboard.txt", "a+")
    flag_score = True
    user_nick = ""
    flag = False
    flag2 = False
    flag_nick = False
    flag_enter = False
    flag_back_from_leader_to_gameover = False
    stage = 1
    clock = 0
    pizzas = []
    cacti = []  #(more than one cactus)
    cacti_lu = [] #additional cacti for level up
    player = Player()
    playera = Player()
    playera.image = pygame.transform.scale(pygame.image.load("paula0.png"), (82, 111))  # wczytywanie grafiki
    textinput = TextInput(100, 295, 280, 40, maxlength=8, empty="        Podaj nick")
    score = 0
    score_info = ()
    score_leaderboard = []
    run = True
    sex = 0

    timer = 1.4
    level = 3
    game_level1 = 5
    game_level2 = 10
    game_level3 = 15
    game_level4 = 20
    game_level5 = 25
    game_level6 = 30
    game_level7 = 35
    game_level8 = 40
    game_level9 = 45
    game_level10 = 50
    awesome = pygame.font.Font.render(pygame.font.SysFont("arial", 88), "AWESOME!", True, (255, 0, 0))

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
    nick_bg = pygame.image.load("nick.png")
    leaderboard = pygame.image.load("leaderboard.png")


    while run:
        clock += pygame.time.Clock().tick(120) / 1000 #max 60 fps (refreshing loop)
        #print(clock)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            #     pause = not pause
        keys = pygame.key.get_pressed()  # values from keyboard

        if stage == 1: #game start
            if (keys[pygame.K_SPACE]):
                flag = True
            window.blit(start, (0, 0))
            if not keys[pygame.K_SPACE] and flag == True:
                stage = 7
                flag = False
            if keys[pygame.K_r]:
                stage = 2
        #time.sleep(1)
        elif stage == 2: #game rules
            if not (keys[pygame.K_SPACE]):
                flag = True
            window.blit(rules, (0, 0))
            if keys[pygame.K_SPACE] and flag == True:
                stage = 7
                flag = False
            elif keys[pygame.K_ESCAPE]:
                stage = 1
                flag = False
###################################################   Animation   ##############################################
        elif stage == 3: #game in play
            flag_back_from_leader_to_gameover = False
            if sex == 1:
                player.image = pygame.transform.scale(pygame.image.load("pawl0.png"), (82, 111))  # wczytywanie grafiki
            elif sex == 2:
                player.image = pygame.transform.scale(pygame.image.load("paula0.png"), (82, 111))  # wczytywanie grafiki
            window.blit(road, (0, 0))  # roadff

            if clock >= timer:
                
                clock = 0
                x_cactus1, x_cactus2, x_pizza = position()
                pizzas.append(Pizza(x_pizza))
                cacti.append(Cactus(x_cactus1))
                if score >= game_level2:
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
            if score >= game_level2:
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

            if score >= game_level2:
                for cactus_lu in cacti_lu:
                    if player.hitbox.colliderect(cactus_lu.hitbox):
                        if player.mask.overlap(cactus_lu.mask, (cactus_lu.x_cord - player.x_cord, cactus_lu.y_cord - player.y_cord)):
                            time.sleep(0.5) #delay 0.5s
                            stage = 4
                            player.x_cord = 190 # new coordinates for new game
                            player.y_cord = 40
                            cacti_lu.remove(cactus_lu)
            score_text = pygame.font.Font.render(pygame.font.SysFont("arial", 24), f"Wynik: {score}", True, (255, 0, 0))
            nick_text = pygame.font.Font.render(pygame.font.SysFont("arial", 24), f"Nick: {user_nick}", True, (255, 0, 0))
            rect = pygame.Rect(0, 0, 480, 38)
            pygame.draw.rect(window, (0, 0, 0), rect)
            window.blit(score_text, (50, 5))
            window.blit(nick_text, (300, 5))
####################################################### game levels #######################################################
            if score == game_level1:
                window.blit(level_up, (43, 270))
                level = 4
                timer = 1
            if score == game_level2:
                window.blit(level_up, (43, 270))
            if score == game_level3:
                window.blit(level_up, (43, 270))
                level = 5
                timer = 0.85
            if score == game_level4:
                window.blit(level_up, (43, 270))
                level = 6
                timer = 0.8
            if score == game_level5:
                window.blit(level_up, (43, 270))
                level = 7
                timer = 0.72
            if score == game_level6:
                window.blit(level_up, (43, 270))
                level = 8
                timer = 0.63
            if score == game_level7:
                window.blit(level_up, (43, 270))
                level = 9
                timer = 0.56
            if score == game_level8:
                window.blit(level_up, (43, 270))
                level = 10
                timer = 0.5
            if score == game_level9:
                window.blit(level_up, (43, 270))
                level = 11
                timer = 0.45
            if score == game_level10:
                window.blit(awesome, (43, 270))
                level = 11
                timer = 0.45
################################################ End of game levels ##############################################
##############################################   End of animation   ##############################################
        elif stage == 4: #game is over

            cacti.clear()
            pizzas.clear()
            window.blit(gameover, (0, 0))
            score_text = pygame.font.Font.render(pygame.font.SysFont("arial", 40), f"Twój wynik to: {score}", True, (105, 5, 22))
            window.blit(score_text, (124, 80))
            if flag_score == True and flag_back_from_leader_to_gameover == False:
                file.write(str(score) + " " + user_nick + "\n")
                flag_score = False
                file.close()
            score_leaderboard = []
            file = open("scoreboard.txt", "r")
            for line in file.readlines():
                line1 = line.split()[0]
                line2 = line.split()[1]
                score_info = (int(line1), line2)
                score_leaderboard.append(score_info)
            sorted_leader = sorted(score_leaderboard, key=lambda x: x[0], reverse=True)

            # delete users who score is over top 10
            for i in range(len(sorted_leader) - 1, -1, -1):
                if i > 9:
                    del sorted_leader[i]

            file.close()
            file = open("scoreboard.txt", "a+")
            if eh == 1:
                print(sorted_leader)
                print(sorted_leader[3])
                print(sorted_leader[3][0])
                print(sorted_leader[3][1])
                eh = 2
            if keys[pygame.K_SPACE]:
                stage = 3
                flag_score = True
                score = 0
                timer = 1.4
                level = 3
            if keys[pygame.K_l]:
                stage = 8
                flag_score = True

                timer = 1.4
                level = 3

        elif stage == 8: #leaderboard
            if not (keys[pygame.K_SPACE]):
                flag = True
                window.blit(leaderboard, (0, 0))
                pygame.draw.rect(window, (255, 255, 255), (50, 180, 380, 295), border_radius=10)
            for iter in range(10):
                leader_storage_score = pygame.font.Font.render(pygame.font.SysFont("arial", 24),
                                                    f"{iter+1}. Gracz: {sorted_leader[iter][1]}", True, (0, 0, 0))
                leader_storage_nick = pygame.font.Font.render(pygame.font.SysFont("arial", 24),
                                                    f"Wynik: {str(sorted_leader[iter][0])}", True, (0, 0, 0))

                window.blit(leader_storage_score, (70, 200 + 25 * iter))
                window.blit(leader_storage_nick, (320, 200 + 25 * iter))


            if keys[pygame.K_SPACE] and flag == True:
                stage = 3
                score = 0
                flag = False
            elif keys[pygame.K_ESCAPE]:
                stage = 4
                flag = False
                flag_back_from_leader_to_gameover = True
        elif stage == 5: #choose Men
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

        elif stage == 6: #choose Woman
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
                player.x_cord = 190
                player.y_cord = 40
                sex = 2

        elif stage == 7: #enter a nickname

            content = textinput.tick(events)
            if content is not None:
                #print(f"user podał: {content}")
                user_nick = content
            #user_nick = user_nick.replace(" ", "")
            user_nick = user_nick.strip()
            user_nick = user_nick.replace(" ", "_")
            if user_nick == "":
                user_nick = "player"

            if not (keys[pygame.K_SPACE]):
                flag_nick = True
                window.blit(nick_bg, (0, 0))
            if keys[pygame.K_RETURN]:
                flag_enter = True
            if keys[pygame.K_SPACE] and flag_nick == True and flag_enter == True:
                stage = 5
                flag_nick = False


            textinput.draw(window)

        pygame.display.update()

    file.close()


    #print(sorted_leader)
if __name__ == "__main__":
    main()