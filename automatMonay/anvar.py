
import pygame
import random

# initialize Pygame
pygame.init()

# set up the screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

# set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# set up the font
font = pygame.font.Font(None, 36)

# set up the clock
clock = pygame.time.Clock()

# set up the car
car_size = 20
car_x = WIDTH // 2 - car_size // 2
car_y = HEIGHT // 2 - car_size // 2
car_speed = 5

# set up the oil
oil_size = 10
oil_x = random.randint(0, WIDTH - oil_size)
oil_y = random.randint(0, HEIGHT - oil_size)
oil_speed = 3

# set up the score
score = 0

# set up the game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_x -= car_speed
            elif event.key == pygame.K_RIGHT:
                car_x += car_speed
            elif event.key == pygame.K_UP:
                car_y -= car_speed
            elif event.key == pygame.K_DOWN:
                car_y += car_speed

    # move the oil
    oil_y += oil_speed
    if oil_y > HEIGHT:
        oil_x = random.randint(0, WIDTH - oil_size)
        oil_y = -oil_size
        score += 1

    # check for collision with oil
    if car_x < oil_x + oil_size and car_x + car_size > oil_x and car_y < oil_y + oil_size and car_y + car_size > oil_y:
        oil_x = random.randint(0, WIDTH - oil_size)
        oil_y = -oil_size
        score += 1

    # draw the screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, [oil_x, oil_y, oil_size, oil_size])
    pygame.draw.rect(screen, WHITE, [car_x, car_y, car_size, car_size])
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])
    pygame.display.flip()

    # set the frame rate
    clock.tick(60)

# quit Pygame
pygame.quit()