from circleshape import CircleShape
from constants import *
import pygame
import random
from logger import log_event

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		
	def draw(self, surface):

		cx = int(self.position.x)
		cy = int(self.position.y)
		pygame.draw.circle(surface, (255, 255, 255), (cx, cy), int(self.radius), 2)


	def update(self, dt):

		self.position += self.velocity * dt

	def split(self):
		log_event("asteroid_split")
		self.kill()
		#print(self.position)
		if(self.radius <= ASTEROID_MIN_RADIUS):
			return
		angle = random.uniform(20, 50)
		first_asteroid_velocity = self.velocity.rotate(angle)
		second_asteroid_velocity = self.velocity.rotate(-angle)

		self.radius -= ASTEROID_MIN_RADIUS
		
		asteroid_one = Asteroid(self.position.x, self.position.y, self.radius)
		asteroid_second = Asteroid(self.position.x, self.position.y, self.radius)

		asteroid_one.velocity = pygame.Vector2(first_asteroid_velocity * 1.2)
		asteroid_second.velocity = pygame.Vector2(second_asteroid_velocity)