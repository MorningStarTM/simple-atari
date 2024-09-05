import pygame
from .jet import Jet
from .asteroid import Asteroid
from .bullet import Bullet
from .const import *
import random

class GameScreen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.image.load(BG).convert()
        self.jet_group = pygame.sprite.Group()
        self.asteroid_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()

        # Initialize one jet
        self.jet1 = Jet(x=WIDTH // 2, y=HEIGHT - 30)
        self.jet_group.add(self.jet1)

        self.clock = pygame.time.Clock()
        self.max_asteroids = 10  # Limit the number of asteroids

    def create_asteroid(self):
        # Create a new asteroid if below the max limit
        if len(self.asteroid_group) < self.max_asteroids:
            x = random.randint(0, WIDTH)
            y = random.randint(-100, -40)
            asteroid = Asteroid(x, y)
            self.asteroid_group.add(asteroid)

    def update(self):
        self.jet_group.update()
        self.bullet_group.update()
        self.asteroid_group.update()

        # Bullet and asteroid collision
        for bullet in self.bullet_group:
            # Remove asteroid and bullet on collision
            collided_asteroids = pygame.sprite.spritecollide(bullet, self.asteroid_group, True, pygame.sprite.collide_mask)
            if collided_asteroids:
                bullet.kill()  # Remove the bullet after hitting an asteroid

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.jet_group.draw(self.screen)
        self.bullet_group.draw(self.screen)
        self.asteroid_group.draw(self.screen)
        pygame.display.flip()

    def check_collision(self):
        # Collision detection between jets and asteroids
        for jet in self.jet_group:
            if pygame.sprite.spritecollide(jet, self.asteroid_group, False, pygame.sprite.collide_mask):
                print("Jet collided with an asteroid!")
                return True
        return False

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.jet1.move_left()
        if keys[pygame.K_d]:
            self.jet1.move_right()
        if keys[pygame.K_SPACE]:
            self.jet1.shoot(self.bullet_group)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.handle_input()
            if self.check_collision():
                print("Game Over")
                running = False  # End the game loop on collision
            self.create_asteroid()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()
