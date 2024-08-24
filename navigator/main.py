import pygame
from screen import GameScreen
from const import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    game_screen = GameScreen()
    #jet = Jet(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)  # Initialize jet at the bottom center

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle player input

        # Update game state
        game_screen.update()
        #jet.update()

        # Check for collisions

        # Draw the player jet
        #jet.draw(game_screen.screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
