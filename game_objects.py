import pygame
from config import *

class Ground:
    def __init__(self):
        self.rect = pygame.Rect(0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT)
        self.color = GROUND_COLOR
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(None, 36)
        self.text_color = WHITE
    
    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.value}", True, self.text_color)
        screen.blit(score_text, (20, 20))
    
    def increase(self):
        self.value += 1
        
    def reset(self):
        self.value = 0