import pygame


# Definir la Classe qui va gerer le projectile


class Projectile(pygame.sprite.Sprite):

    # Definir le constructeur de cette class projectile
    def __init__(self, velocity=3, angle=0):
        super().__init__()
        self.velocity = velocity
        self.image = pygame.image.load('assets/Projectile/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = self.sprite.position[0] + 120
        self.rect.y = self.sprite.position[1] + 80
        self.origin_image = self.image
        self.angle = angle


    def rotate(self):
        # donner de la rotation a mon projectile
        self.angle += 12
        self.image = pygame.transform.rotozoom(
            self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

    #  # verifier si le projectile entre en collision avec un mo,stre
    #     for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
    #         # suprimer le projectile
    #         self.remove()
    #     # infliger les degats
    #         monster.damage(self.player.attack)

        # verifiersi ntre projectile nest plus prset sur lecran
        if self.rect.x > 1080:
            # suprimmer le projectile en dehors de lecran
            self.remove()
            print("Projectile suprimer!")

    
    def launch_projectile(self):
        # creer une nouvel instance de la classe projectile
        self.all_projectiles.add(Projectile(self))
        # demarer l'animation
        self.start_animation()
