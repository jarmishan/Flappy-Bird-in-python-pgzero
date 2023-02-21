import pgzrun
from random import *

HEIGHT= 500
WIDTH = 900

alive = True
start = False
score = 0

bird = Actor("flappybird_bird (1)")
bird_flying = Actor("flappybird_bird (2)")
bird.x = WIDTH / 4
bird.y = HEIGHT / 2
fly = False
delay = 0

bg1 = Actor("flappybird_background")
bg2 = Actor("flappybird_background")
bg2.x = -450

pipe = [Actor("flappybird_pipe")]
toppipes = [Actor("flappybird_pipe")]
pipe[-1].x = 800
pipe[-1].y = randrange(400,700,50)
toppipes[-1].x = 800 
toppipes[-1].y = pipe[-1].y - 555 

def update():
    global alive 
    global start
    global fly
    global delay
    global score
    bird_flying.x = bird.x 
    bird_flying.y = bird.y
    bg1.x += 1          # goofy ahh code
    bg2.x += 1  
    if bg1.x == 450:
        bg2.x = -450
    if bg2.x == 450:
        bg1.x = -450    # end of goofy ahh code
    if start:
        if alive:
            for bottompipe in pipe:
                bottompipe.x -= 2.5
                if bird.colliderect(bottompipe):
                    alive = False
                elif bird.x == bottompipe.x:
                    score += 1
                if bottompipe.x == -20:
                    pipe.remove(bottompipe)
            for toppipe in toppipes:
                toppipe.x -= 2.5
                if bird.colliderect(toppipe):
                    alive = False
                if bird.y < toppipe.y and bird.x == toppipe.x:
                    print(bird.y)
                    print(toppipe.y)
                    alive = False
                    if toppipe.x == -20:
                        toppipes.remove(toppipe)
            if bottompipe.x == 750:
                pipe.append(Actor("flappybird_pipe"))
                pipe[-1].x = 1000
                pipe[-1].y = randrange(400,700,50)
                toppipes.append(Actor("flappybird_pipe"))
                toppipes[-1].x = 1000
                toppipes[-1].y = pipe[-1].y - 555
            bird.y += 5
        if bird.y >= 515:
            alive = False
            bird.y = -100
    delay += 1
    if delay == 20:
        fly= False
        delay = 0
        
def on_key_down(key):
    global alive
    global start
    global speed
    global fly
    if alive:
        if key == keys.SPACE:
            start = True
            fly = True
            animate(bird, tween = 'accel_decel', duration = 0.3, pos = (bird.x,bird.y - 75))

def on_mouse_down():
    global alive
    global start
    global speed
    global fly
    if alive:
        start = True
        fly = True
        animate(bird, tween = 'accel_decel', duration = 0.3, pos = (bird.x,bird.y - 75))

def draw():
    global alive
    global fly
    global score 
    global alive
    screen.clear()
    bg1.draw()
    bg2.draw()
    if alive:
        for bottompipe in pipe:
            bottompipe.draw()
        for toppipe in toppipes:
            toppipe.angle = 180                                                 
            toppipe.draw()
        if fly:
            bird_flying.draw()
        elif fly == False:
            bird.draw()
    elif alive == False:
        screen.draw.text("YOU DIED",(WIDTH/2-175,225), color="black",fontsize = 100)
    screen.draw.text(str(score),(WIDTH/69,10), color="white",fontsize = 100)

pgzrun.go()

# from random import *
# import pygame
# import math
# import sys
# import os
 
# pygame.init()

# WHITE = (255,255,255)
# BLACK = (0,0,0)
# RED = (255,0,0)
# GREEN = (0,255,0)
# BLUE = (0,0,255)

# fps = 30

# vamp_width, vamp_height = 50,122
# WIDTH,HEIGHT = 1000,600
# screen = pygame.display.set_mode((WIDTH,HEIGHT))
# pygame.display.set_caption("vampire game")


# class vampire:
#     def __init__(self, x, y):
#         pass


# class player:
#     def __init__(self, x, y):
#         pass
    
# stepindex = 0

# GRASS = pygame.image.load(os.path.join("images", "dirt.png"))
# WATER = pygame.image.load(os.path.join("images", "water.png"))

# #"____", 
# tilemap = [
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     [],
#     ["GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS",],
#     ["GRASS", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "GRASS",],
#     ["GRASS", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "GRASS",],
#     ["GRASS", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "GRASS",],
#     ["GRASS", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "GRASS",],
#     ["GRASS", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "_____", "GRASS",],
#     ["GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS", "GRASS",],
#     []
#     ]
# player_right = [pygame.transform.scale(pygame.image.load(os.path.join('Player', 'R' +str (i) +'.png')), (128,128)) for i in range(1,9)]
# player_left = [pygame.transform.scale(pygame.image.load(os.path.join('Player', 'L' +str (i) +'.png')), (128,128)) for i in range(1,9)]  



# x = 336
# y = 325
# vel = 10
# left = True
# right = False
# num = 0
# jump = False
# yes = None
# jump_cooldown = 0
# def move():
#         global blocked
#         global left
#         global right
#         global stepindex
#         global vel
#         global x
#         global y
#         global jump
#         global tilerect
#         global playerA
#         global yes
#         global jump_cooldown
#         global dx

#         player = pygame.Rect(x ,y, 128, 128)
#         rightblocked = False
#         leftblocked = False
#         for i in tilerect: 
#             if i.collidepoint(player.centerx ,player.bottom - 1):
#                 y = i.y - 124
#                 if keys[pygame.K_SPACE] and jump_cooldown > 4 :
#                     vel = -18
#                     jump_cooldown = -18
#                     jump = True

#                 if jump != True:
#                     vel = 0

#             if i.collidepoint(player.centerx ,player.top + 1):
#                 y += 5
#                 vel = 0

#             if i.collidepoint(player.centerx + 64, player.centery + 32):
#                 leftblocked = True 

#             elif i.collidepoint(player.centerx - 64, player.centery + 32):
#                 rightblocked = True




#         if keys[pygame.K_a]:
#             if not jump:
#                 screen.blit(player_left[stepindex], (x, y))
#             else: 
#                 screen.blit(player_left[0], (x,y))

#             left = True
#             right = False
#             if not rightblocked:
#                 dx += 1

#         elif keys[pygame.K_d]:
#             if not jump:
#                 screen.blit(player_right[stepindex], (x,y))
#             else:
#                 screen.blit(player_right[0], (x, y))
#             right = True
#             left = False
#             if not leftblocked:
#                 dx -= 1


#         elif left:
#             screen.blit(player_left[0], (x, y))

#         elif right:
#             screen.blit(player_right[0], (x, y))




#         y += vel
#         vel += 2
#         jump_cooldown += 1

#         if jump_cooldown >= 5:
#             jump = False



                
        
    
# dx = 0          
# delay = 0
# def main():
#     global stepindex
#     global x
#     global fps
#     global left
#     global right
#     global keys
#     global movingright
#     global movingleft
#     global delay
#     global dx
#     global tilerect
#     clock = pygame.time.Clock()
#     run = True
#     while run:
#         clock.tick(fps)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False

#         keys = pygame.key.get_pressed()
#         screen.fill(WHITE)
       
        
#         tilerect = []
#         tiley = 0
#         for i in range(len(tilemap)):
#             tilex = dx 
#             for a in tilemap[i]:                         
#                 if a == "WATER":
#                     screen.blit(WATER, (tilex * 32,tiley * 32))
#                 if a == "GRASS":
#                     screen.blit(GRASS, (tilex * 32, tiley * 32))  
#                     tilerect.append(pygame.Rect(tilex * 32, tiley * 32, 32,32))
#                 else: 
#                     pass
#                 tilex += 1
#             tiley += 1  
            


#         move()


#         pygame.display.update()
#         if stepindex == 7:
#             stepindex = 0
#         delay += 1
#         if delay == 2:
#             delay = 0
#             stepindex += 1
#         pygame.display.update()

#     pygame.quit()

# if __name__ == "__main__":
#     main()