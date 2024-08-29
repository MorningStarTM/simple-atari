import pygame
from screen import GameScreen
from const import FPS

def main():
    pygame.init()
    clock = pygame.time.Clock()
    game_screen = GameScreen()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_screen.bird.flap()

        # Update game state
        game_screen.update()

        # Check for collisions
        if game_screen.check_collision():
            print("Game Over!")
            running = False

        # Draw everything
        game_screen.draw()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
