import pygame as pg
from utilities import *
from settings import *


class Engine:
	def __init__(self, ship, x, y, POS, ROT):
		self.x = x
		self.y = y
		self.POS = POS
		self.ROT = ROT
		
		self.index = 0
		self.frames = [scale_and_rot_image(pg.image.load(f"assets/engine_effects/{i:02d}_vanguard.png"), ship.ratio / 1.5, self.ROT) for i in range(32)]
		self.image = self.frames[self.index]

		self.width, self.height = self.image.get_size()

		self.frame_rate = 0.5
		self.last_update = pg.time.get_ticks()

	def move(self, ship):
		# Attach the ship's engine to the ship
		self.x = ship.x + (self.POS[0] * ship.ratio)
		self.y = ship.y + (self.POS[1] * ship.ratio)

	def update(self):
		current = pg.time.get_ticks()
		if current - self.last_update > self.frame_rate:
			self.index = (self.index+1) % len(self.frames)
			self.image = self.frames[self.index]
			self.last_update = current

	def draw(self, screen):
		screen.blit(self.image, (self.x - (self.width / 2), self.y))

