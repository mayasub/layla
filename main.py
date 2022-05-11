import pygame
import sys
from image import Image
def runGame():
	pygame.init()
	screen=pygame.display.set_mode((500,700))
	pygame.display.set_caption("Test Image")
	#Make a ship
	image = Image(screen)
	while True:
		pygame.display.flip()
		image.blitme()
runGame()

