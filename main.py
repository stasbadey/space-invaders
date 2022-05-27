import threading

import pygame

from pygame import Rect

from dao.ScoreDao import ScoreDao
from entity.SpaceShip import SpaceShip
from entity_factory.AlienGenerator import AlienGenerator
from entity_factory.AlienMovements import AlienMovements
from entity_factory.EntityFactory import EntityFactory
from entity_factory.MeteorGenerator import MeteorGenerator
from entity_factory.MeteorMovements import MeteorMovements
from entity_factory.WaveFactory import WaveFactory
from render.Render import Render
from render.util import RenderProperties
from menu import Menu


def main():
    Menu.show_menu()


def start_game():
    spaceship_bullets: list = []
    spaceship_rect: Rect = pygame.Rect(230, 915, RenderProperties.SPACESHIP_WIDTH, RenderProperties.SPACESHIP_HEIGHT)
    spaceship_health: int = 3
    score: int = 0

    spaceship = SpaceShip(spaceship_bullets, spaceship_health, spaceship_rect, score)

    run = True

    clock = pygame.time.Clock()

    while run:
        clock.tick(RenderProperties.FPS)

        alien_generator = AlienGenerator()

        render = Render()

        render.set_spaceship(spaceship)

        entity_factory = EntityFactory()

        entity_factory.set_spaceship(spaceship)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == RenderProperties.HIT_THE_SPACESHIP_EVENT:
                RenderProperties.ALIEN_GOT_HIT_SOUND.play()

                if next(spaceship) == 0:
                    run = False
                    Menu.game_over()

                    score_dao: ScoreDao = ScoreDao(score)
                    score_dao.save_score()

            if event.type == RenderProperties.HIT_ALIEN_TYPE1_EVENT:
                RenderProperties.HIT_SOUND.play()


                score += 1
                spaceship.set_score(score)

            if event.type == RenderProperties.HIT_THE_UFO_EVENT:
                RenderProperties.HIT_SOUND.play()

                score += 1
                spaceship.set_score(score)

            if event.type == RenderProperties.SPACESHIP_GET_BULLET_BOOST:
                RenderProperties.BOOST_UP.play()

            if event.type == RenderProperties.ALIEN_TOUCH_A_SPACESHIP_EVENT:
                Menu.game_over()

            if event.type == RenderProperties.HIT_ALIEN_TYPE2_EVENT:
                RenderProperties.HIT_SOUND.play()

                Render.type2_alien_render(RenderProperties.ALIEN_TYPE2)
                score += 1

                if next(spaceship) == 0:
                    run = False
                    Menu.game_over()

            if event.type == RenderProperties.SPACESHIP_BEAT_UP_PREDATOR_EVENT:
                run = False

                RenderProperties.BEAT_UP_PREDATOR_SOUND.play()

            if event.type == RenderProperties.SPACESHIP_GET_POWER_UP_BOOST:
                RenderProperties.BOOST_UP.play()

                spaceship.set_health(spaceship.get_health() + 2)

        entity_factory.set_pressed_key(pygame.key.get_pressed())

        entity_factory.keyboard_handler()

        WaveFactory.waves(score)

        render.set_aliens(AlienGenerator.type1_aliens)
        render.set_type2_aliens(AlienGenerator.type2_aliens)
        render.set_ufos(AlienGenerator.ufos)

        entity_factory.set_aliens(AlienGenerator.type1_aliens)
        entity_factory.set_type2_aliens(AlienGenerator.type2_aliens)
        entity_factory.set_ufos(AlienGenerator.ufos)
        entity_factory.set_predator_alien(AlienGenerator.predator)

        thread2 = threading.Thread(target=alien_generator.generate)
        thread2.start()

        thread = threading.Thread(target=entity_factory.spaceship_bullet_factory)
        thread.start()

        thread1 = threading.Thread(target=entity_factory.alien_bullet_factory)
        thread1.start()

        thread1 = threading.Thread(target=entity_factory.type2_alien_bullet_factory)
        thread1.start()

        thread6 = threading.Thread(target=entity_factory.ufo_bullet_factory)
        thread6.start()

        thread8 = threading.Thread(target=entity_factory.predator_alien_bullet_factory)
        thread8.start()

        render.set_aliens(alien_generator.type1_aliens)
        render.set_predator_alien(alien_generator.predator)
        render.set_health(spaceship.get_health())
        render.set_wave(WaveFactory.wave)

        alien_movements = AlienMovements(AlienGenerator.type1_aliens)
        alien_movements.set_major_aliens(AlienGenerator.type2_aliens)
        alien_movements.set_ufos(AlienGenerator.ufos)
        alien_movements.set_predator_alien(AlienGenerator.predator)

        thread5 = threading.Thread(target=alien_movements.aliens_type2_movements)
        thread5.start()

        thread7 = threading.Thread(target=alien_movements.predator_alien_movements)
        thread7.start()

        alien_movements.set_spaceship_rect(spaceship.get_rectangle())

        thread3 = threading.Thread(target=alien_movements.aliens_type1_movements)
        thread3.start()

        alien_movements.ufo_movements()

        render.window_render()

        meteor_movements = MeteorMovements(MeteorGenerator.meteors)

        meteor_movements.set_spaceship_rectangle(spaceship.get_rectangle())


if __name__ == '__main__':
    main()
