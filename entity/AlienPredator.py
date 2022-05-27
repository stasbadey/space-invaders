from pygame import Rect
from pygame.sprite import Sprite

from entity.Alien import Alien


class AlienPredator(Alien, Sprite):
    def __init__(self, bullets: list, health: int, rectangle: Rect, atype: int):
        super().__init__(bullets, health, rectangle, atype)
        Sprite.__init__(self)
        self.__bullets = bullets
        self.__health = health
        self.__rectangle = rectangle
        self.__atype = atype

    def __next__(self):
        super().__health += 1
