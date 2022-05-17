import pygame
import math
from game import Game
import Data.settings as settings
import Data.data as data



class Menu:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(data.GAME_NAME)
        self.game = Game()
        
        
                # importer de charger l'arriere plan
        self.background = pygame.image.load('assets/bg.jpg')

        # importer ou charger notre banniere 
        self.banner = pygame.image.load('assets/banner.png')
        self.banner = pygame.transform.scale(self.banner, (600, 600))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = math.ceil(self.screen.get_width() / 4)
        
        # import chatger notre bouton pour lancer la partie 
        self.play_button = pygame.image.load('assets/button.png')
        self.play_button = pygame.transform.scale(self.play_button, (400, 150))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = math.ceil(self.screen.get_width() / 3.33)
        self.play_button_rect.y = math.ceil(self.screen.get_height() / 2)
        
    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            
            # appliquer l'arrier plan de notre jeu 
            self.screen.blit(self.background, (0, -200))
            
            # verifier si notre jeu a commencer ou non 
            if self.game.is_playing:
                #declancher les instruction de la partie
                    self.game.update(self.screen)
            # verifier si notre jeu na pas commencer 
            else:
                # ajouter mon ecran de bienvenue
                self.screen.blit(self.play_button, self.play_button_rect)        
                self.screen.blit(self.banner, self.banner_rect)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    self.game.pressed[event.key] = True

                elif event.type == pygame.KEYUP:
                    self.game.player.sprite.status = 'idle'
                    self.game.pressed[event.key] = False
                    
                clock.tick(settings.FPS)