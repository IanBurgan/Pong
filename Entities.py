import pygame

class Player_Paddle():
	def __init__(self, screen, width, height, vy):
		self.left = screen[0] - (11 + width)
		self.top =  (screen[1] // 2) - (height // 2)
		
		self.width = width
		self.height = height
		
		self.ybound = screen[1]
		
		self.direction = 0
		self.speed = vy
		
		self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
		
	def update(self):
		if self.rect.bottom >= self.ybound - 1 and self.direction == 1:
			self.rect.bottom = self.ybound -1
		elif self.rect.top <= 0 and self.direction == -1:
			self.rect.top = 0
		else:
			self.rect.centery += self.direction * self.speed

class AI_Paddle():
	def __init__(self, screen, width, height, vy):
		self.left = 10
		self.top = (screen[1] // 2) - (height // 2)
		
		self.width = width
		self.height = height
		
		self.ybound = screen[1]
		
		self.direction = 0
		self.speed = vy
		
		self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
		
	def update(self, ball):
		if self.rect.bottom < ball.rect.top:
			self.direction = 1
		elif self.rect.top > ball.rect.bottom:
			self.direction = -1
		
			
		if self.rect.bottom >= self.ybound - 1 and self.direction == 1:
			self.rect.bottom = self.ybound - 1
		elif self.rect.top <= 0 and self.direction == -1:
			self.rect.top = 0
		else:
			self.rect.centery += self.direction * self.speed
		
class Ball():
	def __init__(self, screen, radius, vx, vy):
		self.left = screen[0] // 2 - radius
		self.top = screen[1] // 2 - radius
		self.radius = radius
		
		self.xbound = screen[0]
		self.ybound = screen[1]
		self.direction = [1,1]
		self.vx = vx
		self.vy = vy
		
		self.rect = pygame.Rect(self.left, self.top, self.radius * 2, self.radius * 2)
	
	def update(self, player, computer):
		self.rect.centerx += self.vx * self.direction[0]
		self.rect.centery += self.vy * self.direction[1]

		if self.rect.colliderect(player.rect):
			self.direction[0] = -1
			self.vy += (self.rect.centery - player.rect.centery) // 8
		if self.rect.colliderect(computer.rect):
			self.direction[0] = 1
			self.vy += (self.rect.centery - computer.rect.centery) // 8

		if self.rect.top <= 0 or self.rect.bottom >= self.ybound - 1:
			self.direction[1] *= -1
