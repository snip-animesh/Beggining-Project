import pygame, random, math
from pygame import mixer
import button

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))
# Title and icon
pygame.display.set_caption("Ani'Space Invaders")
icon = pygame.image.load('data/ufo.png')
pygame.display.set_icon(icon)

# score and High Score
score_value = 0
high_score_value = 0
# score font
font = pygame.font.Font('data/samuf.ttf', 32)
textX = 10
textY = 10

# Game Over font
over_font = pygame.font.Font('data/samuf.ttf', 64)
# Background Image
background = pygame.image.load("data/background.jpg")

# clock
clock=pygame.time.Clock()

# Background Music
mixer.music.load('data/background.wav')
mixer.music.play(-1)

# Player
playerImg = pygame.image.load('data/player.png')
playerX = 370
playerY = 500
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemY = []
enemyX_change = []
enemY_change = []
num_of_enemies = 4
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('data/enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemY.append(random.randint(70, 150))
    enemyX_change.append(0.5)
    enemY_change.append(30)

# Ready- You can't see the bullet
# Fired- Bullet is on the screen
# Bullet
bulletImg = pygame.image.load('data/bullet.png')
bulletX = 0
bulletY = 480
# bulletX_change = 0
bulletY_change = 1.5
bullet_state = "ready"


def game_over_text(x):
    if x:
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (300, 150))


def showScore(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
    high_score = font.render("Highest Score : " + str(high_score_value), True, (255, 255, 255))
    screen.blit(high_score, (620, 10))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    # x+16 and y+10 is just to create an illusion that bullet is coming from the center and
    # of the spaceship


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def isCollision(enemyX, enemY, bulletX, bulletY):
    distance = math.dist([enemyX, enemY], [bulletX, bulletY])
    if distance < 32:
        return True
    else:
        return False


running = True
x = 1
show = True
while running:
    screen.fill((128, 0, 0))
    screen.blit(background, (0, 0))
    # playerX+=0.1
    clock.tick(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Checking for keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change += 1
            if event.key == pygame.K_LEFT:
                playerX_change -= 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Get the current x coordinate of bullet
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    # Bullet sound
                    bulletSound = mixer.Sound('data/laser.wav')
                    bulletSound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change

    # Bounding player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)

    # Movement enemy
    for i in range(num_of_enemies):
        # Making Game Over (440)
        if enemY[i] > 440:
            # Move all the enemies out of the screen
            for j in range(num_of_enemies):
                enemY[j] = 2000
            game_over_text(x)
            # Create play again and exit button instances
            start_btn = button.Button(325, 225, button.start_img, 0.4)
            # exit_btn = button.Button(370, 280, button.exit_img, 0.4)
            exit_btn = button.Button(325, 290, button.exit_img, 0.4)

            if start_btn.draw(screen, show):
                # x=0 to hide game over text
                x = 0
                game_over_text(x)
                # Making show to False to hide exit button
                show = False
                for j in range(num_of_enemies):
                    enemY[j] = random.randint(70, 150)
                    # Making x=1 and show =True to show the buttons again and display game over text
                    # Make the score to 0 again
                    x = 1
                    show = True
                    score_value = 0
            if exit_btn.draw(screen, show):
                running = False
            break
        # Increasing enemy speed based on Score
        if score_value < 16:
            if enemyX[i] <= 0:
                enemyX_change[i] = 0.5
                enemY[i] += enemY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -0.5
                enemY[i] += enemY_change[i]
        elif score_value < 26:
            if enemyX[i] <= 0:
                enemyX_change[i] = 0.8
                enemY[i] += enemY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -0.8
                enemY[i] += enemY_change[i]
        elif score_value < 36:
            if enemyX[i] <= 0:
                enemyX_change[i] = 1.2
                enemY[i] += enemY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -1.2
                enemY[i] += enemY_change[i]
        else:
            if enemyX[i] <= 0:
                enemyX_change[i] = 2
                enemY[i] += enemY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -2
                enemY[i] += enemY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemY[i], bulletX, bulletY)
        if collision:
            explotionSound = mixer.Sound('data/explosion.wav')
            explotionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            # Update high_score value
            if score_value > high_score_value:
                high_score_value = score_value
            # After hitting enemy lets respone it
            enemyX[i] = random.randint(0, 735)
            enemY[i] = random.randint(70, 150)
            # print(score_)
        enemyX[i] += enemyX_change[i]
        enemy(enemyX[i], enemY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    showScore(textX, textY)
    pygame.display.update()

pygame.quit()