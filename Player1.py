#player class

import pygame    

class player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        
        self.area = (448,576,64,64)
        self.spritesheet = pygame.image.load("spritesheet.png")

        self.original_image = pygame.Surface((80,80),pygame.SRCALPHA)
        self.original_image.blit(self.spritesheet,(0,0),self.area)

        self.size = 80
        self.image = pygame.transform.scale(self.original_image,(self.size,self.size))
        
        
        #self.image = pygame.transform.rotozoom(self.image,0,0.5)
        self.rect = self.image.get_rect()
        #self.image_face = pygame.transform.rotozoom(self.image_face,0,0.5)
        #self.rect = self.image_face.get_rect()
        
          
        
    def grow(self):
        self.size += 10
        self.image = pygame.transform.scale(self.original_image,(self.size,self.size))
        self.rect = self.image.get_rect(center=(self.x,self.y))

    def draw(self, screen):
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.rect)    
