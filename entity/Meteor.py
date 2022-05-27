from pygame import Rect


# todo enums with mtype and atype
class Meteor:
    def __init__(self, meteor_rect: Rect, speed: int, mtype: int):
        self.__meteor_rect = meteor_rect
        self.__speed = speed
        self.__mtype = mtype

    def get_meteor_rect(self):
        return self.__meteor_rect

    def get_speed(self):
        return self.__speed

    def get_mtype(self):
        return self.__mtype
