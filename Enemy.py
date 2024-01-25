import pygame as pg
import random
from Engine import *
from utilities import *
from settings import *

class Enemy:
	def __init__(self, x, y, base_speed, max_speed, acceleration, damage, health, asset):
		self.x = x
		self.y = y
		self.base_speed = base_speed
		self.max_speed = max_speed
		self.acceleration = 0
		self.speed = 0
		self.damage = damage
		self.health = health
		self.image = scale_image(asset, 120, 80)
		self.width, self.height = self.image.get_size()
		self.direction = 1 # 1 = right, -1 = left
		self.last_update = 0
		self.ratio = get_ratio(self.image, 120, 80)
	
	def move(self, game):
		# X - AXIS
		self.last_update += pg.time.get_ticks()
		if self.last_update > random.randint(1000000, 9000000):
			self.direction *= -1
			self.speed = -self.base_speed
			self.last_update = 0

		if self.x <= 0 or self.x + self.width >= WIDTH:
			self.direction = -1
			self.speed = self.base_speed

		self.speed = min(self.speed + self.acceleration * game.dt_seconds, self.max_speed)
		self.x += self.direction * self.speed * game.dt_seconds
		
		# Y - AXIS
		if self.y < HEIGHT - 240:
			self.y += abs(self.base_speed) * game.dt_seconds

		# Engine movement
		for engine in self.engines:
			engine.move(self)
	
	def update(self, game):
		self.move(game)

		for engine in self.engines:
			engine.update()

		

	def draw(self, screen):
		# Enemy ship drawing
		screen.blit(self.image, (self.x, self.y))

		# Engine drawing
		for engine in self.engines:
			engine.draw(screen)

class Marauder(Enemy):
	def __init__(self, x, y , speed, damage, health):
		asset = pg.image.load("assets/enemy_ships/marauder.png")
		x = random.randint(0, WIDTH - asset.get_width())
		
		base_speed = 30
		max_speed = 120
		acceleration = 15
		damage = 10
		health = 500

		super().__init__(x, y, base_speed, max_speed, acceleration, damage, health, asset)

		self.image = pg.transform.rotate(self.image, 180)
		self.ratio = get_ratio(asset, 120, 80)

		# If you want to add engines to the ship, you can do it here
		self.engines = []
		self.engines.append(Engine(self, self.x + 20, self.y + 80, (100, 276), 0))

	def move(self, game):
		super().move(game)

	def draw(self, screen):
		super().draw(screen)
