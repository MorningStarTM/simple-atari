import os
from pathlib import Path

root = os.getcwd()

WIDTH = 800
HEIGHT = 600


ASTEROID = Path(os.path.join(root, 'invader/assets/asteroid_2.png'))
JET = Path(os.path.join(root, 'invader/assets/spaceship.png'))
BULLET = Path(os.path.join(root, 'invader/assets/bullet.png'))
BG = Path(os.path.join(root, 'invader/assets/bg.jpg'))