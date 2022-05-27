import json
import random
import pygame

from pygame.sprite import Group

pygame.init()

JSON_PATH = "properties.json"

MAP_PROPS = "mapProps"
ENEMIES = "enemies"
MAIN_CHARACTER = "mainCharacter"
ANIMATIONS = "animations"


def get_property(struct: str, property: str):
    with open(JSON_PATH, 'r') as data:
        contents: dict = json.loads(data.read())

    return contents[struct][0].get(property)


def alien_image_picker():
    pick: int = random.randrange(1, 4)

    if pick == 1:
        return ALIEN_TYPE1_1_IMAGE
    if pick == 2:
        return ALIEN_TYPE1_2_IMAGE
    if pick == 3:
        return ALIEN_TYPE1_3_IMAGE
    else:
        return ALIEN_TYPE1_4_IMAGE


def background_picker():
    pick: int = random.randrange(1, 4)

    if pick == 1:
        return BLUE_SPACE_IMAGE
    if pick == 2:
        return BLACK_SPACE_IMAGE
    if pick == 3:
        return DARK_PURPLE_SPACE_IMAGE
    else:
        return PURPLE_SPACE_IMAGE


FPS = get_property(MAP_PROPS, "gameFPS")

GAME_CAPTION = get_property(MAP_PROPS, "gameCaption")

HIT_SOUND = pygame.mixer.Sound(get_property(MAP_PROPS, "spaceshipHitSoundPath"))
ALIEN_GOT_HIT_SOUND = pygame.mixer.Sound(get_property(MAP_PROPS, "spaceshipGotHitSoundPath"))
BOOST_UP = pygame.mixer.Sound(get_property(MAP_PROPS, "spaceshipGotBoosterSoundPath"))
BEAT_UP_PREDATOR_SOUND = pygame.mixer.Sound(get_property(MAP_PROPS, "spaceshipBeatUpThePredatorSoundPath"))
WIDTH, HEIGHT = get_property(MAP_PROPS, "gameWidth"), get_property(MAP_PROPS, "gameHeight")

BORDER = pygame.Rect(0, 10, WIDTH, HEIGHT)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

SCORE_FONT = pygame.font.SysFont('comicsans', 40)
WAVE_FONT = pygame.font.SysFont('comicsans', 40)
HP_FONT = pygame.font.SysFont('comicsans', 40)
GAME_OVER = pygame.font.SysFont('comicsans', 60)

HIT_THE_SPACESHIP_EVENT = pygame.USEREVENT + 1
HIT_ALIEN_TYPE1_EVENT = pygame.USEREVENT + 2
HIT_ALIEN_TYPE2_EVENT = pygame.USEREVENT + 3
ALIEN_TOUCH_A_SPACESHIP_EVENT = pygame.USEREVENT + 4
SPACESHIP_GET_POWER_UP_BOOST = pygame.USEREVENT + 5
SPACESHIP_GET_BULLET_BOOST = pygame.USEREVENT + 6
SPACESHIP_BEAT_UP_PREDATOR_EVENT = pygame.USEREVENT + 7
HIT_THE_UFO_EVENT = pygame.USEREVENT + 8
SPACESHIP_GET_LASER_BOOST = pygame.USEREVENT + 9


ALIEN_TYPE1_VELOCITY = get_property("enemies", "alienVelocity")
ALIEN_TYPE1_1_IMAGE = pygame.image.load(get_property(ENEMIES, "alienImage1"))
ALIEN_TYPE1_2_IMAGE = pygame.image.load(get_property(ENEMIES, "alienImage2"))
ALIEN_TYPE1_3_IMAGE = pygame.image.load(get_property(ENEMIES, "alienImage3"))
ALIEN_TYPE1_4_IMAGE = pygame.image.load(get_property(ENEMIES, "alienImage4"))
ALIEN_TYPE1_WIDTH, ALIEN_TYPE1_HEIGHT = get_property(ENEMIES, "alienWidth"), get_property(ENEMIES, "alienHeight")

ALIEN_TYPE1_BULLET_VELOCITY = get_property(ENEMIES, "alienLaserVelocity")
ALIEN_TYPE1_BULLET_WIDTH, ALIEN_TYPE1_BULLET_HEIGHT = get_property(ENEMIES, "alienLaserWidth"), \
                                                      get_property(ENEMIES, "alienLaserHeight")
ALIEN_TYPE1_BULLET_IMAGE = pygame.image.load(get_property(ENEMIES, "alienLaserImage"))

ALIEN_TYPE2_BULLET_VELOCITY = get_property(ENEMIES, "majorAlienLaserVelocity")
ALIEN_TYPE2_BULLET_WIDTH, ALIEN_TYPE2_BULLET_HEIGHT = get_property(ENEMIES, "majorAlienLaserWidth"), \
                                                      get_property(ENEMIES, "majorAlienLaserHeight")
ALIEN_TYPE2_BULLET_IMAGE = pygame.image.load(get_property(ENEMIES, "majorAlienLaserImage"))
ALIEN_TYPE2_BULLET = pygame.transform.scale(ALIEN_TYPE2_BULLET_IMAGE,
                                            (ALIEN_TYPE2_BULLET_WIDTH, ALIEN_TYPE2_BULLET_HEIGHT)).convert_alpha()

ALIEN_TYPE1 = pygame.transform.scale(alien_image_picker(), (ALIEN_TYPE1_WIDTH, ALIEN_TYPE1_HEIGHT)).convert_alpha()
ALIEN_TYPE1_BULLET = pygame.transform.scale(ALIEN_TYPE1_BULLET_IMAGE,
                                            (ALIEN_TYPE1_BULLET_WIDTH, ALIEN_TYPE1_BULLET_HEIGHT)).convert_alpha()

ALIEN_TYPE2_VELOCITY = get_property(ENEMIES, "majorAlienVelocity")
ALIEN_TYPE2_IMAGE = pygame.transform.rotate(pygame.image.load(get_property(ENEMIES, "majorAlienImage")), 180)
ALIEN_TYPE2_WIDTH, ALIEN_TYPE2_HEIGHT = get_property(ENEMIES, "majorAlienWidth"), \
                                        get_property(ENEMIES, "majorAlienHeight")
ALIEN_TYPE2 = pygame.transform.rotate(
    pygame.transform.scale(ALIEN_TYPE2_IMAGE, (ALIEN_TYPE2_WIDTH, ALIEN_TYPE2_HEIGHT)).convert_alpha(), 180)
# --------
PREDATOR_VELOCITY = get_property(ENEMIES, "predatorVelocity")
PREDATOR_IMAGE = pygame.transform.rotate(pygame.image.load(get_property(ENEMIES, "predatorImage")), 180)
PREDATOR_WIDTH, PREDATOR_HEIGHT = get_property(ENEMIES, "predatorWidth"), get_property(ENEMIES, "predatorHeight")
PREDATOR = pygame.transform.scale(PREDATOR_IMAGE, (PREDATOR_WIDTH, PREDATOR_HEIGHT)).convert_alpha()

PREDATOR_BULLET_VELOCITY = get_property(ENEMIES, "predatorLaserVelocity")
PREDATOR_BULLET_IMAGE = pygame.image.load(get_property(ENEMIES, "predatorLaserImage"))
PREDATOR_BULLET_WIDTH, PREDATOR_BULLET_HEIGHT = get_property(ENEMIES, "predatorLaserWidth"), \
                                                get_property(ENEMIES, "predatorLaserHeight")
PREDATOR_BULLET = pygame.transform.scale(PREDATOR_BULLET_IMAGE,
                                         (PREDATOR_BULLET_WIDTH, PREDATOR_BULLET_HEIGHT)).convert_alpha()
# ------
SPACESHIP_VELOCITY = get_property(MAIN_CHARACTER, "spaceshipVelocity")
SPACESHIP_IMAGE = pygame.image.load(get_property(MAIN_CHARACTER, "spaceshipImage"))
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = get_property(MAIN_CHARACTER, "spaceshipWidth"), \
                                    get_property(MAIN_CHARACTER, "spaceshipHeight")
SPACESHIP = pygame.transform.scale(SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)).convert_alpha()
SPACESHIP_HP_WIDTH, SPACESHIP_HP_HEIGHT = 20, 20
SPACESHIP_HP_IMAGE = pygame.image.load(get_property(MAP_PROPS, "spaceshipHpImage"))
SPACESHIP_HP = pygame.transform.scale(SPACESHIP_HP_IMAGE, (SPACESHIP_HP_WIDTH, SPACESHIP_HP_HEIGHT)).convert_alpha()

BULLET_VELOCITY = get_property(MAIN_CHARACTER, "spaceshipLaserVelocity")
SPACESHIP_BULLET_IMAGE = pygame.image.load(get_property(MAIN_CHARACTER, "spaceshipLaserImage"))
BULLET_WIDTH, BULLET_HEIGHT = get_property(MAIN_CHARACTER, "spaceshipLaserWidth"), \
                              get_property(MAIN_CHARACTER, "spaceshipLaserHeight")
SPACESHIP_BULLET = pygame.transform.scale(SPACESHIP_BULLET_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT)).convert_alpha()
ALLIEN_BULLET = pygame.transform.rotate(
    pygame.transform.scale(SPACESHIP_BULLET_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT)).convert_alpha(), 180)

UFO_VELOCITY = get_property(ENEMIES, "ufoVelocity")
UFO_WIDTH, UFO_HEIGHT = get_property(ENEMIES, "ufoWidth"),  get_property(ENEMIES, "ufoHeight")
UFO_IMAGE = pygame.image.load(get_property(ENEMIES, "ufoImage"))
UFO = pygame.transform.scale(UFO_IMAGE, (UFO_WIDTH, UFO_HEIGHT)).convert_alpha()

UFO_BULLET_VELOCITY = get_property(ENEMIES, "ufoLaserVelocity")
UFO_BULLET_WIDTH, UFO_BULLET_HEIGHT = get_property(ENEMIES, "ufoLaserWidth"), get_property(ENEMIES, "ufoLaserHeight")
UFO_BULLET_IMAGE = pygame.image.load(get_property(ENEMIES, "ufoLaserImage"))
UFO_BULLET = pygame.transform.scale(UFO_BULLET_IMAGE, (UFO_BULLET_WIDTH, UFO_BULLET_HEIGHT)).convert_alpha()

BLUE_SPACE_IMAGE = pygame.image.load(get_property(MAP_PROPS, "blueBackground"))
BLACK_SPACE_IMAGE = pygame.image.load(get_property(MAP_PROPS, "blackBackground"))
DARK_PURPLE_SPACE_IMAGE = pygame.image.load(get_property(MAP_PROPS, "darkPurpleBackground"))
PURPLE_SPACE_IMAGE = pygame.image.load(get_property(MAP_PROPS, "purpleBackground"))
SPACE_MENU_IMAGE = pygame.image.load(get_property(MAP_PROPS, "spaceBackground"))

SPACE = pygame.transform.scale(background_picker(), (WIDTH, HEIGHT))

SMALL_METEOR_WIDTH, SMALL_METEOR_HEIGHT = get_property(ENEMIES, "smallMeteorWidth"), \
                                          get_property(ENEMIES, "smallMeteorHeight")
SMALL_METEOR_IMAGE = pygame.image.load(get_property(ENEMIES, "smallMeteorImage"))
SMALL_METEOR = pygame.transform.scale(SMALL_METEOR_IMAGE, (SMALL_METEOR_WIDTH, SMALL_METEOR_HEIGHT)).convert_alpha()

POWER_UP_BOOST_WIDTH, POWER_UP_BOOST_HEIGHT = get_property(MAP_PROPS, "powerUpBoostWidth"), \
                                              get_property(MAP_PROPS, "powerUpBoostHeight")
POWER_UP_BOOST_IMAGE = pygame.image.load(get_property(MAP_PROPS, "powerUpBoostImage"))
POWER_UP_BOOST = pygame.transform.scale(POWER_UP_BOOST_IMAGE, (POWER_UP_BOOST_WIDTH, POWER_UP_BOOST_HEIGHT))

BULLET_BOOST_IMAGE = pygame.image.load(get_property(MAP_PROPS, "laserBoostImage"))
BULLET_BOOST = pygame.transform.scale(BULLET_BOOST_IMAGE, (POWER_UP_BOOST_WIDTH, POWER_UP_BOOST_HEIGHT))

pygame.display.set_caption(GAME_CAPTION)
