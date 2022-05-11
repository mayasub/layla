#Name: Mike P.
#Date: 1/19/22
#Description: creating a pygame window and 
#respond to user input.
import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from alien import Alien
from button import Button
import gamefunctions as gf
def runGame():
	#Initialize game,settings and create a screen
	pygame.init()
	ai_settings = Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	play_button = Button(ai_settings,screen,"Play")
	stats = GameStats(ai_settings)
	#Make a ship
	ship = Ship(ai_settings,screen)
	#Make an alien
	alien = Alien(ai_settings,screen)
	#Make a group to store bullets in.
	bullets = Group()
	aliens = Group()
	#Create the fleet of aliens
	gf.create_fleet(ai_settings,screen,ship,aliens)
	#Create an instance to store game stats
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	#Start the main loop for the game.
	while True:
		#watch for keyboard and mounse events
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
		
runGame()
