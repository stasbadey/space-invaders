import random
from typing import List

import pygame
from pygame import Rect

from entity.Meteor import Meteor
from render.util import RenderProperties


class MeteorMovements:
    __step_counter: int = 0
    meteor_finish_point_x: int = random.randrange(30, RenderProperties.WIDTH - 30)

    def __init__(self, meteors: List[Meteor]):
        self.__meteors = meteors
        self.__spaceship_rect = None

    def set_spaceship_rectangle(self, spaceship_rect: Rect):
        self.__spaceship_rect = spaceship_rect

    def movement(self):
        for meteor in self.__meteors:
            meteor_rect: Rect = meteor.get_meteor_rect()

            while meteor_rect.x < MeteorMovements.meteor_finish_point_x and meteor_rect.y < RenderProperties.HEIGHT - 20:
                meteor_rect.x += 1

            while meteor_rect.x > 0 and meteor_rect.y < RenderProperties.HEIGHT - 20:
                meteor_rect.x -= 1

            if self.__spaceship_rect.colliderect(meteor_rect):
                self.__meteors.remove(meteor)
                pygame.event.post(pygame.event.Event(RenderProperties.ALIEN_TOUCH_A_SPACESHIP_EVENT))
