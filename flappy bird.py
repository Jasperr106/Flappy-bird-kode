import pygame
import sys
import random

pygame.init()

#basic variables setting up the game
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Flappy bird")

clock = pygame.time.Clock()

# score

score = 0

#variables for jumping and falling mechanics

hop_height = 13
vel = hop_height
jumping = False
falling = True
fall = 2.3

#starting game at pause menu
game_paused = True

#making so it begins by falling
start_hop = 1000

#loading images and getting rects from them
flappy_bird = pygame.image.load("filer/flappy_bird2.png")
flappy_bird = pygame.transform.scale(flappy_bird, (70,50))
flappy_bird_fall = pygame.transform.rotate(flappy_bird, 330)
flappy_bird_hop = pygame.transform.rotate(flappy_bird, 30)

background = pygame.image.load("filer/background.png")
background = pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))

flappy_birdRect = flappy_bird.get_rect()
flappy_birdRect.center = (225,200)

flappy_bird_hopRect = flappy_bird.get_rect()
flappy_bird_hopRect.center = (225,200)

flappy_birdRect = flappy_bird.get_rect()
flappy_birdRect.center = (225,200)

# getting font and setting text(s), creating a function to edit texts later
font = pygame.font.SysFont("Arial",20)

text_l1 = "Welcome to flappy bird!"
text_l2 = "Keep your bird away from the pipes by hopping (space)"
text_l3 = 'Press "1" to play!'

def render_text(l1, l2, l3):
    pause_text_l1 = font.render(l1, True, "black")
    pause_text_l1Rect =pause_text_l1.get_rect()
    pause_text_l1Rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50)
    SCREEN.blit(pause_text_l1,pause_text_l1Rect)

    pause_text_l2 = font.render(l2, True, "black")
    pause_text_l2Rect =pause_text_l2.get_rect()
    pause_text_l2Rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    SCREEN.blit(pause_text_l2,pause_text_l2Rect)

    pause_text_l3 = font.render(l3, True, "black")
    pause_text_l3Rect =pause_text_l3.get_rect()
    pause_text_l3Rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50)
    SCREEN.blit(pause_text_l3,pause_text_l3Rect)

def write_score(score):
    score_font = pygame.font.SysFont("Arial", 45)
    score_text = score_font.render(score,True,"black")
    scoreRect = score_text.get_rect()
    scoreRect.center = (0 +80, 0+ 40)
    SCREEN.blit(score_text,scoreRect)
    
def update_score(score, birdRect, pillar_x, pillar2_x):
    if birdRect.x == pillar_x + 50:
        score += 1
        print("score")
    if birdRect.x == pillar2_x + 60 or birdRect.x == pillar2_x + 61:
        score += 1
        print("score")
    else:
        pass
    return score

#getting random variables for pillars, variation
def pillar_var():
    global top_pillar_height
    global bottom_pillar_height

    while True:
        top_pillar_height = random.randint(20, SCREEN_HEIGHT - SCREEN_HEIGHT/2 + 70)
        bottom_pillar_height = SCREEN_HEIGHT - top_pillar_height - 125
        if SCREEN_HEIGHT - top_pillar_height - bottom_pillar_height == 125:
            break
        else:
            pass

#second pillar
def pillar2_var():
    global top_pillar_height_2
    global bottom_pillar_height_2

    while True:
        top_pillar_height_2 = random.randint(20, SCREEN_HEIGHT - SCREEN_HEIGHT / 2 + 70)
        bottom_pillar_height_2 = SCREEN_HEIGHT - top_pillar_height - 125
        if SCREEN_HEIGHT - top_pillar_height_2 - bottom_pillar_height_2 == 125:
            break
        else:
            pass

#running functions so we start with values
pillar_var()
pillar2_var()

#setting start point for first pilalr
top_pillar_x = SCREEN_WIDTH - 100
bottom_pillar_x = SCREEN_WIDTH - 100

#function to draw pillars
def draw_pillar(topheight, bottomheight):
    global top_pillar_x
    global bottom_pillar_x

    pygame.draw.rect(SCREEN,(0,255,0), (top_pillar_x, 0, 50, topheight))
    pygame.draw.rect(SCREEN,(0,255,0), (bottom_pillar_x, SCREEN_HEIGHT - bottomheight, 50, bottomheight))

    top_pillar_x -= 2
    bottom_pillar_x -= 2

#start ppoint second pillar
top_pillar_x_2 = SCREEN_WIDTH + 225
bottom_pillar_x_2 = SCREEN_WIDTH + 225

def draw_pillar2(topheight, bottomheight):
    global top_pillar_x_2
    global bottom_pillar_x_2

    pygame.draw.rect(SCREEN,(0,255,0), (top_pillar_x_2, 0, 50, topheight))
    pygame.draw.rect(SCREEN,(0,255,0), (bottom_pillar_x_2,SCREEN_HEIGHT - bottomheight, 50, bottomheight))

    top_pillar_x_2 -= 2
    bottom_pillar_x_2 -= 2
    
#drawing bird
def draw_bird(bird, birdRect):
    pygame.draw.rect(bird,(255,255,255), birdRect)
    SCREEN.blit(bird,birdRect)

#checking for collisions, if collision pauses and changes puase text
def check_collision(birdRect, top_pillar_height, bottom_pillar_height, top_pillar_x):
    global game_paused
    global text_l1
    global text_l2
    global text_l3

    text_l1 = "You lost!"
    text_l2 = 'Press "1" to play again!'
    text_l3 = ""

    if birdRect.x + flappy_bird.get_width() in range(int(top_pillar_x), int(top_pillar_x + 100)):
        if top_pillar_height -20 > birdRect.y:
            render_text(text_l1,text_l2,text_l3)
            game_paused = True

        if birdRect.y > SCREEN_HEIGHT - bottom_pillar_height - 60:            
            render_text(text_l1,text_l2,text_l3)
            game_paused = True

run_game = True

#main game loop
while run_game:
    clock.tick(60)

    key = pygame.key.get_pressed()

#events - pause and space to jump
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_hop = flappy_birdRect.y
                jumping = True
        
    if not jumping:
        falling = True

#pause menu loop
    if game_paused:

        pillar_var()
        pillar2_var

        #setting variables back so we can reset

        top_pillar_x = SCREEN_WIDTH - 100
        bottom_pillar_x = SCREEN_WIDTH - 100
        top_pillar_x_2 = top_pillar_x + 325
        bottom_pillar_x_2 = bottom_pillar_x + 325
        flappy_birdRect.y = SCREEN_HEIGHT /2

        clock.tick(60)
        SCREEN.blit(background,(0,0))
        render_text(text_l1,text_l2,text_l3)


        key = pygame.key.get_pressed()
        if key[pygame.K_1]:
            game_paused = False
 
        pygame.display.update()

#main gameloop
    else:
        SCREEN.blit(background, (0,0))

        if 1> top_pillar_x:
            pillar_var()
            top_pillar_x = SCREEN_WIDTH
            bottom_pillar_x = SCREEN_WIDTH
        
        if 1> top_pillar_x_2:
            pillar2_var
            top_pillar_x_2 = SCREEN_WIDTH 
            bottom_pillar_x_2 = SCREEN_WIDTH

        if jumping:
            fall = 2.3
            falling = False
            flappy_birdRect.y -= vel
            vel -= 2.3 #gravity
            if vel < -7:
                jumping = False
                vel = hop_height
            
        if falling:
            jumping = False
            fall += 0.07
            if flappy_birdRect.y > SCREEN_HEIGHT - 5 - flappy_bird.get_height():
                flappy_birdRect.y = SCREEN_HEIGHT - flappy_bird.get_height() 

            flappy_birdRect.y += fall


        if top_pillar_x_2 > top_pillar_x:
            check_collision(flappy_birdRect, top_pillar_height, bottom_pillar_height, top_pillar_x)

        elif top_pillar_x > top_pillar_x_2:
            check_collision(flappy_birdRect, top_pillar_height_2, bottom_pillar_height_2, top_pillar_x_2)

        if flappy_birdRect.y > start_hop:
            if 20 > flappy_birdRect.y:
                draw_bird(flappy_bird, flappy_birdRect)
            draw_bird(flappy_bird_fall,flappy_birdRect)

        elif start_hop + 300 > flappy_birdRect.y:
            draw_bird(flappy_bird_hop,flappy_birdRect)
        
        draw_pillar(top_pillar_height, bottom_pillar_height)

        draw_pillar2(top_pillar_height_2,bottom_pillar_height_2)

        score = update_score(score,flappy_birdRect, top_pillar_x, top_pillar_x_2)

        write_score(str(score))

        pygame.display.update()


