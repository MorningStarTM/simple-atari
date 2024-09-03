from pathlib import Path
import os
root = os.getcwd()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

ASTEROID_COUNT = 90
ASTEROID_MIN_SIZE = 50
ASTEROID_MAX_SIZE = 100
BACKGROUND_COLOR = (59, 61, 64)
ASTEROID_SPEED = 4

JET_SPEED = 2
BRAKE_SPEED = 3

FPS = 60
ASTEROID_IMAGES = [Path(os.path.join(root, "navigator/assets/rock.png")), Path(os.path.join(root, "navigator/assets/asteroid.png"))]
IMAGE = Path(os.path.join(root, "navigator/assets/fighter-jet.png"))