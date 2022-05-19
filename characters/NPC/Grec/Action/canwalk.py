import pygame


class CanWalk:
    # Must be attached to unit
    def __init__(self, name, nb_points, speed_walk=1, speed_run=5, ):
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.nb_points = nb_points
        self.points = []
        self.name = name
        self.current_point = 0

    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.sprite.position[0] = location.x
        self.sprite.position[1] = location.y
        self.sprite.save_location()



    def move_right(self):
        self.sprite.facing_right = True
        self.speed_walk = 3
        self.move()
        self.sprite.status = 'run'
        self.sprite.animation_speed = 0.25

    def move_left(self):
        self.sprite.facing_right = False
        self.speed_walk = -3
        self.move()
        self.sprite.status = 'run'
        self.sprite.animation_speed = 0.25

    def move(self):
        current_point = self.current_point
        target_point = self.current_point + 1

        if target_point >= self.nb_points:
            target_point = 0

        current_rect = self.points[current_point]
        target_rect = self.points[target_point]


        if current_rect.x > target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.move_left()
        elif current_rect.x < target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.move_right()

        if self.sprite.rect.colliderect(target_rect):
            self.current_point = target_point

    def load_points(self, tmx_data):
        for num in range(1, self.nb_points+1):
            point = tmx_data.get_object_by_name(f"{self.name}_path{num}")
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)


