import pygame as pg
import math
import copy

from utilities import *
from settings import *


class Laser:
	def __init__(self, x, y, damage, ship, targetPos = None):
		self.width = 3
		self.height = 10
		self.x = x - (self.width / 2)
		self.y = y - (self.height / 2)
		self.damage = damage


		

		self.frame_rate = 20
		self.last_update = pg.time.get_ticks()

		# Speed
		self.speed = 250

		# Target
		self.targetPos = targetPos
		if targetPos is not None:
			

			dx = self.targetPos[0] - self.x
			dy = self.targetPos[1] - self.y

			distance = math.sqrt(dx**2 + dy**2)
			self.vx = dx / distance
			self.vy = dy / distance

			self.rotate = math.degrees(math.atan2(-dy, dx))
				
			self.frames = [pg.transform.rotate(ship.basic_laser_frames[i], 90+self.rotate) for i in range(len(ship.basic_laser_frames))]
		
		if targetPos is None:
			self.frames = ship.basic_laser_frames
		# Frame
		self.index = 0
		self.image = self.frames[self.index]
		self.width, self.height = self.image.get_size()

	def collide(self, enemy):
		return pg.Rect(self.x, self.y, self.width, self.height).colliderect(pg.Rect(enemy.x, enemy.y, enemy.width, enemy.height))

	def move(self, dt_seconds):
		if self.targetPos is None:
			self.y -= self.speed * dt_seconds
		else:
			self.y += self.vy * self.speed * dt_seconds
			self.x += self.vx * self.speed * dt_seconds

	def update(self, dt_seconds):
		self.move(dt_seconds)

		current = pg.time.get_ticks()
		if current - self.last_update > self.frame_rate:
			self.index = (self.index+1) % len(self.frames)
			self.image = self.frames[self.index]
			self.last_update = current

	def draw(self, screen):
		screen.blit(self.image, (self.x - (self.width / 2), self.y - (self.height / 2)))
		

