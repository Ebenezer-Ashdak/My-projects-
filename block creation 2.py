import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Block Builder")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
GREEN = (50, 200, 50)
RED = (200, 50, 50)
BLACK = (0, 0, 0)

# Grid settings
TILE_SIZE = 40
grid = {}

# Player settings
player_size = 30
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

clock = pygame.time.Clock()

# Game loop
while True:
    clock.tick(60)
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Mouse click to place/remove blocks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            grid_x = mx // TILE_SIZE
            grid_y = my // TILE_SIZE

            if event.button == 1:  # Left click = place block
                grid[(grid_x, grid_y)] = BLUE

            if event.button == 3:  # Right click = remove block
                if (grid_x, grid_y) in grid:
                    del grid[(grid_x, grid_y)]

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

    # Draw blocks
    for (gx, gy), color in grid.items():
        pygame.draw.rect(screen, color,
                         (gx * TILE_SIZE, gy * TILE_SIZE,
                          TILE_SIZE, TILE_SIZE))

    # Draw player
    pygame.draw.rect(screen, GREEN,
                     (player_x, player_y, player_size, player_size))

    pygame.display.flip()