import random
from typing import List

import pygame


from pygame import Rect
from entity.Alien import Alien
from entity.AlienPredator import AlienPredator
from entity.MajorAlien import MajorAlien
from entity.Meteor import Meteor
from entity.SpaceShip import SpaceShip
from entity.Ufo import Ufo
from render.util import RenderProperties


class Render:
    __x_rand: int = random.randrange(20, RenderProperties.WIDTH - 40)
    __y_rand: int = random.randrange(20, RenderProperties.HEIGHT // 3)
    boost: int = random.randrange(1, 3)
    set_boosters: bool = False
    booster_rect = None
    bullet_booster_rect = None
    spaceship_got_bullet_booster = False

    def __init__(self):
        self.__spaceship = None
        self.__aliens = None
        self.__meteors = None
        self.__type2_aliens = None
        self.__ufos = None
        self.__predator_alien = None
        self.__wave = None
        self.__health = None

    def set_spaceship(self, spaceship: SpaceShip):
        self.__spaceship = spaceship

    def set_aliens(self, aliens: List[Alien]):
        self.__aliens = aliens

    def set_meteors(self, meteors: List[Meteor]):
        self.__meteors = meteors

    def set_type2_aliens(self, type2_aliens: List[MajorAlien]):
        self.__type2_aliens = type2_aliens

    def set_ufos(self, ufos: List[Ufo]):
        self.__ufos = ufos

    def set_predator_alien(self, predator_alien: AlienPredator):
        self.__predator_alien = predator_alien

    def set_wave(self, wave: int):
        self.__wave = wave

    def set_health(self, health: int):
        self.__health = health

    def window_render(self):
        score = RenderProperties.SCORE_FONT.render("score: " + str(self.__spaceship.get_score()), 1, (255, 255, 255))
        wave = RenderProperties.WAVE_FONT.render("Wave: " + str(self.__wave), 1, (255, 255, 255))
        hp = RenderProperties.HP_FONT.render(str(self.__health), 1, (255, 255, 255))

        RenderProperties.WINDOW.blit(RenderProperties.SPACE, (0, 0))

        RenderProperties.WINDOW.blit(score, (10, 10))
        RenderProperties.WINDOW.blit(wave, (390, 970))
        RenderProperties.WINDOW.blit(RenderProperties.SPACESHIP_HP, (450, 10))
        RenderProperties.WINDOW.blit(hp, (480, 10))


        RenderProperties.WINDOW.blit(RenderProperties.SPACESHIP,
                                     (self.__spaceship.get_rectangle().x, self.__spaceship.get_rectangle().y))

        if Render.set_boosters is True:
            if Render.boost == 1 and Render.spaceship_got_bullet_booster is False:
                self.bullet_boost_render()
            if Render.boost == 2:
                self.power_up_boost_render()

        self.alien_render()
        self.type2_alien_render()
        self.ufo_render()
        self.spaceship_bullet_render()
        self.predator_alien_render()
        self.alien_bullet_render()
        self.type2_alien_bullet_render()
        self.ufo_bullet_render()
        self.predator_bullet_render()

        pygame.display.update()

    def alien_render(self):
        for alien in self.__aliens:
            alien_rect: Rect = alien.get_rectangle()

            RenderProperties.WINDOW.blit(RenderProperties.ALIEN_TYPE1, (alien_rect.x, alien_rect.y))

    @staticmethod
    def __boost_rect_render():
        return pygame.Rect(Render.__x_rand,
                           Render.__y_rand,
                           RenderProperties.POWER_UP_BOOST_WIDTH,
                           RenderProperties.POWER_UP_BOOST_HEIGHT)

    def bullet_boost_render(self):
        Render.bullet_booster_rect = self.__boost_rect_render()

        RenderProperties.WINDOW.blit(RenderProperties.BULLET_BOOST,
                                     (Render.bullet_booster_rect.x, Render.bullet_booster_rect.y))

    def power_up_boost_render(self):
        Render.booster_rect = self.__boost_rect_render()

        RenderProperties.WINDOW.blit(RenderProperties.POWER_UP_BOOST, (Render.booster_rect.x, Render.booster_rect.y))

    def type2_alien_render(self):
        for alien in self.__type2_aliens:
            alien_rect: Rect = alien.get_rectangle()

            RenderProperties.WINDOW.blit(RenderProperties.ALIEN_TYPE2, (alien_rect.x, alien_rect.y))

    def ufo_render(self):
        for ufo in self.__ufos:
            ufo_rect: Rect = ufo.get_rectangle()

            RenderProperties.WINDOW.blit(RenderProperties.UFO, (ufo_rect.x, ufo_rect.y))

    def predator_alien_render(self):
        if self.__predator_alien is not None:
            predator_alien_rect: Rect = self.__predator_alien.get_rectangle()

            RenderProperties.WINDOW.blit(RenderProperties.PREDATOR, (predator_alien_rect.x, predator_alien_rect.y))

    def meteor_render(self):
        for meteor in self.__meteors:
            meteor_rect: Rect = meteor.get_meteor_rect()

            RenderProperties.WINDOW.blit(RenderProperties.SMALL_METEOR, (meteor_rect.x, meteor_rect.y))

    @staticmethod
    def alien_rectangle_render(alien_rect_x: int):
        alien_rect: Rect = pygame.Rect(alien_rect_x, 100,  # todo randomize
                                       RenderProperties.ALIEN_TYPE1_WIDTH,
                                       RenderProperties.ALIEN_TYPE1_HEIGHT)

        alien = Alien([], 1, alien_rect, 1)

        return alien

    @staticmethod
    def type2_alien_rectangle_render(alien_rect_x: int):
        alien_rect: Rect = pygame.Rect(alien_rect_x, 40,
                                       RenderProperties.ALIEN_TYPE2_WIDTH,
                                       RenderProperties.ALIEN_TYPE2_HEIGHT)

        major_alien = MajorAlien([], 2, alien_rect, 1)

        return major_alien

    @staticmethod
    def ufo_rectangle_render(ufo_rect_x: int):
        ufo_rect: Rect = pygame.Rect(ufo_rect_x, 40,
                                     RenderProperties.ALIEN_TYPE2_WIDTH,
                                     RenderProperties.ALIEN_TYPE2_HEIGHT)

        ufo = Ufo([], 2, ufo_rect, 1)

        return ufo

    @staticmethod
    def meteor_rectangle_render(generate_from_y_dot: int, generate_from_x_dot: int):
        meteor_rect: Rect = pygame.Rect(generate_from_x_dot, generate_from_y_dot,
                                        RenderProperties.SMALL_METEOR_WIDTH,
                                        RenderProperties.SMALL_METEOR_HEIGHT)

        return meteor_rect

    @staticmethod
    def predator_render(rect_x: int = 200):
        predator_alien_rect: Rect = pygame.Rect(rect_x, 40, RenderProperties.PREDATOR_WIDTH, RenderProperties.PREDATOR_HEIGHT)

        predator_alien: AlienPredator = AlienPredator([], 15, predator_alien_rect, 3)

        return predator_alien

    @staticmethod  # todo
    def alient_duo_rectangle_render(alien_rect_x: int, alien_rect_y: int):
        alien_rect: Rect = pygame.Rect(alien_rect_x, alien_rect_y,
                                       RenderProperties.ALIEN_TYPE1_WIDTH,
                                       RenderProperties.ALIEN_TYPE1_HEIGHT)

        return alien_rect

    def alien_bullet_render(self):
        for alien in self.__aliens:
            alien_bullets = alien.get_bullets()

            for bullet in alien_bullets:
                if bullet.y <= 0:
                    alien_bullets.remove(bullet)

                bullet.y += RenderProperties.ALIEN_TYPE1_BULLET_VELOCITY

                RenderProperties.WINDOW.blit(RenderProperties.ALIEN_TYPE1_BULLET, (bullet.x, bullet.y))

    def type2_alien_bullet_render(self):
        for alien in self.__type2_aliens:
            alien_bullets = alien.get_bullets()

            for bullet in alien_bullets:
                if bullet.y <= 0:
                    alien_bullets.remove(bullet)

                bullet.y += RenderProperties.ALIEN_TYPE2_BULLET_VELOCITY

                RenderProperties.WINDOW.blit(RenderProperties.ALIEN_TYPE2_BULLET, (bullet.x, bullet.y))

    def ufo_bullet_render(self):
        for ufo in self.__ufos:
            ufo_bullets = ufo.get_bullets()

            for bullet in ufo_bullets:
                if bullet.y <= 0:
                    ufo_bullets.remove(bullet)

                bullet.y += RenderProperties.UFO_BULLET_VELOCITY

                RenderProperties.WINDOW.blit(RenderProperties.UFO_BULLET, (bullet.x, bullet.y))

    def predator_bullet_render(self):
        if self.__predator_alien is not None:
            predator_bullets: list = self.__predator_alien.get_bullets()

            for bullet in predator_bullets:
                if bullet.y <= 0:
                    predator_bullets.remove(bullet)

                if bullet.x < self.__spaceship.get_rectangle().x:
                    bullet.x += 2
                if bullet.x > self.__spaceship.get_rectangle().x:
                    bullet.x -= 2
                bullet.y += RenderProperties.PREDATOR_BULLET_VELOCITY

                RenderProperties.WINDOW.blit(RenderProperties.PREDATOR_BULLET, (bullet.x, bullet.y))

    def spaceship_bullet_render(self):
        spaceship_bullets = self.__spaceship.get_bullets()

        for bullet in spaceship_bullets:
            if bullet.y <= 0:
                spaceship_bullets.remove(bullet)

            bullet.y -= RenderProperties.BULLET_VELOCITY

            RenderProperties.WINDOW.blit(RenderProperties.SPACESHIP_BULLET, (bullet.x, bullet.y))

