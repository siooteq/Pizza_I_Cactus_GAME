import pygame
from random import randint

import os
import sys

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

pygame.init()

r_x = 480
r_y = 640
rozdz = (r_x, r_y)
window = pygame.display.set_mode(rozdz)

import pygame
pygame.init()
class Player:
    def __init__(self):
        self.x_cord = 330 #wspolrzedna
        self.y_cord = 330
        self.image = pygame.transform.scale(pygame.image.load("pawl0.png"), (2*55, 2*74))  # wczytywanie grafiki
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 5 #prędkość
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self, keys):
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.x_cord < r_x - self.width - 35:
                self.x_cord += self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if self.x_cord > 0 + 35:
                self.x_cord -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if self.y_cord < r_y - self.height - 10:
                self.y_cord += self.speed
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.y_cord > 0 + 40:
                self.y_cord -= self.speed

        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Cash:
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


def animacja():
    pass

def main():

    dotyk = False
    clock = 0
    monety = []
    kaktusy = []
    punkty = 0
    run = True
    first_start = False
    restart_gry = False
    wynik = 0

    tekst = pygame.font.Font.render(pygame.font.SysFont("arial", 24), f"Wynik: {punkty}", True, (0, 0, 0))
    nowa_gra = pygame.font.Font.render(pygame.font.SysFont("arial", 24), "Naciśnij spację aby uruchomić nową grę", True, (0, 0, 0))
    start = pygame.image.load("gamestart.png")
    tlo = pygame.image.load("tlo.jpg")
    droga = pygame.image.load("droga.png")
    koniec = pygame.image.load("gameover.png")

    player = Player()
   

    while run:
        clock += pygame.time.Clock().tick(60) / 1000 #maksymalnie 60 fps (odswiezanie pętli)
        #print(clock)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        window.blit(start, (0, 0))
        if keys[pygame.K_SPACE]:
            first_start = True
        if first_start == True or restart_gry == True :
            restart_gry = False

            ################ TUTAJ JEST POCZĄTEK ANIMACJI
            if clock >= 2:
                clock = 0
                monety.append(Cash())
                kaktusy.append(Cactus())
            for moneta in monety:
                moneta.tick()
            for kaktus in kaktusy:
                kaktus.tick()


            for moneta in monety:
                if player.hitbox.colliderect(moneta.hitbox):
                    monety.remove(moneta)
                    punkty += 1
                    tekst = pygame.font.Font.render(pygame.font.SysFont("arial", 24), f"Wynik: {punkty}", True, (0, 0, 0))

            # for kaktus in kaktusy:
            #     if player.hitbox.colliderect(kaktus.hitbox):
            #         wynik = punkty
            #         dotyk = True
            #         window.blit(koniec, (0, 0))
            #         window.blit(pygame.font.Font.render(pygame.font.SysFont("arial", 32), f"Twój wynik to: {wynik}", True,
            #                                     (130, 52, 40)), (140, 60))


            #window.fill((255, 255, 255))
            window.blit(droga, (0, 0)) #tlo
            window.blit(tekst, (50, 5))

            player.tick(keys)
            player.draw()


            for moneta in monety:
                moneta.draw()
            for kaktus in kaktusy:
                kaktus.draw()

            for kaktus in kaktusy:
                if player.hitbox.colliderect(kaktus.hitbox):

                    wynik = punkty
                    window.blit(koniec, (0, 0))
                    window.blit(pygame.font.Font.render(pygame.font.SysFont("arial", 32), f"Twój wynik to: {wynik}", True,
                                                         (130, 52, 40)), (140, 60))

                    if keys[pygame.K_SPACE]:
                        kaktusy.remove(kaktus)
                        restart_gry = True
                        punkty = 0
                        tekst = pygame.font.Font.render(pygame.font.SysFont("arial", 24), f"Wynik: {punkty}", True,
                                                        (0, 0, 0))


        pygame.display.update()

    print(dotyk)

if __name__ == "__main__":
    main()





# class Koniec:
#     def __init__(self):
#         self.image = pygame.image.load("gameover.png")  # wczytywanie grafiki
#         self.x_cord = 0
#         self.y_cord = 0
#         self.width = self.image.get_width()
#         self.height = self.image.get_height()
#
#
#
#     def tick(self):
#         self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
#
#     def draw(self):
#         window.blit(self.image, (self.x_cord, self.y_cord))
#
# class Start:
#     def __init__(self):
#         self.image = pygame.image.load("droga.png")  # wczytywanie grafiki
#         self.imageP = pygame.image.load("pizza0.png")  # wczytywanie grafiki
#         self.imageC = pygame.image.load("kaktus0.png")  # wczytywanie grafiki
#         self.tekst1 = pygame.font.Font.render(pygame.font.SysFont("arial", 24), "Pizza & Cactus GAME", True, (0, 0, 0))
#         self.tekst2 = pygame.font.Font.render(pygame.font.SysFont("arial", 24), "Naciśnij spację, aby rozpocząć", True, (0, 0, 0))
#         self.x_cord = 0
#         self.y_cord = 0
#         self.width = self.image.get_width()
#         self.height = self.image.get_height()
#
#
#
#     def tick(self):
#         self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
#
#     def draw(self):
#         window.blit(self.image, (self.x_cord, self.y_cord))
