import pygame

# Definir la Classe qui va gerer le projectile 
class Projectile(pygame.sprite.Sprite):

    # Definir le constructeur de cette class projectile
    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('assets/Projectile/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # donner de la rotation a mon projectile
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    
    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
     
         
        # verifiersi ntre projectile nest plus prset sur lecran
        if self.rect.x > 1080 :
            # suprimmer le projectile en dehors de lecran
            self.remove()
            print("Projectile suprimer!")
