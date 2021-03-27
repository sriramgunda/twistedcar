import pygame
import random
import time
import datetime

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Twist Car")
icon = pygame.image.load('icon-car.png')
pygame.display.set_icon(icon)


#Fonts
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 24)
game_over_text = pygame.font.Font('freesansbold.ttf', 40)

textX = 10
textY = 10


def show_text(fontsize, txt, color, position):
    font = pygame.font.Font('freesansbold.ttf', fontsize)
    screen.blit(font.render(txt, True, color), position)


def show_score(x,y):
    show_text(24, "Score : "+ str(score_value), (255,255,255), (x,y))
    #score = font.render("Score : "+ str(score_value), True, (255,255,255))
    #screen.blit(score, (x,y))


def game_over():
    show_text(40, "GAME OVER", (255,0,255), (280,250))
    #g_over = game_over_text.render("GAME OVER", True, (255,0,255))
    #screen.blit(g_over, (280,250))


#Car Player
carimg = pygame.image.load('player-car.png')
carX = 320
carY = 300
carX_change = 0

def player(x, y):
    screen.blit(carimg, (x, y))


#Star Coins
coinimg = pygame.image.load('star_32px.png')


def star(x, y):
    screen.blit(coinimg, (x, y))


def star_coins():
    starY = 340
    starX = random.random() * 750
    star(starX, starY)


running = True
starX = 10
starY = 340

while running:
    now = datetime.datetime.now()
    now_seconds = int(now.strftime("%S"))
    screen.fill((21, 21, 21))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('quit')
            running = False

        if event.type == pygame.KEYDOWN:
            print('down')
            if event.key == pygame.K_LEFT:
                print('left')
                carX_change = 0.5
            if event.key == pygame.K_RIGHT:
                print('right')
                carX_change = -0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print('up')
                carX_change = carX_change

    carX += carX_change
    if carX < 0:
        carX = 0;
        game_over()
    if carX >= 672:
        carX = 672
        game_over()


    if carX == round(starX) or carX == round(starX) - 128:
        score_value += 1
        starRandX = random.random() * 750
        starX = starRandX
        starRandX = starX
        #star(starX, starY)

    
    player(carX, carY)
    
    
    if now_seconds % 3 == 0:
        starRandX = random.random() * 750
        starX = starRandX
        starRandX = starX
    else:
        star(starX, starY)

    show_score(textX, textY)
    
    pygame.display.update()

pygame.quit()


