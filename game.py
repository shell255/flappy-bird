import pygame
import sys
from bird import Bird
from pipe_system import PipeSystem
from game_objects import *
from config import *

class FlappyGame:
    def __init__(self):
        """مقداردهی اولیه بازی"""
        pygame.init()
        
        # تنظیمات پنجره
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Flappy Bird AI')
        self.clock = pygame.time.Clock()
        
        self.background_color = BG_COLOR
                
        # ایجاد اجزای بازی
        self.bird = Bird()
        self.pipe_system = PipeSystem()
        self.ground = Ground()
        self.score = Score()
        
        # وضعیت بازی
        self.game_active = False
        self.setup_events()
        
        # فونت برای نمایش پیام‌ها
        self.font = pygame.font.SysFont('Arial', 32)

    def setup_events(self):
        """تنظیم رویدادهای زمان‌بندی شده"""
        self.SPAWNPIPE = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPAWNPIPE, PIPE_FREQUENCY)

    def check_collisions(self):
        """بررسی برخوردهای بازی"""
        # برخورد با زمین
        if self.bird.rect.bottom >= self.ground.rect.top:
            return True
        
        # برخورد با لوله‌ها
        for pipe in self.pipe_system.pipes:
            if self.bird.rect.colliderect(pipe):
                return True
        
        # برخورد با سقف
        if self.bird.rect.top <= 0:
            return True
            
        return False

    def handle_events(self):
        """مدیریت رویدادهای ورودی"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_active:
                        self.bird.jump()
                    else:
                        self.reset_game()
                        self.game_active = True
            
            if event.type == self.SPAWNPIPE and self.game_active:
                self.pipe_system.add_pipe()

    def update_game(self):
        """به‌روزرسانی وضعیت بازی"""
        if not self.game_active:
            return
            
        # آپدیت پرنده
        self.bird.update()
        
        # آپدیت لوله‌ها
        self.pipe_system.move_pipes()
        
        # بررسی عبور از لوله و افزایش امتیاز
        for pipe in self.pipe_system.pipes:
            if pipe.right < self.bird.rect.left and id(pipe) not in self.pipe_system.passed_pipes:
                self.pipe_system.passed_pipes.append(id(pipe))
                #self.score.increase()
        
        # بررسی برخوردها
        if self.check_collisions():
            self.game_active = False

    def render(self):
        """رندرینگ اجزای بازی"""
        # پس‌زمینه
        self.screen.fill(self.background_color)
        
        # لوله‌ها (فقط در حالت فعال)
        if self.game_active:
            self.pipe_system.draw_pipes(self.screen)
            self.bird.draw(self.screen)
        
        # زمین و امتیاز (همیشه نمایش داده می‌شود)
        self.ground.draw(self.screen)
        self.score.draw(self.screen)
        
        # پیام شروع/پایان بازی
        if not self.game_active:
            status_text = "Game Ended. Press SPACE" if self.score.value > 0 else "Press SPACE To Start"
            text_surface = self.font.render(status_text, True, WHITE)
            text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
            self.screen.blit(text_surface, text_rect)
        
        pygame.display.update()

    def reset_game(self):
        print("Resetting game...")
        self.bird.reset()
        print("Resetting PipeSystem...")
        self.pipe_system.reset()
        print("Resetting Score...")
        self.score.reset()

    def run(self):
        """حلقه اصلی بازی"""
        while True:
            self.handle_events()
            self.update_game()
            self.render()
            self.clock.tick(FPS)