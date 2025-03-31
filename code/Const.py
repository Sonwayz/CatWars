# C
import pygame

COLOR_SILVER = (171, 167, 76)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (235, 51, 36)
COLOR_YELLOW = (235, 253, 85)
COLOR_GREEN = (55, 126, 71)
COLOR_PINK = (234, 54, 128)
COLOR_PURPLE = (116, 27, 124)
COLOR_ORANGE = (240, 134, 80)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Player1'  : 300,
    'Player1Shoot': 1,
    'Player2'  : 300,
    'Player2Shoot': 1,
    'Enemy1'   : 50,
    'Enemy1Shoot': 1,
    'Enemy2'   : 60,
    'Enemy2Shoot': 1,
    'Enemy3'   : 70,
    'Enemy3Shoot': 1,
}

ENTITY_SHOOT_DELAY = {
    'Player1' : 20,
    'Player2' : 15,
    'Enemy1'  : 100,
    'Enemy2'  : 200,
    'Enemy3'  : 250,
}

ENTITY_SPEED = {
    'Level1Bg0'    : 0,
    'Level1Bg1'    : 1,
    'Level1Bg2'    : 2,
    'Level1Bg3'    : 3,
    'Level1Bg4'    : 4,
    'Level1Bg5'    : 5,
    'Player1'      : 3,
    'Player1Shoot' : 1,
    'Player2'      : 3,
    'Player2Shoot' : 3,
    'Enemy1'       : 1,
    'Enemy1Shoot'  : 5,
    'Enemy2'       : 1,
    'Enemy2Shoot'  : 2,
    'Enemy3'       : 1,
    'Enemy3Shoot'  : 2,
}

# M
MENU_OPTION = ('NEW GAME',
               'COOP',
               'VERSUS',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP =    {'Player1': pygame.K_w,
                   'Player2':pygame.K_UP}
PLAYER_KEY_DOWN =  {'Player1': pygame.K_s,
                   'Player2':pygame.K_DOWN}
PLAYER_KEY_LEFT =  {'Player1': pygame.K_a,
                   'Player2':pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_d,
                   'Player2':pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_LSHIFT,
                   'Player2':pygame.K_RSHIFT}

# S
SPAWN_TIME = 4000

#  W
WIN_WIDTH = 1920
WIN_HEIGHT = 1080


