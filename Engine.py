import pygame as pg
from settings import *


class Engine:
	def __init__(self, ship, x, y, engine_path):
		self.x = x
		self.y = y
		
		self.index = 0
		self.frames = [scale_image(pg.image.load(f"assets/engine_effects/{i:02d}_vanguard.png"), ship.ratio) for i in range(32)]
		self.image = self.frames[self.index]

		self.width, self.height = self.image.get_size()

		self.frame_rate = 0.5
		self.last_update = pg.time.get_ticks()

	def update(self):
		current = pg.time.get_ticks()
		if current - self.last_update > self.frame_rate:
			self.index = (self.index+1) % len(self.frames)
			self.image = self.frames[self.index]
			self.last_update = current

	def draw(self, screen):
		screen.blit(self.image, (self.x - (self.width / 2), self.y))

def scale_image (image, ratio):
	original_width, original_height = image.get_size()

	new_width = int(original_width * ratio)
	new_height = int(original_height * ratio)

	return pg.transform.rotate(pg.transform.scale(image, (new_width, new_height)), 180)
