import pygame
from config import *

class Bird:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, BIRD_WIDTH, BIRD_HEIGHT)
        self.rect.center = (BIRD_START_X, BIRD_START_Y)
        self.movement = 0
        self.gravity = GRAVITY
        self.color = BIRD_COLOR
    
    def jump(self):
        self.movement = JUMP_STRENGTH
    
    def update(self):
        self.movement += self.gravity
        self.rect.y += self.movement
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)  # رسم پرنده به شکل بیضی
    
    def reset(self):
        self.rect.center = (BIRD_START_X, BIRD_START_Y)
        self.movement = 0