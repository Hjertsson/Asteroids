from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		
	def draw(self, surface):

		cx = int(self.position.x)
		cy = int(self.position.y)
		pygame.draw.circle(surface, (255, 255, 255), (cx, cy), int(self.radius), 2)



	def update(self, dt):

		self.position += self.velocity * dt

