import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1500, 844))
clock = pygame.time.Clock()
running = True
dt = 0

pygame.display.set_caption("Ball Buster!")
background = pygame.image.load("brick-wall-background-texture1.png")


# Medicine Ball
playerimg = pygame.image.load("medicine-ball.png")
playerx = 750
playery = 422
playerx_change = 0
playery_change = 0

def player(x,y):
    screen.blit(playerimg, (x, y))


# game loop
while running:
    # background
    screen.fill((0,0,0))
    #background image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame. K_LEFT:
                playerx_change = -5
            if event.key == pygame. K_RIGHT:
                playerx_change = 5
            if event.key == pygame. K_UP:
                playery_change = -5
            if event.key == pygame. K_DOWN:
                playery_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame. K_LEFT or event.key == pygame. K_RIGHT:
                playerx_change = 0
            if event.key == pygame. K_UP or event.key == pygame. K_DOWN:
                playery_change = 0


    playerx += playerx_change
    playery += playery_change

    if playerx <=0:
        playerx = 0
    elif playerx >= 1436:
        playerx = 1436

    if playery <=0:
        playery = 0
    elif playery >= 780:
        playery = 780
    player(playerx, playery)

    # THIS DISPLAYS YOUR WORK
    pygame.display.update()

    # This is used for frame rate for the game
    dt = clock.tick(60) / 1000

pygame.quit()
