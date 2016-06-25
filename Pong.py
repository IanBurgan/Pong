#Pong by Ian Burgan

import random, pygame, sys
from pygame.locals import *
from Entities import *

def main():
	pygame.init()
	#             R    G    B
	WHITE     = (255, 255, 255)
	BLACK     = (  0,   0,   0)

	WIDTH = 900
	HEIGHT = 600
	SCREENSIZE = (WIDTH, HEIGHT)
	DISPLAYSURF = pygame.display.set_mode(SCREENSIZE)

	pygame.display.set_caption("Pong by Ian")
	
	clock = pygame.time.Clock()
	
	vertical = random.randint(-3, 4)
	# Ball(screen tuple, radius, vx, vy)
	ball = Ball(SCREENSIZE, 10, 6, vertical)
	player = Player_Paddle(SCREENSIZE, 20, 80, 5)
	computer = AI_Paddle(SCREENSIZE, 20, 80, 5)
	
	done = False

	while not done:
		clock.tick(30)
		
		for event in pygame.event.get():
			if event.type == QUIT:
				done = True
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					done = True
				elif event.key == K_DOWN:
					player.direction = 1
				elif event.key == K_UP:
					player.direction = -1
			if event.type == KEYUP:
				if event.key == K_DOWN or event.key == K_UP:
					player.direction = 0
		
		DISPLAYSURF.fill(BLACK)
		player.update()
		computer.update(ball)
		ball.update(player, computer)
		pygame.draw.rect(DISPLAYSURF, WHITE, player.rect)
		pygame.draw.rect(DISPLAYSURF, WHITE, computer.rect)
		pygame.draw.rect(DISPLAYSURF, WHITE, ball.rect)
		pygame.display.update()
	
	pygame.quit()
	sys.exit()
main()
