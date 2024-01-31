import pygame as pg

from Player import *
from utilities import *
from settings import *

class Interface:
	def __init__(self, game):
		self.screen = pg.display.set_mode(RES)
		pg.display.set_caption("Space Shooter")

		self.health_background_bg, self.ui_ratio = scale_image_and_get_ratio(game.ui["health_bar_bg"], 320, 60)
		self.health_background_mask_imgORG = scale_and_rot_image(game.ui["health_bar_bg_mask"], self.ui_ratio, 0)
		self.health_background_mask_img = scale_and_rot_image(game.ui["health_bar_bg_mask"], self.ui_ratio, 0)
		self.health_background_mask_img_max_size = self.health_background_mask_img.get_size()

		self.health_left_block = scale_and_rot_image(game.ui["health_bar_left_block"], self.ui_ratio, 0)

		self.last_update = 0
		self.frame_rate = 1
		self.last_health_size = self.health_background_mask_img_max_size[0]


	def draw_health_bar(self):
		self.screen.blit(self.health_background_bg, (28, 10))
		self.screen.blit(self.health_background_mask_img, (28, 10))
		self.screen.blit(self.health_left_block, (10, 10))
		pass
		

	def update(self, game):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				game.running = False
			elif event.type == pg.KEYDOWN:
				game.running = True

		current = pg.time.get_ticks()
		if current - self.last_update > self.frame_rate:
			desired_health_size = game.player.health * (self.health_background_mask_img_max_size[0] / game.player.max_health)
			if abs(self.last_health_size - desired_health_size) > 1:
				self.last_health_size += (desired_health_size - self.last_health_size) / abs(desired_health_size - self.last_health_size)
				self.health_background_mask_img = self.health_background_mask_imgORG.subsurface((0, 0, int(self.last_health_size), self.health_background_mask_img_max_size[1]))
			self.last_update = current
	

	def draw(self, player):
		self.draw_health_bar()
	


		

	
		
