
import pygame
from random import randint

class fish(pygame.sprite.Sprite):
    def __init__(self,size,fish):
        pygame.sprite.Sprite.__init__(self)        
        self.fp = fish
        self.image = pygame.image.load(self.fp)

        
        
        self.x= randint(0, size[0])
        self.y = randint(0, size[1])
        self.vx = randint(-5,5)/10
        self.vy = randint(-5,5)/10
        self.width, self.height = size
        
        self.rect = self.image.get_rect()
        self.visible = True 
        
        
          
    def draw(self, screen):
        if self.visible == True:

            # updating the rect position
            self.x += self.vx
            self.y += self.vy

            # check to see if its in bounds
            if self.x < 0 or self.x > self.width:
                self.vx = -self.vx

            if self.y < 0 or self.y > self.height:
                self.vy = -self.vy

            self.rect.center = (self.x, self.y)

            screen.blit(self.image, self.rect)
        
