import os
from pathlib import Path

root = os.getcwd()

WIDTH = 800
HEIGHT = 600


ASTEROID = Path(os.path.join(root, 'assets/asteroid_2.png'))
JET = Path(os.path.join(root, './assets/spaceship.png'))
BULLET = Path(os.path.join(root, './assets/bullet.png'))
BG = Path(os.path.join(root, './assets/bg.jpg'))