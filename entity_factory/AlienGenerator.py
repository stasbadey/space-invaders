import random
from typing import List

from entity.Alien import Alien
from entity.AlienPredator import AlienPredator
from entity.MajorAlien import MajorAlien
from entity.Ufo import Ufo
from entity_factory.WaveFactory import WaveFactory
from render.Render import Render
from render.util import RenderProperties


# todo interfaces
class AlienGenerator:
    type1_aliens: List[Alien] = []
    type2_aliens: List[MajorAlien] = []
    ufos: List[Ufo] = []
    predator: AlienPredator = None
    spawn_ufo = True

    def __init__(self):
        pass

    def generate(self):
        while len(AlienGenerator.type1_aliens) != WaveFactory.type1_alien_amount:
            alien_rect_x: int = self.__collision_checker(random.randrange(10, RenderProperties.WIDTH - 30))

            alien: Alien = Render.alien_rectangle_render(alien_rect_x)

            AlienGenerator.type1_aliens.append(alien)

        while len(AlienGenerator.type2_aliens) != WaveFactory.type2_alien_amount:
            alien_rect_x: int = random.randrange(150, RenderProperties.WIDTH - 150)

            major_alien: MajorAlien = Render.type2_alien_rectangle_render(alien_rect_x)

            AlienGenerator.type2_aliens.append(major_alien)

        while len(AlienGenerator.ufos) != WaveFactory.ufo_amount and AlienGenerator.spawn_ufo is True:
            ufo: Ufo = Render.ufo_rectangle_render(20)

            AlienGenerator.ufos.append(ufo)

        while WaveFactory.spawn_predator_alien is True:
            AlienGenerator.predator = Render.predator_render()

            WaveFactory.spawn_predator_alien = False

    def __collision_checker(self, type1_alien_rect_x: int):
        for alien in AlienGenerator.type1_aliens:
            alien_rect_x = alien.get_rectangle().x

            if alien_rect_x == type1_alien_rect_x or alien_rect_x - 50 <= type1_alien_rect_x <= alien_rect_x + 50:
                return self.__collision_checker(random.randrange(10, RenderProperties.WIDTH - 30))
        return type1_alien_rect_x