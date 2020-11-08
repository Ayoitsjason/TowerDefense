import pygame
import math


class Enemy:

    imgs = []

    def __init__(self, x, y):
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(45, 223), (172, 225), (221, 264), (271, 285), (529, 280), (577, 254), (614, 203), (632, 109), (696, 62), (769, 61), (813, 106), (836, 180), (859, 251), (927, 272), (996, 299),
                     (1040, 341), (1047, 416), (1017, 473), (970, 498), (898, 497), (765, 499), (721, 523), (680, 550), (619, 549), (292, 557), (186, 552), (133, 537), (99, 496), (81, 401), (44, 356), (2, 347)]
        self.img = None
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]

        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        win.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, X, Y):
        """
        Returns if position has hit enemy
        :param x: int
        :param y: int
        :return: bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def move(self):
        """
        Move enemy
        :return: None
        """
        x1, y1 = self.path[self.path_pas]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-2, )
        else:
            x2, y2 = self.path[self.path_pos+1]

        move_dis = math.sqrt(((x2-x1)**2 + (y2-y1)**2))

        self.move_count += 1
        dirn = (x2 - x1, y2 - y1)

        pos = (self.x + dirn[0] * self.move_count,
               self.y + dirn[1] * self.move_count)
        self.dis += math.sqrt((move_x-x1)**2 + (move_y-y1)**2)

        # go to next point
        if self.dis >= move.dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1

        self.x = move_x
        self.y = move_y

    def hit(self):
        """
        Return True if health reaches 0
        :return: bool
        """
        self.health -= 1
        if self.health <= 0:
            return true
