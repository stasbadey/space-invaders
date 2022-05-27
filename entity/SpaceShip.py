from pygame import Rect
from entity.Explosion import Explosion


class SpaceShip:
    def __init__(self, bullets: list, health: int, rectangle: Rect, score: int):
        self.__bullets = bullets
        self.__health = health
        self.__rectangle = rectangle
        self.__score = score
        self.explosions = []




    def __next__(self):
        self.__health -= 1

        return self.__health

    def get_bullets(self):
        return self.__bullets

    def get_health(self):
        return self.__health

    def set_health(self, health: int):
        self.__health = health

    def get_rectangle(self):
        return self.__rectangle

    def set_bullets(self, bullets: list):
        self.__bullets = bullets

    def set_rectangle(self, rectangle: Rect):
        self.__rectangle = rectangle

    def set_score(self, score: int):
        self.__score = score

    def get_score(self):
        return self.__score
