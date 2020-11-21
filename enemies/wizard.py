import pygame
import os
from enemies.enemy import Enemy

class Wizard(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = []

        for x in range(20):
            add_str = str(x)
            if x < 10:
                add_str = "0" + add_str
            self.imgs.append(pygame.transform.scale(pygame.image.load(os.path.join(
                "game_assets/enemies/2", "2_enemies_1_run_0" + add_str + ".png")), (64, 64)))