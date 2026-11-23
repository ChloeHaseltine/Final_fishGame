#New game class

import pygame
from random import randint
from Font1 import font 
from Bad1 import bad_fish
from Player1 import player
from Fish import fish


############################

############ADDDDDDDDDDDDDDDDDDDDDDDDDDDDDD INSTRUCTIONS TO THE CODE

##############################
 


TS = 80
WIDTH = 8*TS
HEIGHT = 8*TS 
SIZE = (WIDTH, HEIGHT)
pygame.init()

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock() 
#make a simple bg
golfish_orange = (255,174,3)
dark_red = (105,20,14)
yellow = (255,249,79)
bg = pygame.Surface(SIZE)
bg.fill(golfish_orange)

title = font(WIDTH/2, HEIGHT/2 -50, "Hungry Goldfish!", 90)
bottom_title = font(WIDTH/2, HEIGHT/2 +30, "Press Spacebar to Begin", 40)

title_end = font(WIDTH/2, HEIGHT/2 -50, "Game Over :(", 100)
bottom_title_end = font(WIDTH/2, HEIGHT/2 +30, "Press Spacebar to Exit", 40)

#make a sound
pygame.mixer.init()
bonk = pygame.mixer.Sound('bonk.mp3')
bubble = pygame.mixer.Sound('bubble.mp3')
chomp = pygame.mixer.Sound('chomp.mp3')
underTheSea = pygame.mixer.Sound('bgmusic.mp3')

player1 = player(100,200)
evil1 = bad_fish((600,600), "fish_brown_outline.png")
evil2 = bad_fish((600,600), "fish_brown_outline.png")
evil3 = bad_fish((600,600), "fish_brown_outline.png")
evil4 = bad_fish((600,600), "fish_brown_outline.png")
evil5 = bad_fish((600,600), "fish_brown_outline.png")
evil6 = bad_fish((600,600), "fish_brown_outline.png")

#make all of the fish round one 
red_1 = fish((600,600), "fish_red.png")
green_1 = fish((600,600), "fish_green.png")
blue_1 = fish((600,600), "fish_blue.png")
#make all of the fish round two
red_2 = fish((600,600), "fish_red.png")
green_2 = fish((600,600), "fish_green.png")
blue_2 = fish((600,600), "fish_blue.png")
purple_2 = fish((600,600), "fish_pink.png")
red_22 = fish((600,600), "fish_red.png")
green_22 = fish((600,600), "fish_green.png")
#make all of the fish round three
red_3 = fish((600,600), "fish_red.png")
green_3 = fish((600,600), "fish_green.png")
blue_3 = fish((600,600), "fish_blue.png")
purple_3 = fish((600,600), "fish_pink.png")
red_33 = fish((600,600), "fish_red.png")
green_33 = fish((600,600), "fish_green.png")
blue_33 = fish((600,600), "fish_blue.png")
purple_33 = fish((600,600), "fish_pink.png")

fish_eaten = 0 



#intro screen loop
running = 1
while running:
    screen.blit(bg,(0,0))
    title.draw(screen)
    bottom_title.draw(screen)
    pygame.display.flip()
    underTheSea.play()
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            running = 0
        if e.type == pygame.KEYDOWN:
            running = 0
            


player1_x = 100
player1_y = 100
player1_speed = 15        
#make main loop
bg.fill((255,249,79))

#aquarium background 
bg_image = pygame.image.load("background.jpg").convert()
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
        
#Level OOOOONNNNNNEEEEEEEE SCREEN
running = 1
while running:
    #blit bg
    screen.blit(bg_image, (0, 0))
    player1.draw(screen)
    evil1.draw(screen)
    evil2.draw(screen)
    fish_text = font(100, 30, "Fish Eaten Score: " + str(fish_eaten), 25)
    level_text = font(580, 30, "Level: 1", 25)
    fish_text.draw(screen)
    level_text.draw(screen)
    
    red_1.draw(screen)
    green_1.draw(screen)
    blue_1.draw(screen)
    
    pygame.display.flip()
    events = pygame.event.get()
    
    
    clock.tick(60)
    for e in events:
        if e.type == pygame.QUIT:
            running = 0
    
    
        if e.type == pygame.KEYDOWN:

            # Move down
            if e.key == pygame.K_DOWN:
                if player1_y + player1.size//2 < HEIGHT:
                    player1_y += player1_speed
                    bubble.play()

            # Move up
            if e.key == pygame.K_UP:
                if player1_y - player1.size//2 > 0:
                    player1_y -= player1_speed
                    

            # Move left
            if e.key == pygame.K_LEFT:
                if player1_x - player1.size//2 > 0:
                    player1_x -= player1_speed
                    

            # Move right
            if e.key == pygame.K_RIGHT:
                if player1_x + player1.size//2 < WIDTH:
                    player1_x += player1_speed
                    
                    
            player1.x = player1_x
            player1.y = player1_y
            
            print("X:", player1.x, "Y:", player1.y)
            
            
            
    if red_1.visible and player1.rect.colliderect(red_1.rect):
        print("Yummy! Red fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        red_1.visible = False

    if blue_1.visible and player1.rect.colliderect(blue_1.rect):
        print("Yummy! Green fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        blue_1.visible = False

    if green_1.visible and player1.rect.colliderect(green_1.rect):
        print("Yummy! Green fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        green_1.visible = False
        
        
    if player1.rect.colliderect(evil1.rect):
        print("Collided")
        bonk.play()
        running = 0
    if player1.rect.colliderect(evil2.rect):
        print("Collided")
        bonk.play()
        running = 0

    
    if fish_eaten == 3:
        running = 0 
        #print("X:", player1.x, "Y:", player1.y)
        
#LEVEL TTTTTTTWWWWWWWWOOOOOOOOOOOOO SCREEN
fish_eaten = 0 
running = 1
while running:
    #blit bg
    screen.blit(bg_image, (0, 0))
    player1.draw(screen)
    evil1.draw(screen)
    evil2.draw(screen)
    evil3.draw(screen)
    evil4.draw(screen)
    fish_text = font(100, 30, "Fish Eaten Score: " + str(fish_eaten), 25)
    level_text = font(580, 30, "Level: 2", 25)
    fish_text.draw(screen)
    level_text.draw(screen)
    
    red_2.draw(screen)
    green_2.draw(screen)
    blue_2.draw(screen)
    purple_2.draw(screen)
    red_22.draw(screen)
    green_22.draw(screen)
    
    pygame.display.flip()
    events = pygame.event.get()
    
    
    clock.tick(60)
    for e in events:
        if e.type == pygame.QUIT:
            running = 0
    

        if e.type == pygame.KEYDOWN:

            # Move down
            if e.key == pygame.K_DOWN:
                if player1_y + player1.size//2 < HEIGHT:
                    player1_y += player1_speed
                    bubble.play()

            # Move up
            if e.key == pygame.K_UP:
                if player1_y - player1.size//2 > 0:
                    player1_y -= player1_speed
                    

            # Move left
            if e.key == pygame.K_LEFT:
                if player1_x - player1.size//2 > 0:
                    player1_x -= player1_speed
                    

            # Move right
            if e.key == pygame.K_RIGHT:
                if player1_x + player1.size//2 < WIDTH:
                    player1_x += player1_speed
                    
                    
            player1.x = player1_x
            player1.y = player1_y
            
            print("X:", player1.x, "Y:", player1.y)
            
            
            
    if red_2.visible and player1.rect.colliderect(red_2.rect):
        print("Yummy! Red fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        red_2.visible = False

    if blue_2.visible and player1.rect.colliderect(blue_2.rect):
        print("Yummy! Green fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        blue_2.visible = False

    if green_2.visible and player1.rect.colliderect(green_2.rect):
        print("Yummy! Green fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        green_2.visible = False
        
    if purple_2.visible and player1.rect.colliderect(purple_2.rect):
        print("Yummy! Green fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        purple_2.visible = False
    
    if red_22.visible and player1.rect.colliderect(red_22.rect):
        print("Yummy! Green fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        red_22.visible = False
    
    if green_22.visible and player1.rect.colliderect(green_22.rect):
        print("Yummy! Green fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        green_22.visible = False
        
    
        
        
    if player1.rect.colliderect(evil1.rect):
        print("Collided")
        bonk.play()
        running = 0
    if player1.rect.colliderect(evil2.rect):
        print("Collided")
        bonk.play()
        running = 0
    if player1.rect.colliderect(evil3.rect):
        print("Collided")
        bonk.play()
        running = 0
    if player1.rect.colliderect(evil4.rect):
        print("Collided")
        bonk.play()
        running = 0
        
    if fish_eaten == 6:
        running = 0

###LEVEL TTTTTTTHHHHHHHRRRRRREEEEEEEEEEE SCREEN
fish_eaten = 0 
running = 1
while running:
    #blit bg
    screen.blit(bg_image, (0, 0))
    player1.draw(screen)
    evil1.draw(screen)
    evil3.draw(screen)
    evil4.draw(screen)
    evil5.draw(screen)
    evil6.draw(screen) 
    fish_text = font(100, 30, "Fish Eaten Score: " + str(fish_eaten), 25)
    level_text = font(580, 30, "Level: 3", 25)
    fish_text.draw(screen)
    level_text.draw(screen)
    
    red_3.draw(screen)
    green_3.draw(screen)
    blue_3.draw(screen)
    purple_3.draw(screen)
    red_33.draw(screen)
    green_33.draw(screen)
    blue_33.draw(screen)
    purple_33.draw(screen)
    
    pygame.display.flip()
    events = pygame.event.get()
    
    
    clock.tick(60)
    for e in events:
        if e.type == pygame.QUIT:
            running = 0
    
    
        if e.type == pygame.KEYDOWN:

            # Move down
            if e.key == pygame.K_DOWN:
                if player1_y + player1.size//2 < HEIGHT:
                    player1_y += player1_speed
                    bubble.play()

            # Move up
            if e.key == pygame.K_UP:
                if player1_y - player1.size//2 > 0:
                    player1_y -= player1_speed
                    

            # Move left
            if e.key == pygame.K_LEFT:
                if player1_x - player1.size//2 > 0:
                    player1_x -= player1_speed
                    

            # Move right
            if e.key == pygame.K_RIGHT:
                if player1_x + player1.size//2 < WIDTH:
                    player1_x += player1_speed
                    
                    
            player1.x = player1_x
            player1.y = player1_y
            
            print("X:", player1.x, "Y:", player1.y)
            
            
            
    if red_3.visible and player1.rect.colliderect(red_3.rect):
        print("Yummy! Red fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        red_3.visible = False

    if blue_3.visible and player1.rect.colliderect(blue_3.rect):
        print("Yummy! Green fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        blue_3.visible = False

    if green_3.visible and player1.rect.colliderect(green_3.rect):
        print("Yummy! Green fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        green_3.visible = False
        
        
    if purple_3.visible and player1.rect.colliderect(purple_3.rect):
        print("Yummy! Green fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        green_3.visible = False
        
        
    if red_33.visible and player1.rect.colliderect(red_33.rect):
        print("Yummy! Green fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        red_33.visible = False
        
    if blue_33.visible and player1.rect.colliderect(blue_33.rect):
        print("Yummy! Green fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        blue_33.visible = False
        
    if green_33.visible and player1.rect.colliderect(green_33.rect):
        print("Yummy! Green fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        green_33.visible = False
        
    if purple_33.visible and player1.rect.colliderect(purple_33.rect):
        print("Yummy! Green fish eaten!")
        chomp.play()
        fish_eaten += 1
        player1.grow()
        purple_33.visible = False
        
    if player1.rect.colliderect(evil1.rect):
        print("Collided")
        bonk.play()
        running = 0
    if player1.rect.colliderect(evil2.rect):
        print("Collided")
        bonk.play()
        running = 0
    if player1.rect.colliderect(evil3.rect):
        print("Collided")
        bonk.play()
        running = 0
    if player1.rect.colliderect(evil4.rect):
        print("Collided")
        bonk.play()
        running = 0
    if player1.rect.colliderect(evil5.rect):
        print("Collided")
        bonk.play()
        running = 0
    if player1.rect.colliderect(evil6.rect):
        print("Collided")
        bonk.play()
        running = 0
    
    if fish_eaten == 8:
        running = 0


#END SCREEN LOOP
bg.fill((105,20,14))
running = 1
while running:
    screen.blit(bg,(0,0))
    title_end.draw(screen)
    bottom_title_end.draw(screen)
    pygame.display.flip()
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            running = 0
        if e.type == pygame.KEYDOWN:
            running = 0

                     
            
pygame.quit()
            

