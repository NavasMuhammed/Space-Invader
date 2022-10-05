import pygame
import random
import math
import time
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('enemy/ufo.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background/img_1.png')
running = True
count = 0
# mixer.music.load("title.mp3")
# mixer.music.play(-1)

playerImg = pygame.image.load('player/player.png')
playerX = 370
playerY = 480
playerX_change = 0

enemySpeed = 0.3
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
enemylink = 'enemy/ufo.png'
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(enemylink))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(30, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(0.01)


bulletImg = pygame.image.load('bullet/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.5
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def new_game():
    global playerx,playerY,playerX_change,playerY_change,enemyImg,enemyX,enemyY,enemyX_change,enemyY_change,num_of_enemies,bulletImg,bulletX,bulletY,bulletX_change,bulletY_change,bullet_state,score_value,font,textX,textY,over_font
    # playerImg = pygame.image.load('player.png')
    playerX = 370
    playerY = 480
    playerX_change = 0

    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 6
    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load(enemylink))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(30, 150))
        enemyX_change.append(0.3)
        enemyY_change.append(0.01)

    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 0.5
    bullet_state = "ready"

    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    textX = 10
    textY = 10

    over_font = pygame.font.Font('freesansbold.ttf', 64)
    game_loop()

def story_new_game(bg,en,enspeed):
    global playerx,playerY,playerX_change,playerY_change,enemySpeed,enemyImg,enemyX,enemyY,enemyX_change,enemyY_change,num_of_enemies,bulletImg,bulletX,bulletY,bulletX_change,bulletY_change,bullet_state,score_value,font,textX,textY,over_font
    # playerImg = pygame.image.load('player.png')
    playerX = 370
    playerY = 480
    playerX_change = 0
    enemySpeed = enspeed

    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 6
    background = pygame.image.load(bg)
    enemylink = en
    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load(enemylink))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(30, 150))
        enemyX_change.append(enemySpeed)
        enemyY_change.append(0.01)

    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 0.5
    bullet_state = "ready"

    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    textX = 10
    textY = 10

    over_font = pygame.font.Font('freesansbold.ttf', 64)
    story_mode_loop()

def game_over_text():
    green = (0,255,0)
    bright_green = (0,200,0)
    red = (255,0,0)
    bright_red = (200,0,0)
    over_text = over_font.render("~GAME OVER~", True, (200, 200, 255))
    screen.blit(over_text, (170, 250))
    button("Menu",150,450,100,100,green,bright_green,game_intro)
    button("Quit",350,450,100,100,red,bright_red,quitgame)

def game_won_text():
    green = (0,255,0)
    bright_green = (0,200,0)
    red = (255,0,0)
    bright_red = (200,0,0)
    white = (255,255,255)
    over_text = over_font.render("~GAME WON~", True, red)
    screen.blit(over_text, white)
    button("Menu",150,450,100,100,green,bright_green,game_intro)

def show_score(x, y):
    score = font.render("score: " + str(score_value), True, (200, 200, 255))
    screen.blit(score, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 32, y - 12))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(bulletX - enemyX, 2) + math.pow(bulletY - enemyY, 2))
    if distance <= 27:
        return True
    else:
        return False

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def changeBackground(backgrounds):
    global backgroundSelected
    global background
    backgroundSelected = False
    background = pygame.image.load(backgrounds)
    
def changeEnemy(image):
    global EnemySelected
    global enemylink
    EnemySelected = False
    enemylink  = image

def changePlayer(image):
    global PlayerSelected
    global playerImg
    PlayerSelected = False
    DEFAULT_IMAGE_SIZE = (80,80)
    player = pygame.image.load(image)
    playerImg = pygame.transform.scale(player, DEFAULT_IMAGE_SIZE)

def changeBullet(image):
    global BulletSelected
    global bulletImg
    BulletSelected = False
    DEFAULT_IMAGE_SIZE = (20,30)
    bullet = pygame.image.load(image)
    bulletImg = pygame.transform.scale(bullet, DEFAULT_IMAGE_SIZE)

def imagebutton(x, y, w, h, ic, ac, img,imglink, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x, y, w, h)
    on_button = rect.collidepoint(mouse)
    DEFAULT_IMAGE_SIZE = (w,h)
    image = pygame.transform.scale(img, DEFAULT_IMAGE_SIZE)
    pygame.draw.rect(screen, ic, rect)
    if on_button:
        if click[0] == 1 and action!= None:
            action(imglink)
    screen.blit(image, image.get_rect(center = rect.center)) 
        

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    gameDisplay = screen
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def selectBullet():
    global BulletSelected
    BulletSelected = True
    while BulletSelected:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_intro()
        green = (0,255,0)
        bright_green = (0,200,0)
        red = (255,0,0)
        bright_red = (200,0,0)
        black = (0,0,0)
        screen.fill(black)
        imagebutton(100, 100, 150, 150, green, bright_green, pygame.image.load('bullet/bullet.png'),'bullet/bullet.png',changeBullet)
        imagebutton(300, 100, 150, 150, green, bright_green, pygame.image.load('bullet/bullet2.png'),'bullet/bullet2.png',changeBullet)
        pygame.display.update()

def selectEnemy():
    global EnemySelected
    EnemySelected = True
    while EnemySelected:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_intro()
        green = (0,255,0)
        bright_green = (0,200,0)
        red = (255,0,0)
        bright_red = (200,0,0)
        black = (0,0,0)
        screen.fill(black)
        imagebutton(100, 100, 150, 150, green, bright_green, pygame.image.load('enemy/enemy.png'),'enemy/enemy.png',changeEnemy)
        imagebutton(300, 100, 150, 150, green, bright_green, pygame.image.load('enemy/ufo.png'),'enemy/ufo.png',changeEnemy)
        pygame.display.update()

def selectPlayer():
    global PlayerSelected
    PlayerSelected = True
    while PlayerSelected:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_intro()
        green = (0,255,0)
        bright_green = (0,200,0)
        red = (255,0,0)
        bright_red = (200,0,0)
        black = (0,0,0)
        screen.fill(black)
        imagebutton(100, 100, 150, 150, green, bright_green, pygame.image.load('player/player.png'),'player/player.png',changePlayer)
        imagebutton(300, 100, 150, 150, green, bright_green, pygame.image.load('player/player2.png'),'player/player2.png',changePlayer)
        imagebutton(500, 100, 150, 150, green, bright_green, pygame.image.load('player/player3.png'),'player/player3.png',changePlayer)
        pygame.display.update()

def selectBackground():
    global backgroundSelected
    backgroundSelected = True
    while backgroundSelected:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_intro()
        green = (0,255,0)
        bright_green = (0,200,0)
        red = (255,0,0)
        bright_red = (200,0,0)
        black = (0,0,0)
        screen.fill(black)
        imagebutton(100, 100, 150, 150, green, bright_green, pygame.image.load('background/img_1.png'),'background/img_1.png',changeBackground)
        imagebutton(300, 100, 150, 150, green, bright_green, pygame.image.load('background/img.png'),'background/img.png',changeBackground)
        pygame.display.update()

def game_intro():

    intro = True
    display_width = 800
    display_height = 600
    white = (255,255,255)
    red = (255,0,0)
    green = (0,255,0)
    bright_green = (0,200,0)
    bright_red = (200,0,0)
    yellow = (255,255,0)
    global screen
    gameDisplay = screen
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(yellow)
        largeText = pygame.font.Font('freesansbold.ttf',95)
        TextSurf, TextRect = text_objects("Space Invaders", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("FREEPLAY",150,450,100,50,green,bright_green,new_game)
        button("STORY MODE",150,550,100,50,green,bright_green,story_mode_loop)
        button("GO!",280,450,100,50,green,bright_green,game_loop)
        button("change Arena",390,450,130,50,green,bright_green,selectBackground)
        button("change Player",390,550,130,50,green,bright_green,selectPlayer)
        button("change Enemy",280,550,130,50,green,bright_green,selectEnemy)
        button("change Bullet",520,550,130,50,green,bright_green,selectBullet)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        # clock.tick(15)
        # intro = False

def game_loop():
    global playerX,playerY,playerX_change,playerY_change,bulletX,bulletY,bulletX_change,bulletY_change,bullet_state,score_value,enemyX,enemyY,enemyX_change,enemyY_change
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
        
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    playerX_change = -0.3
                if event.key == pygame.K_RIGHT:
                    playerX_change = 0.3
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletSound = mixer.Sound("shoot.wav")
                        bulletSound.play()
                        bulletX = playerX
                        fire_bullet(playerX, playerY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        if playerX >= 706:
            playerX = 706

        for i in range(num_of_enemies):
            if enemyY[i] > 180:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break
            enemyX[i] += enemyX_change[i]
            enemyY[i] += 1.25*enemyY_change[i]
            if enemyX[i] <= 0:
                enemyY[i] += enemyY_change[i]
                enemyX_change[i] = 0.3
            if enemyX[i] >= 736:
                enemyY[i] += enemyY_change[i]
                enemyX_change[i] = -0.3
            if enemyY[i] >= 600:
                enemyY[i] = random.randint(30, 150)

            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound("explosion.mp3")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(30, 150)

            enemy(enemyX[i], enemyY[i], i)

        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            screen.blit(bulletImg, (bulletX + 32, bulletY - 12))
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()
        # global keys
        
def story_mode_loop():
    global playerX,playerY,count,playerX_change,enemySpeed,playerY_change,bulletX,bulletY,bulletX_change,bulletY_change,bullet_state,score_value,enemyX,enemyY,enemyX_change,enemyY_change
    running = True
    count=count + 1
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
        
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    playerX_change = -0.3
                if event.key == pygame.K_RIGHT:
                    playerX_change = 0.3
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletSound = mixer.Sound("shoot.wav")
                        bulletSound.play()
                        bulletX = playerX
                        fire_bullet(playerX, playerY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        if playerX >= 706:
            playerX = 706

        for i in range(num_of_enemies):
            if enemyY[i] > 450:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break
            enemyX[i] += enemyX_change[i]
            enemyY[i] += 1.25*enemyY_change[i]
            if enemyX[i] <= 0:
                enemyY[i] += enemyY_change[i]
                enemyX_change[i] = enemySpeed
            if enemyX[i] >= 736:
                enemyY[i] += enemyY_change[i]
                enemyX_change[i] = -(enemySpeed)
            if enemyY[i] >= 600:
                enemyY[i] = random.randint(30, 150)

            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound("explosion.mp3")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(30, 150)

            enemy(enemyX[i], enemyY[i], i)

        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            screen.blit(bulletImg, (bulletX + 32, bulletY - 12))
            bulletY -= bulletY_change
        
        if score_value >= 5 and count ==1:
            running = False
            story_new_game('background/img.png','enemy/enemy.png',0.5)

        if score_value >= 5 and count ==2:
            # running = False
            game_won_text()
        

        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()
        # global keys

game_intro()
# game_loop()
pygame.quit()
