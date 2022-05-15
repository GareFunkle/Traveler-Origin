

class CanWalk:
    # Must be attached to unit
    def __init__(self, rect, speed_walk=3, speed_run=5):
        self.rect = rect
        self.speed_walk = speed_walk
        self.speed_run = speed_run

    def move_right(self):
        self.sprite.facing_right = True
        self.sprite.position[0] += self.speed_walk
        self.sprite.status = 'run'
        self.sprite.animation_speed = 0.25

    def move_left(self):
        self.sprite.facing_right = False
        self.sprite.position[0] -= self.speed_walk
        self.sprite.status = 'run'
        self.sprite.animation_speed = 0.25
        

    
    def run_right(self):
        self.sprite.position[0] += self.speed_run
        self.sprite.status = 'run'
        self.sprite.animation_speed = 0.55

    def run_left(self):
        self.position[0] -= self.speed_run
        self.sprite.status = 'run'
        self.sprite.animation_speed = 0.55
