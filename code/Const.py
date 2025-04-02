# C
import pygame

C_SILVER = (171, 167, 76)
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_RED = (235, 51, 36)
C_YELLOW = (235, 253, 85)
C_GREEN = (0, 128, 0)
C_PINK = (234, 54, 128)
C_PURPLE = (116, 27, 124)
C_ORANGE = (240, 134, 80)
C_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_DAMAGE =  {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Level2Bg7': 0,
    'Level2Bg8': 0,
    'Player1'  : 1,
    'Player1Shoot': 25,
    'Player2'  : 1,
    'Player2Shoot': 25,
    'Enemy1'   : 1,
    'Enemy1Shoot': 20,
    'Enemy2'   : 1,
    'Enemy2Shoot': 15,
    'Enemy3'   : 1,
    'Enemy3Shoot': 12,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'Level2Bg6': 999,
    'Level2Bg7': 999,
    'Level2Bg8': 999,
    'Player1'  : 300,
    'Player1Shoot': 1,
    'Player2'  : 300,
    'Player2Shoot': 1,
    'Enemy1'   : 100,
    'Enemy1Shoot': 1,
    'Enemy2'   : 150,
    'Enemy2Shoot': 1,
    'Enemy3'   : 200,
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
    'Level1Bg6'    : 6,
    'Level2Bg0'    : 0,
    'Level2Bg1'    : 1,
    'Level2Bg2'    : 2,
    'Level2Bg3'    : 3,
    'Level2Bg4'    : 4,
    'Level2Bg5'    : 5,
    'Level2Bg6'    : 6,
    'Level2Bg7'    : 7,
    'Level2Bg8'    : 8,
    'Player1'      : 3,
    'Player1Shoot' : 5,
    'Player2'      : 3,
    'Player2Shoot' : 3,
    'Enemy1'       : 1,
    'Enemy1Shoot'  : 5,
    'Enemy2'       : 1,
    'Enemy2Shoot'  : 2,
    'Enemy3'       : 1,
    'Enemy3Shoot'  : 2,
}

ENTITY_SCORE = {
    'Level1Bg0'    : 0,
    'Level1Bg1'    : 0,
    'Level1Bg2'    : 0,
    'Level1Bg3'    : 0,
    'Level1Bg4'    : 0,
    'Level1Bg5'    : 0,
    'Level1Bg6'    : 0,
    'Level2Bg0'    : 0,
    'Level2Bg1'    : 0,
    'Level2Bg2'    : 0,
    'Level2Bg3'    : 0,
    'Level2Bg4'    : 0,
    'Level2Bg5'    : 0,
    'Level2Bg6'    : 0,
    'Level2Bg7'    : 0,
    'Level2Bg8'    : 0,
    'Player1'      : 0,
    'Player1Shoot' : 0,
    'Player2'      : 0,
    'Player2Shoot' : 0,
    'Enemy1'       : 100,
    'Enemy1Shoot'  : 0,
    'Enemy2'       : 125,
    'Enemy2Shoot'  : 0,
    'Enemy3'       : 150,
    'Enemy3Shoot'  : 0,
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
SPAWN_TIME = 1000

# T
TIMEOUT_STEP = 100 # 100ms
TIMEOUT_LEVEL = 20000 #60 segundos

#  W
WIN_WIDTH = 1920
WIN_HEIGHT = 1080


