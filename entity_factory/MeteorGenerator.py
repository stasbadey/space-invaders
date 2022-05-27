import random
from typing import List

from entity.Meteor import Meteor
from entity_factory.WaveFactory import WaveFactory
from render.Render import Render
from render.util import RenderProperties


class MeteorGenerator:
    rand: int = random.randrange(0, 2)
    meteors: List[Meteor] = []

    def __init__(self):
        pass

    def generate(self):
        global meteor_rect

        if len(MeteorGenerator.meteors) < WaveFactory.meteor_amount:
            generate_from_y_dot: int = random.randrange(50, RenderProperties.HEIGHT // 3)

            if MeteorGenerator.rand == 0:
                meteor_rect = Render.meteor_rectangle_render(generate_from_y_dot, 0)
            if MeteorGenerator.rand == 1:
                meteor_rect = Render.meteor_rectangle_render(generate_from_y_dot, RenderProperties.WIDTH - 20)

            meteor: Meteor = Meteor(meteor_rect, 1, 1)

            MeteorGenerator.meteors.append(meteor)
