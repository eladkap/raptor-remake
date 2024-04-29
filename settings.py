"""
Screen resolutions:
- 800 x 600
- 1024 x 768
- 1280 x 720
- 1366 x 768
- 1600 x 900
- 1920 x 1080
"""
SCREEN_RES = [1600, 900]
SCREEN_TITLE = 'Raptor'
RESIZABLE = True

COLORS = {
    'BLACK': [0, 0, 0],
    'BLACK_LIGHT': [20, 20, 20],
    'GRAY0': [50, 50, 50],
    'GRAY1': [100, 100, 100],
    'GRAY2': [150, 150, 150],
    'GRAY3': [200, 200, 200],
    'RED': [220, 0, 0],
    'ORANGE': [250, 150, 50],
    'PINK': [250, 100, 150],
    'BROWN': [200, 200, 0],
    'YELLOW': [255, 255, 0],
    'GREEN': [0, 100, 0],
    'AQUA': [100, 255, 255],
    'BLUE': [0, 0, 250],
    'NAVY': [0, 0, 128],
    'DARK_BLUE': [0, 0, 64]
}

AIRCRAFT_DIAMETER = 72

# Raptor settings

RAPTOR_ALTITUDE = 100
RAPTOR_VELOCITY = [0, 0]
RAPTOR_HEALTH = 1000
RAPTOR_SHIELD = 500
RAPTOR_MOVEMENT = 5

# Enemy settings
ENEMY_VELOCITY = [0, -3]

SCALING = 0.15

BG_IMAGES = {
    'bg_space1': 'assets/images/background/bg_space1.png',
    'bg_space2': 'assets/images/background/bg_space2.png',
    'bg_space3': 'assets/images/background/bg_space3.png'
}

SPRITES = {
    'raptor': 'assets/images/sprites/raptor/raptor.png',
    'asteroid': 'assets/images/sprites/enemies/asteroid.png',
    'enemy1': 'assets/images/sprites/enemies/enemy_1.png',
    'enemy2': 'assets/images/sprites/enemies/enemy_2.png',
    'enemy3': 'assets/images/sprites/enemies/enemy_3.png',
    'enemy4': 'assets/images/sprites/enemies/enemy_4.png'
}
