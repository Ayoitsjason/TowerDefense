import pygame
import os
import time
from enemies.scorpion import Scorpion


class Game:
    # initialize game
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = [Scorpion()]
        self.towers = []
        self.lives = 10
        self.money = 100
        print(os.getcwd())
        print(os.path.join("game_assets", "bg.png"))
        print(os.listdir())
        self.bg = pygame.image.load(os.path.join("game_assets", "./support_towers/bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

    # function to run game
    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            # loop through enemies
            to_del = []
            for en in self.enemies:
                if en.x < -5:
                    to_del.append(en)

            # delete all enemies off the screen
            for d in to_del:
                self.enemys.remove(d)

            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))

        for enemy in self.enemies:
            enemy.draw(self.win)

        pygame.display.update()


g = Game()
g.run()
