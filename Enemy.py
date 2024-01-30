import pygame as pg
import random

from Laser import *
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
		self.image, self.ratio = scale_image_and_get_ratio(asset, 120, 80)
		self.width, self.height = self.image.get_size()
		self.direction = 1 # 1 = right, -1 = left
		self.last_update = 0

		# Engines
		self.engines = []

		# Turrets
		self.basic_laser_frames = [scale_and_rot_image(pg.image.load(f"assets/laser/ally_basic_laser/sprite_{i:02d}.png"), self.ratio / 4, (0)) for i in range(23)]
		self.lasers = []
		self.turretPoses = []
		self.laserCooldown = 0.32
		self.last_fired_time = 0
	
	def move(self, game):
		# X - AXIS
		self.last_update += pg.time.get_ticks()
		if self.last_update > random.randint(pg.time.get_ticks(), pg.time.get_ticks()+9000000):
			self.direction *= -1
			self.speed = -self.base_speed
			self.last_update = 0

		if self.x <= 0 or self.x + self.width >= WIDTH:
			self.direction = -1
			self.speed = self.base_speed

		self.speed = min(self.speed + self.acceleration * game.dt_seconds, self.max_speed * game.dt_seconds)
		self.x += self.direction * self.speed * game.dt_seconds
		
		# Y - AXIS
		if self.y < HEIGHT - 240:
			self.y += abs(self.base_speed) * game.dt_seconds

		# Engine movement
		for engine in self.engines:
			engine.move(self)

	def fire(self, game):
		current_time = pg.time.get_ticks() / 1000.0
		# You can add range
		if self.y > 0:
			if current_time - self.last_fired_time >= self.laserCooldown:
				for xy in self.turretPoses:
					turretX, turretY = xy
					turretX = self.x + (turretX * self.ratio)
					turretY = self.y + (turretY * self.ratio)
					self.lasers.append(Laser(turretX, turretY, self.damage, self, (game.player.spaceship.x, game.player.spaceship.y)))
				
				game.sound_effects["enemy_laser"].play()
				self.last_fired_time = current_time

	def collide(self, spaceship):
		return pg.Rect(self.x, self.y, self.width, self.height).colliderect(pg.Rect(spaceship.x, spaceship.y, spaceship.width, spaceship.height))
	
	def update(self, game):
		self.move(game)
		self.fire(game)
		

		for engine in self.engines:
			engine.update()

		for laser in self.lasers:
			if (laser.y > HEIGHT):
				self.lasers.remove(laser)
			else:
				laser.update(game.dt_seconds)

		

	def draw(self, screen):
		# Enemy ship drawing
		screen.blit(self.image, (self.x, self.y))

		# Engine drawing
		for engine in self.engines:
			engine.draw(screen)

		for laser in self.lasers:
			laser.draw(screen)

class Marauder(Enemy):
	def __init__(self, x, y , speed, damage, health, game):
		asset = game.enemy_assets["Marauder"]
		x = random.randint(0, WIDTH - asset.get_width())
		
		base_speed = 15
		max_speed = 60
		acceleration = 5
		damage = 5
		health = 200

		super().__init__(x, y, base_speed, max_speed, acceleration, damage, health, asset)

		self.image = asset
		self.ratio = get_ratio(asset, 120, 80)

		# If you want to add engines to the ship, you can do it here
		self.engines.append(Engine(self, self.x + 20, self.y + 80, (100, 276), 0))

		# If you want to add turrets to the ship, you can do it here
		self.turretPoses.append((60, 80))
		self.laserCooldown = 1.32

	def move(self, game):
		super().move(game)

	def draw(self, screen):
		super().draw(screen)
