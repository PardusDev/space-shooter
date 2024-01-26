import pygame as pg
from utilities import *
from settings import *


class Laser:
	def __init__(self, x, y, damage, ship):
		self.width = 3
		self.height = 10
		self.x = x - (self.width / 2)
		self.y = y - (self.height / 2)
		self.damage = damage

		# Frame
		self.index = 0
		self.frames = ship.basic_laser_frames
		self.image = self.frames[self.index]
		self.width, self.height = self.image.get_size()

		self.frame_rate = 20
		self.last_update = pg.time.get_ticks()

		# Speed
		self.speed = 250

	def collide(self, enemy):
		return pg.Rect(self.x, self.y, self.width, self.height).colliderect(pg.Rect(enemy.x, enemy.y, enemy.width, enemy.height))

	def move(self, dt_seconds):
		self.y -= self.speed * dt_seconds

	def update(self, dt_seconds):
		self.move(dt_seconds)

		current = pg.time.get_ticks()
		if current - self.last_update > self.frame_rate:
			self.index = (self.index+1) % len(self.frames)
			self.image = self.frames[self.index]
			self.last_update = current

	def draw(self, screen):
		screen.blit(self.image, (self.x - (self.width / 2), self.y - (self.height / 2)))

		# Old laser drawing
		#pg.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
		

