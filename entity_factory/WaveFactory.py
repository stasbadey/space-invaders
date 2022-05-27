from render.Render import Render


class WaveFactory:
    alien_bullet_amount: int = 0 #0
    type1_alien_amount: int = 3 #3
    type2_alien_amount: int = 0 #0
    ufo_amount: int = 0 #0
    meteor_amount: int = 0 #0
    spaceship_health: int = 3 #3
    __major_alien_killed: bool = False #False
    __spawn_ufo = None
    spawn_predator_alien = False
    wave: int = 1

    def major_alien_killed(self, killed=True):
        WaveFactory.__major_alien_killed = killed

    @staticmethod
    def set_spawn_ufo(spawn_ufo: bool):
        WaveFactory.__spawn_ufo = spawn_ufo

    @staticmethod
    def waves(score: int):
        if score == 10:
            WaveFactory.wave = 2
            WaveFactory.alien_bullet_amount = 1
        if score == 15:
            WaveFactory.wave = 3
            WaveFactory.type1_alien_amount = 5
        if score == 20:
            WaveFactory.wave = 4
            Render.set_boosters = True
        if score == 25:
            WaveFactory.wave = 5
            WaveFactory.type1_alien_amount = 6
        if score == 30:
            WaveFactory.wave = 6
            if WaveFactory.spaceship_health < 3:
                WaveFactory.spaceship_health = 3
            WaveFactory.meteor_amount = 2
        if score == 35:
            WaveFactory.wave = 7
            WaveFactory.type2_alien_amount = 1
        if WaveFactory.__major_alien_killed is True and score >= 40:
            WaveFactory.wave = 8
            WaveFactory.type2_alien_amount = 2
            WaveFactory.type1_alien_amount = 0
            WaveFactory.__major_alien_killed = False
        if WaveFactory.__major_alien_killed is True and score >= 42:
            WaveFactory.wave = 9
            WaveFactory.type2_alien_amount = 0
            WaveFactory.type1_alien_amount = 7
            WaveFactory.alien_bullet_amount = 2
            WaveFactory.__major_alien_killed = False
        if WaveFactory.__major_alien_killed is True and score >= 51:
            WaveFactory.wave = 10
            WaveFactory.type2_alien_amount = 3
            WaveFactory.alien_bullet_amount = 1
            WaveFactory.__major_alien_killed = False
        if WaveFactory.__major_alien_killed is True and score >= 55:
            WaveFactory.wave = 11
            WaveFactory.spaceship_health = 5
            WaveFactory.ufo_amount = 1
        if score >= 61:
            WaveFactory.wave = 12
            WaveFactory.ufo_amount = 2
            WaveFactory.spaceship_health = 5
        if score >= 63:
            WaveFactory.wave = 13
            WaveFactory.type1_alien_amount = 0
            WaveFactory.type2_alien_amount = 3
            WaveFactory.ufo_amount = 3
            Render.set_boosters = True
        if score >= 69:
            WaveFactory.wave = 14
            WaveFactory.type1_alien_amount = 23
            WaveFactory.alien_bullet_amount = 0
            WaveFactory.type2_alien_amount = 0
            WaveFactory.ufo_amount = 0
        if score >= 98:
            WaveFactory.wave = 15
            WaveFactory.type1_alien_amount = 5
            WaveFactory.alien_bullet_amount = 1
            WaveFactory.type2_alien_amount = 4
            WaveFactory.ufo_amount = 2
        if score >= 109:
            WaveFactory.wave = 16
            WaveFactory.spaceship_health = 7
            WaveFactory.type1_alien_amount = 10
            WaveFactory.alien_bullet_amount = 1
            WaveFactory.type2_alien_amount = 3
            WaveFactory.ufo_amount = 4
        if score >= 126:
            WaveFactory.wave = 17
            WaveFactory.type1_alien_amount = 17
            WaveFactory.alien_bullet_amount = 1
            WaveFactory.type2_alien_amount = 2
            WaveFactory.ufo_amount = 2
        if score >= 147:
            WaveFactory.wave = 18
            Render.set_boosters = True
            WaveFactory.type1_alien_amount = 24
            WaveFactory.alien_bullet_amount = 1
            WaveFactory.type2_alien_amount = 0
            WaveFactory.ufo_amount = 0
        if score >= 171:
            WaveFactory.wave = 19
            WaveFactory.type1_alien_amount = 24
            WaveFactory.alien_bullet_amount = 1
            WaveFactory.type2_alien_amount = 1
            WaveFactory.ufo_amount = 1
        if score >= 197:
            WaveFactory.wave = 20
            WaveFactory.spaceship_health = 7
            WaveFactory.alien_bullet_amount = 1
            WaveFactory.type2_alien_amount = 0
            WaveFactory.ufo_amount = 0
            WaveFactory.spawn_predator_alien = True
