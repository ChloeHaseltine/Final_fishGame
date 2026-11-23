import pygame

class font:
    def __init__(self,x,y,message, SIZE):
        #make my title font
        self.font_fn = "orange juice 2.0.ttf"
        self.title_font = pygame.font.Font(self.font_fn, SIZE)
        self.title_surface = self.title_font.render(message, 1, (255,255,255))
        self.title_rect = self.title_surface.get_rect()
        self.title_rect.center = (x,y)
        
    def draw(self, screen):
        screen.blit(self.title_surface, self.title_rect)