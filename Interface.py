import pygame as pg


from Player import *
from utilities import *
from settings import *

class Interface:
	def __init__(self):
		self.screen = pg.display.set_mode(RES)
		pg.display.set_caption("Space Shooter")

		self.health_background_bg, self.ui_ratio = scale_image_and_get_ratio(pg.image.load(HEALTH_BAR_BACKGROUND), 320, 60)
		self.health_background_mask_imgORG = scale_and_rot_image(pg.image.load(HEALTH_BAR_BACKGROUND_MASK), self.ui_ratio, 0)
		self.health_background_mask_img = scale_and_rot_image(pg.image.load(HEALTH_BAR_BACKGROUND_MASK), self.ui_ratio, 0)
		self.health_background_mask_img_max_size = self.health_background_mask_img.get_size()

		self.health_left_block = scale_and_rot_image(pg.image.load(HEALTH_BAR_LEFT_BLOCK), self.ui_ratio, 0)

		self.last_update = 0
		self.frame_rate = 1
		self.last_health_size = self.health_background_mask_img_max_size[0]

		# For debug

		self.splash = scale_image(pg.image.load(DIALOG_SPLASH), 500, 300)

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
	

	def update_manual(self, player):
		# Color changing code. However, it does not work correctly.
		
		# self.health_background_mask_img = pg.transform.scale(self.health_background_mask_img, (player.health * (self.health_background_mask_img_max_size[0] / player.max_health), self.health_background_mask_img_max_size[1]))
		# if (player.health < 25):
		# 	mask_threshold = (255, 99, 71) 
		# 	mask_surface = pg.Surface(self.health_background_mask_img.get_size(), pg.SRCALPHA)
		# 	mask_surface.fill(mask_threshold)

		# 	self.health_background_mask_img.blit(mask_surface, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
		# else:
		# 	mask_threshold = (115, 198, 207) 
		# 	mask_surface = pg.Surface(self.health_background_mask_img.get_size(), pg.SRCALPHA)
		# 	mask_surface.fill(mask_threshold)

		# 	self.health_background_mask_img.blit(mask_surface, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
		pass

	def draw(self, player):
		self.draw_health_bar()
		
		# For debug
		x, y = self.splash.get_size()
		self.screen.blit(self.splash, (WIDTH / 2 - x / 2, HEIGHT / 2 - y / 2))


		

	
		
