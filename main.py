import pygame
import constants
from player import Player
from constants import *
def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")
	time_check = pygame.time.Clock()
	dt = 0
	
	new_player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		screen.fill(pygame.Color('black'))
		new_player.update(dt)
		new_player.draw(screen)
		pygame.display.flip()		
		dt = time_check.tick(60) / 1000
		
if __name__ == "__main__":
    main()
