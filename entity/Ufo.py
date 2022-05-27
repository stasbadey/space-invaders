from pygame import Rect

from entity.Alien import Alien


class Ufo(Alien):
    def __init__(self, bullets: list, health: float, rectangle: Rect, atype: int):
        super().__init__(bullets, health, rectangle, atype)
