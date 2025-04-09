import pygame
import random
from config import *

class PipeSystem:
    def __init__(self):
        self.pipes = []
        self.pipe_color = PIPE_COLOR
        self.passed_pipes = []
    
    def create_pipe(self):
        random_height = random.randint(200, HEIGHT - 200)
        bottom_pipe = pygame.Rect(WIDTH, random_height, PIPE_WIDTH, HEIGHT - random_height)
        top_pipe = pygame.Rect(WIDTH, 0, PIPE_WIDTH, random_height - PIPE_GAP)
        return bottom_pipe, top_pipe

    def add_pipe(self):
        bottom_pipe, top_pipe = self.create_pipe()
        self.pipes.extend([bottom_pipe, top_pipe])
    
    def move_pipes(self):
        for pipe in self.pipes:
            pipe.x -= PIPE_SPEED
        self.pipes = [pipe for pipe in self.pipes if pipe.right > 0]
    
    def draw_pipes(self, screen):
        for pipe in self.pipes:
            pygame.draw.rect(screen, self.pipe_color, pipe)
    
    def reset(self):
        self.pipes = []
        self.passed_pipes = []