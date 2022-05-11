#Name: Mike P.
#Date: 4/20/21
#Description: Alien Class
import pygame
class Enemy():
	def __init__(self, screen):
		self.screen = screen
		self.ship_speed_factor = 1.5
		self.screen_rect2 = screen.get_rect()
		self.image = pygame.image.load('images/villain.jpg')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.right = self.screen_rect.right - 50
		self.center = float(self.rect.centerx)
		self.moving_left = False
	def update(self):
		if self.moving_left and self.rect.left >0:
			self.center -= self.ship_speed_factor
			self.rect.centerx = self.center
	def blitme(self):
		self.screen.blit(self.image, self.rect)
	def center_ship(self):
		self.center = self.screen_rect.centerx
	def returnScreenRect(self):
		return self.screen_rect
	
