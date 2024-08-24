import pygame
from screen import GameScreen
from const import *
from jet import Jet

def main():
    pygame.init()
    clock = pygame.time.Clock()
    game_screen = GameScreen()
    jet = Jet(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)  # Initialize jet at the bottom center

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            jet.rotate("left")
        if keys[pygame.K_RIGHT]:
            jet.rotate("right")
        if keys[pygame.K_DOWN]:
            jet.brake()

        # Calculate camera offset based on the jet's position
        offset_x = jet.rect.centerx - SCREEN_WIDTH // 2
        offset_y = jet.rect.centery - SCREEN_HEIGHT // 2

        # Update game state
        game_screen.update(offset_x, offset_y)
        jet.update()

        # Check for collisions
        if game_screen.check_collision(jet.rect):
            print("Collision Detected! Game Over.")
            running = False

        # Draw the player jet
        jet.draw(game_screen.screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()


clock = pygame.time.Clock()
jet = Jet(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Initialize the game screen
game_screen = GameScreen()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        jet.rotate(left=True)
    if keys[pygame.K_RIGHT]:
        jet.rotate(right=True)
    if keys[pygame.K_UP]:
        jet.move_forward()
    if keys[pygame.K_DOWN]:
        jet.move_backward()

    # Update the jet's position
    jet.move()

    # Calculate camera offset based on the jet's position
    jet_x, jet_y = jet.get_position()
    offset_x = jet_x - SCREEN_WIDTH // 2
    offset_y = jet_y - SCREEN_HEIGHT // 2

    # Update and draw the game screen with the camera offsets
    game_screen.update(offset_x, offset_y)

    # Draw the jet with the new camera offsets
    jet.draw(game_screen.screen, offset_x, offset_y)

    # Check for collisions
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()