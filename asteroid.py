from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            splitting_angle = random.uniform(20,50)
            split_1 = self.velocity.rotate(splitting_angle)
            split_2 = self.velocity.rotate(-splitting_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            Asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            Asteroid_1.velocity = split_1
            Asteroid_1.velocity *= 1.2
            Asteroid_2.velocity = split_2
            Asteroid_2.velocity *= 1.2