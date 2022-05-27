import time
from typing import List

import pygame

from pygame import Rect
from entity.Alien import Alien
from entity.AlienPredator import AlienPredator
from entity.MajorAlien import MajorAlien
from entity.SpaceShip import SpaceShip
from entity.Ufo import Ufo
from entity.Explosion import Explosion
from entity_factory.AlienGenerator import AlienGenerator
from entity_factory.WaveFactory import WaveFactory
from render.Render import Render
from render.util import RenderProperties



class EntityFactory:
    __got_bullet_booster = False

    def __init__(self):
        self.__spaceship = None
        self.__aliens = None
        self.__type2_aliens = None
        self.__pressed_key = None
        self.__ufos = None
        self.__predator_alien = None
        self.__render = Render()

    def set_spaceship(self, spaceship: SpaceShip):
        self.__spaceship = spaceship

    def set_aliens(self, aliens: List[Alien]):
        self.__aliens = aliens

    def set_pressed_key(self, pressed_key):
        self.__pressed_key = pressed_key

    def set_type2_aliens(self, type2_aliens: List[MajorAlien]):
        self.__type2_aliens = type2_aliens

    def set_ufos(self, ufos: List[Ufo]):
        self.__ufos = ufos

    def set_predator_alien(self, predator_alien: AlienPredator):
        self.__predator_alien = predator_alien

    # todo move in different class
    def keyboard_handler(self):
        spaceship_rect: Rect = self.__spaceship.get_rectangle()

        if self.__pressed_key[pygame.K_d] \
                and spaceship_rect.x + RenderProperties.SPACESHIP_VELOCITY < RenderProperties.WIDTH - 50:
            spaceship_rect.x += RenderProperties.SPACESHIP_VELOCITY

        if self.__pressed_key[pygame.K_a] and spaceship_rect.x + RenderProperties.SPACESHIP_VELOCITY > 5:
            spaceship_rect.x -= RenderProperties.SPACESHIP_VELOCITY

    def spaceship_bullet_factory(self):
        spaceship_rect: Rect = self.__spaceship.get_rectangle()

        spaceship_bullets: list = self.__spaceship.get_bullets()

        if EntityFactory.__got_bullet_booster is True:
            right_bullet = pygame.Rect(spaceship_rect.x - 10, spaceship_rect.y - 50,
                                       RenderProperties.BULLET_WIDTH, RenderProperties.BULLET_HEIGHT)

            left_bullet = pygame.Rect(spaceship_rect.x + 50, spaceship_rect.y - 50,
                                      RenderProperties.BULLET_WIDTH, RenderProperties.BULLET_HEIGHT)

            if len(spaceship_bullets) < 2:
                spaceship_bullets.append(right_bullet)
                spaceship_bullets.append(left_bullet)

        if len(spaceship_bullets) < 1:
            bullet = pygame.Rect(spaceship_rect.x, spaceship_rect.y - 50,
                                 RenderProperties.BULLET_WIDTH, RenderProperties.BULLET_HEIGHT)

            spaceship_bullets.append(bullet)

        for index1, bullet in enumerate(spaceship_bullets):
            for index, alien in enumerate(self.__aliens):
                alien_rect: Rect = alien.get_rectangle()

                if spaceship_rect.colliderect(bullet):

                    pygame.event.post(pygame.event.Event(RenderProperties.HIT_THE_SPACESHIP_EVENT))

                if alien_rect.colliderect(bullet):
                    self.__aliens.pop(index)
                    alien.update_screen(alien_rect.x, alien_rect.y)
                    alien.draw_screen(RenderProperties.WINDOW)

                    spaceship_bullets.pop(index1)
                    pygame.event.post(pygame.event.Event(RenderProperties.HIT_ALIEN_TYPE1_EVENT))


                if self.__render.booster_rect is not None and self.__render.booster_rect.colliderect(bullet):
                    self.__render.booster_rect.x = 1000
                    self.__render.booster_rect.y = 1000
                    Render.set_boosters = False

                    spaceship_bullets.pop(index1)

                    pygame.event.post(pygame.event.Event(RenderProperties.SPACESHIP_GET_POWER_UP_BOOST))

                if self.__render.bullet_booster_rect is not None and self.__render.bullet_booster_rect.colliderect(
                        bullet):
                    self.__render.bullet_booster_rect.x = 1000
                    self.__render.bullet_booster_rect.y = 1000
                    EntityFactory.__got_bullet_booster = True
                    Render.spaceship_got_bullet_booster = True
                    Render.set_boosters = False

                    spaceship_bullets.pop(index1)
                    pygame.event.post(pygame.event.Event(RenderProperties.SPACESHIP_GET_BULLET_BOOST))

            for index, alien in enumerate(self.__type2_aliens):
                alien_rect: Rect = alien.get_rectangle()

                if alien_rect.colliderect(bullet):
                    spaceship_bullets.pop(index1)

                    alien.set_health(alien.get_health() - 1)

                    if round(alien.get_health()) == 0:
                        self.__type2_aliens.pop(index)

            for index, ufo in enumerate(self.__ufos):
                ufo_rect: Rect = ufo.get_rectangle()

                if ufo_rect.colliderect(bullet):
                    spaceship_bullets.pop(index1)
                    AlienGenerator.spawn_ufo = False

                    self.__ufos.pop(index)

                    pygame.event.post(pygame.event.Event(RenderProperties.HIT_THE_UFO_EVENT))

            if self.__predator_alien is not None and self.__predator_alien.get_rectangle().colliderect(bullet):
                if self.__predator_alien.get_health() - 1 == 0:
                    self.__predator_alien.get_rectangle().x = 1000
                    self.__predator_alien.get_rectangle().y = 1000

                    pygame.event.post(pygame.event.Event(RenderProperties.SPACESHIP_BEAT_UP_PREDATOR_EVENT))

                spaceship_bullets.pop(index1)

                self.__predator_alien.set_health(self.__predator_alien.get_health() - 1)

    def alien_bullet_factory(self):
        time.sleep(0.5)

        for alien in self.__aliens:
            alien_rect: Rect = alien.get_rectangle()

            alien_bullet = pygame.Rect(alien_rect.x, alien_rect.y + 50,
                                       RenderProperties.BULLET_WIDTH, RenderProperties.BULLET_HEIGHT)

            alien_bullets: list = alien.get_bullets()

            if len(alien_bullets) < WaveFactory.alien_bullet_amount:
                alien_bullets.append(alien_bullet)

            spaceship_rect: Rect = self.__spaceship.get_rectangle()

            for bullet in alien_bullets:
                if bullet.y > RenderProperties.HEIGHT:
                    alien_bullets.remove(bullet)

                if spaceship_rect.colliderect(bullet):
                    alien_bullets.remove(bullet)

                    pygame.event.post(pygame.event.Event(RenderProperties.HIT_THE_SPACESHIP_EVENT))

    def type2_alien_bullet_factory(self):
        time.sleep(0.2)

        for alien in self.__type2_aliens:
            alien_rect: Rect = alien.get_rectangle()

            alien_left_bullet = pygame.Rect(alien_rect.x + 19, alien_rect.y + 50,
                                            RenderProperties.BULLET_WIDTH,
                                            RenderProperties.BULLET_HEIGHT)

            alien_right_bullet = pygame.Rect(alien_rect.x + 32, alien_rect.y + 50,
                                             RenderProperties.BULLET_WIDTH,
                                             RenderProperties.BULLET_HEIGHT)

            alien_bullets: list = alien.get_bullets()

            if len(alien_bullets) < WaveFactory.alien_bullet_amount:
                alien_bullets.append(alien_left_bullet)
                alien_bullets.append(alien_right_bullet)

            spaceship_rect: Rect = self.__spaceship.get_rectangle()

            for index, bullet in enumerate(alien_bullets):
                if bullet.y > RenderProperties.HEIGHT:
                    alien_bullets.pop(index)

                if spaceship_rect.colliderect(bullet):
                    pygame.event.post(pygame.event.Event(RenderProperties.HIT_ALIEN_TYPE2_EVENT))

                    alien.set_health(alien.get_health() + 0.1)
                    alien_bullets.pop(index)

    def ufo_bullet_factory(self):
        time.sleep(0.5)

        for ufo in self.__ufos:
            ufo_rect: Rect = ufo.get_rectangle()

            ufo_bullet = pygame.Rect(ufo_rect.x, ufo_rect.y + 50,
                                     RenderProperties.UFO_BULLET_WIDTH, RenderProperties.UFO_BULLET_HEIGHT)

            ufo_bullets: list = ufo.get_bullets()

            if len(ufo_bullets) < WaveFactory.alien_bullet_amount:
                ufo_bullets.append(ufo_bullet)

            spaceship_rect: Rect = self.__spaceship.get_rectangle()

            for bullet in ufo_bullets:
                if bullet.y > RenderProperties.HEIGHT:
                    ufo_bullets.remove(bullet)

                if spaceship_rect.colliderect(bullet):
                    ufo_bullets.remove(bullet)

                    pygame.event.post(pygame.event.Event(RenderProperties.HIT_THE_SPACESHIP_EVENT))

    def predator_alien_bullet_factory(self):
        time.sleep(0.5)

        if self.__predator_alien is not None:
            predator_rect: Rect = self.__predator_alien.get_rectangle()

            predator_bullet = pygame.Rect(predator_rect.x, predator_rect.y + 50, RenderProperties.PREDATOR_BULLET_WIDTH,
                                          RenderProperties.PREDATOR_BULLET_HEIGHT)

            predator_bullets: list = self.__predator_alien.get_bullets()

            if len(predator_bullets) < 1:
                predator_bullets.append(predator_bullet)

            spaceship_rect: Rect = self.__spaceship.get_rectangle()

            for bullet in predator_bullets:
                if bullet.y > RenderProperties.HEIGHT:
                    predator_bullets.remove(bullet)

                if spaceship_rect.colliderect(bullet):
                    predator_bullets.remove(bullet)

                    pygame.event.post(pygame.event.Event(RenderProperties.HIT_THE_SPACESHIP_EVENT))