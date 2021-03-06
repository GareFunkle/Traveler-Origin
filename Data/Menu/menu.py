import pygame
import math
from game import Game
import Data.settings as settings
import Data.data as data



class Menu:
    def __init__(self):
        self.running = True
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((settings.DISPLAY_X, settings.DISPLAY_Y))

        pygame.display.set_caption(data.GAME_NAME)
        self.game = Game(self.screen)
        
        
                # importer de charger l'arriere plan
        self.background = pygame.image.load('assets/Menu/bg.jpg')
        # self.background = pygame.transform.scale(self.background, (5120, 1080))

        # importer ou charger notre banniere 
        self.banner = pygame.image.load('assets/Menu/banner.png')
        self.banner = pygame.transform.scale(self.banner, (550, 450))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = math.ceil(self.screen.get_width() / 3.60)
        self.banner_rect.y = math.ceil(self.screen.get_height() / -100)
        
        # import chatger notre bouton pour lancer la partie 
        self.play_button = pygame.image.load('assets/Menu/play_button.png')
        self.play_button = pygame.transform.scale(self.play_button, (150, 50))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = math.ceil(self.screen.get_width() / 2.25)
        self.play_button_rect.y = math.ceil(self.screen.get_height() / 1.60)

        # importer le bouton rejouer
        self.restart_button = pygame.image.load('assets/Menu/restart_button.png')
        self.restart_button = pygame.transform.scale(self.restart_button, (150, 50))
        self.restart_button_rect = self.restart_button.get_rect()
        self.restart_button_rect.x = math.ceil(self.screen.get_width() / 2.25)
        self.restart_button_rect.y = math.ceil(self.screen.get_height() / 1.40)

        # importer le bouton parametre
        self.setting_button = pygame.image.load('assets/Menu/setting_button.png')
        self.setting_button = pygame.transform.scale(self.setting_button, (150, 50))
        self.setting_button_rect = self.setting_button.get_rect()
        self.setting_button_rect.x = math.ceil(self.screen.get_width() / 2.25)
        self.setting_button_rect.y = math.ceil(self.screen.get_height() / 1.23)

        # importer le bouton quitter le jeu 
        self.quit_button = pygame.image.load('assets/Menu/quit_button.png')
        self.quit_button = pygame.transform.scale(self.quit_button, (150, 50))
        self.quit_button_rect = self.quit_button.get_rect()
        self.quit_button_rect.x = math.ceil(self.screen.get_width() / 2.25)
        self.quit_button_rect.y = math.ceil(self.screen.get_height() / 1.10)
    
        self.x_background = 0

    def run(self):
        clock = pygame.time.Clock()
        while self.running:

            # appliquer l'arrier plan de notre jeu avec le scroll
            if self.x_background > -3000:
                self.x_background += -1.5
                self.screen.blit(self.background, (self.x_background, 0))
            else:
                self.x_background = 0

                

            
            # verifier si notre jeu a commencer ou non 
            if self.game.is_playing:
                #declancher les instruction de la partie
                    self.game.update()
            # verifier si notre jeu na pas commencer 
            else:
                # ajouter mon ecran de bienvenue
                self.screen.blit(self.quit_button, self.quit_button_rect)
                self.screen.blit(self.setting_button, self.setting_button_rect)
                self.screen.blit(self.restart_button, self.restart_button_rect)
                self.screen.blit(self.play_button, self.play_button_rect)        
                self.screen.blit(self.banner, self.banner_rect)
            
            pygame.display.flip()
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    self.game.pressed[event.key] = True

                elif event.type == pygame.KEYUP:
                    self.game.player.status = 'idle'
                    self.game.pressed[event.key] = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifier si notre souris est en colision avec notre bouton jouer
                    if self.play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
                        self.game.start()
                    if self.restart_button_rect.collidepoint(event.pos):
                        self.game.restart_game()
                    
                    if self.quit_button_rect.collidepoint(event.pos):
                        self.running = False

            clock.tick(settings.FPS)