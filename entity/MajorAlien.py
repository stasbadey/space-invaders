from pygame import Rect

from entity.Alien import Alien


class MajorAlien(Alien):
    def __init__(self, bullets: list, health: float, rectangle: Rect, atype: int):
        super().__init__(bullets, health, rectangle, atype)
        self.__health = health

    def __next__(self):
        self.__health += 0.1

        return self.__health
