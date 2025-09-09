import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")
	time_check = pygame.time.Clock()
	dt = 0	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	new_player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
	Asteroid.containers = (asteroids, updatable, drawable)
	asteroids = Asteroid(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, 2)
	AsteroidField.containers = (updatable)
	field = AsteroidField()


	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		screen.fill(pygame.Color('black'))


		for item in updatable:
			item.update(dt)

		for item in drawable:
			item.draw(screen)

		pygame.display.flip()		
		dt = time_check.tick(60) / 1000
		
if __name__ == "__main__":
    main()
