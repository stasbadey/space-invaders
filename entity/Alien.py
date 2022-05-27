import pygame.sprite
from pygame import Rect
from pygame.sprite import Sprite
from entity.Explosion import Explosion


class Alien(pygame.sprite.Sprite):
    def __init__(self, bullets: list, health: float, rectangle: Rect, atype: int):
        Sprite.__init__(self)
        self.__bullets = bullets
        self.__health = health
        self.__rectangle = rectangle
        self.__atype = atype
        self.__killed = None
        self.explosions = []

    def __next__(self):
        self.__health -= 1

        return self.__health

    def draw_screen(self, screen):
        for explosion in self.explosions:
            explosion.draw_explosion(screen)

    def update_screen(self, x, y):
        explosion = Explosion(x, y)
        self.explosions.append(explosion)

    def get_bullets(self):
        return self.__bullets

    def get_health(self):
        return self.__health

    def set_health(self, health: float):
        self.__health = health

    def get_rectangle(self):
        return self.__rectangle

    def set_bullets(self, bullets: list):
        self.__bullets = bullets

    def set_rectangle(self, rectangle: Rect):
        self.__rectangle = rectangle

    def set_type(self, atype: int):
        self.__atype = atype

    def get_type(self):
        return self.__atype

    def set_killed_alien(self, killed):
        self.__killed = killed

    def get_killed_alien(self):
        return self.__killed
