import random
import time
from typing import List

import pygame.event
from pygame import Rect

from entity.Alien import Alien
from entity.AlienPredator import AlienPredator
from entity.MajorAlien import MajorAlien
from entity.Ufo import Ufo
from render.Render import Render
from render.util import RenderProperties


class AlienMovements:
    zig_zag_counter: int = 0
    counter = 0
    rand: int = random.randrange(1, 5)

    def __init__(self, aliens: List[Alien]):
        self.__aliens = aliens
        self.__spaceship_rect = None
        self.__major_aliens = None
        self.__ufos = None
        self.__predator_alien = None

    def set_spaceship_rect(self, spaceship_rect: Rect):
        self.__spaceship_rect = spaceship_rect

    def set_major_aliens(self, major_aliens: List[MajorAlien]):
        self.__major_aliens = major_aliens

    def set_ufos(self, ufos: List[Ufo]):
        self.__ufos = ufos

    def set_predator_alien(self, predator_alien: AlienPredator):
        self.__predator_alien = predator_alien

    def aliens_type1_movements(self):
        step: int = 2

        for alien in self.__aliens:
            time.sleep(float(random.uniform(0.5, 1.5)))

            alien_would_move_to: int = self.__spaceship_rect.x

            updated_alien: Alien = Render.alien_rectangle_render(alien_would_move_to)

            if alien.get_rectangle().x < updated_alien.get_rectangle().x:
                while alien.get_rectangle().x <= updated_alien.get_rectangle().x:
                    time.sleep(0.5)
                    if alien.get_rectangle().x > RenderProperties.WIDTH - 30:
                        break
                    alien.get_rectangle().x += step
                    alien.get_rectangle().y += 1
            else:
                while alien.get_rectangle().x >= updated_alien.get_rectangle().x:
                    time.sleep(0.5)
                    if alien.get_rectangle().x < 0:
                        break
                    alien.get_rectangle().x -= step
                    alien.get_rectangle().y += 1
            if len(self.__aliens) != 0 and self.__spaceship_rect.colliderect(alien.get_rectangle()):
                self.__aliens.remove(alien)
                pygame.event.post(pygame.event.Event(RenderProperties.ALIEN_TOUCH_A_SPACESHIP_EVENT))
            if len(self.__aliens) != 0 and alien.get_rectangle().y > RenderProperties.HEIGHT - 20:
                self.__aliens.remove(alien)

    def aliens_type2_movements(self):
        step: int = 1

        for alien in self.__major_aliens:
            time.sleep(float(random.uniform(1, 2.2)))

            alien_rect: Rect = alien.get_rectangle()

            alien_would_move_to: int = self.__spaceship_rect.x

            updated_alien: Alien = Render.type2_alien_rectangle_render(alien_would_move_to)

            if alien_rect.x < updated_alien.get_rectangle().x:
                alien_rect.x += step
            else:
                alien_rect.x -= step

    def ufo_movements(self):
        for ufo in self.__ufos:
            ufo_rect: Rect = ufo.get_rectangle()

            if AlienMovements.rand == 1:
                if ufo_rect.x + 1 > RenderProperties.WIDTH - 100:
                    AlienMovements.rand = random.randrange(1, 5)
                    break
                ufo_rect.x += 4
            if AlienMovements.rand == 2:
                if ufo_rect.y + 1 > RenderProperties.HEIGHT - 350:
                    AlienMovements.rand = random.randrange(1, 5)
                    break
                ufo_rect.y += 4
            if AlienMovements.rand == 3:
                if ufo_rect.x - 1 < 100:
                    AlienMovements.rand = random.randrange(1, 5)
                    break
                ufo_rect.x -= 4
            if AlienMovements.rand == 4:
                if ufo_rect.y - 1 < 150:
                    AlienMovements.rand = random.randrange(1, 5)
                    break
                ufo_rect.y -= 4

    def predator_alien_movements(self):
        time.sleep(float(random.uniform(1, 2.2)))

        if self.__predator_alien is not None:
            alien_rect: Rect = self.__predator_alien.get_rectangle()

            alien_would_move_to: int = self.__spaceship_rect.x

            updated_alien: Alien = Render.predator_render(alien_would_move_to)

            if alien_rect.x < updated_alien.get_rectangle().x:
                alien_rect.x += 1
            else:
                alien_rect.x -= 1
