#Villian class    
        
import pygame
from random import randint

class bad_fish(pygame.sprite.Sprite):
    def __init__(self,size,fish):
        pygame.sprite.Sprite.__init__(self)        
        self.fp = fish
        self.image = pygame.image.load(self.fp)

        
        
        self.x= randint(0, size[0])
        self.y = randint(0, size[1])
        self.vx = randint(-5,5)/10
        self.vy = randint(-5,5)/10
        self.width, self.height = size 
        
        
        
        #self.image = pygame.transform.rotozoom(self.image,0,0.5)
        self.rect = self.image.get_rect()
        #self.image_face = pygame.transform.rotozoom(self.image_face,0,0.5)
        #self.rect = self.image_face.get_rect()
        
          
        
    def draw(self, screen):
        #updating the rect position
        self.x += self.vx
        self.y += self.vy
        
        #check to see if its in bounds
        if self.x < 0 or self.x > self.width:
            self.vx = -self.vx
        if self.y < 0 or self.y > self.height:
            self.vy = -self.vy
        self.rect.center = (self.x, self.y)
        
        #if player1.rect.colliderect(evil4.rect):
        
        screen.blit(self.image, (self.x, self.y))
    
        