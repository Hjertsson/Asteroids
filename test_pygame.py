import pygame

print("Initializing pygame...")
pygame.init()

print("Creating window...")
screen = pygame.display.set_mode((400, 300))
print("Window size:", screen.get_size())

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("red")
    pygame.display.flip()
    clock.tick(30)

print("Exiting...")
pygame.quit()
