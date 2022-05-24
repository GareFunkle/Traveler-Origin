from turtle import screensize
import pygame
from Data.Map.map import MapManager
from characters.entity import NPC, Entity, Player



class Game:

    def __init__(self, screen):
        self.is_playing = False
        # creation de la fenetre du jeu
        self.screen = screen

        # generer un joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)

        self.pressed = {}

    def player_dead(self):
        if self.player.current_health == 0:
            self.game_over()

    def start(self):
        self.is_playing = True
        
    def restart_game(self):
        self.is_playing = False  
        self.map_manager.update()
        self.map_manager.teleport_player("player")
        self.player.status = 'idle'
        self.player.current_health = self.player.max_health      

    def game_over(self):
        # remettre le jeu a neuf, retirer les mponstre remmetre le joueur a 100 point de vie , jeu en attente
        self.map_manager.update()
        self.map_manager.teleport_player("player")
        self.player.status = 'idle'
        self.player.current_health = self.player.max_health
        self.is_playing = False
        

    def move(self):
        if self.pressed.get(pygame.K_ESCAPE):
            self.is_playing = False
        if self.pressed.get(pygame.K_RIGHT):
            self.player.move_right()
        if self.pressed.get(pygame.K_d):
            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT):
            self.player.move_left()
        if self.pressed.get(pygame.K_q):
            self.player.move_left()
        if self.pressed.get(pygame.K_UP) and self.player.position[1] > 0:
            self.player.to_jump = True
            self.player.number_jump += 1
        if self.pressed.get(pygame.K_z) and self.player.position[1] > 0:
            self.player.to_jump = True
            self.player.number_jump += 1
        if self.pressed.get(pygame.K_RIGHT) and self.pressed.get(pygame.K_LSHIFT):
            self.player.run_right()
        if self.pressed.get(pygame.K_LEFT) and self.pressed.get(pygame.K_LSHIFT):
            self.player.run_left()
        if self.pressed.get(pygame.K_d) and self.pressed.get(pygame.K_LSHIFT):
            self.player.run_right()
        if self.pressed.get(pygame.K_q) and self.pressed.get(pygame.K_LSHIFT):
            self.player.run_left()
        if self.pressed.get(pygame.K_SPACE):
            self.player.status = "attack"
            self.player.animation_speed = 0.23
        if self.pressed.get(pygame.K_LCTRL):
            self.player.launch_projectile()

    def update(self):
        self.map_manager.update()
        self.player.save_location()
        self.move()
        self.map_manager.draw()
        self.player.animate()
        # self.npcs.animate()
        self.player.update_health_bar(self.screen)
        self.player_dead()







