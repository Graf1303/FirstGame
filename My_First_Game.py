import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
black = (0, 0, 0)
vel = 8
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # background
    screen.fill("pink")

    # our character
    player = pygame.draw.circle(screen, "blue", player_pos, 40)

    # Border
    border = pygame.draw.rect(screen, black, (0, 0, 1280, 720), 1)

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= vel
    if keys[pygame.K_s]:
        player_pos.y += vel
    if keys[pygame.K_a]:
        player_pos.x -= vel
    if keys[pygame.K_d]:
        player_pos.x += vel

    # THIS DISPLAYS YOUR WORK
    pygame.display.flip()

    # This is used for frame rate for the game
    dt = clock.tick(60) / 1000

pygame.quit()
