import pygame
from characters.Player.player import Player
from Data.Map.map import MapManager



class Game:

    def __init__(self):
        self.is_playing = False
        # creation de la fenetre du jeu
        # self.screen = pygame.display.set_mode((settings.DISPLAY_X, settings.DISPLAY_Y))


        # generer un joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)

        self.pressed = {}

    # def init_screen(width, height, mode):
    #     screen = pygame.display.set_mode((int(width), int(height)), mode)
    #     return screen

    def move(self):
        if self.pressed.get(pygame.K_ESCAPE):
            self.running = False
        if self.pressed.get(pygame.K_RIGHT):
            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT):
            self.player.move_left()
        if self.pressed.get(pygame.K_UP):
            self.player.to_jump = True
            self.player.number_jump += 1
        if self.pressed.get(pygame.K_RIGHT) and self.pressed.get(pygame.K_LSHIFT):
            self.player.run_right()
        if self.pressed.get(pygame.K_LEFT) and self.pressed.get(pygame.K_LSHIFT):
            self.player.run_left()
        if self.pressed.get(pygame.K_SPACE):
            self.player.sprite.status = "attack"
            self.player.sprite.animation_speed = 0.23
        if self.pressed.get(pygame.K_LCTRL):
            self.player.launch_projectile()

    def update(self):
        self.map_manager.update()
        self.player.sprite.save_location()
        self.move()
        self.map_manager.draw()
        self.player.sprite.animate()

# boucle du jeu


        self.running = True

        while self.running:


            pygame.display.flip()




