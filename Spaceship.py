import pygame as pg
from Engine import *
from Laser import *
from utilities import *
from settings import *


class Spaceship:
	def __init__(self, spaceshipName, image, ratio):
		self.spaceshipName = spaceshipName
		self.image = image
		self.ratio = ratio
		self.damage = None # -> It will be set in the child class
		self.speedMultiplier = None # -> It will be set in the child class
		self.width, self.height = self.image.get_size()
		self.x = (WIDTH / 2) - (self.width / 2)
		self.y = (HEIGHT - self.height) - 40
		

		# Weapons
		self.lasers = []
		self.last_fired_time = 0
		

		# Engines
		self.engines = []
	
	def set_engines(self):
		for enginePos in self.enginePoses:
			enginePosX, enginePosY = enginePos
			enginePosX = self.x + (enginePosX * self.ratio)
			enginePosY = self.y + (enginePosY * self.ratio)
			self.engines.append(Engine(self, enginePosX, enginePosY, enginePos, 180))
	
	def move(self, player, dt_seconds):
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT]:
			if (self.x >= 0):
				self.x -= (player.speed * self.speedMultiplier) * dt_seconds
					
		if keys[pg.K_RIGHT]:
			if (self.x + self.width <= WIDTH):
				self.x += (player.speed * self.speedMultiplier) * dt_seconds

		for engine in self.engines:
			engine.move(self)

	def fire(self, player, game):
		current_time = pg.time.get_ticks() / 1000.0
		if current_time - self.last_fired_time >= self.laserCooldown:
			keys = pg.key.get_pressed()
			if keys[pg.K_UP]:
				for xy in self.turretPoses:
					turretX, turretY = xy
					turretX = self.x + (turretX * self.ratio)
					turretY = self.y + (turretY * self.ratio)
					self.lasers.append(Laser(turretX, turretY, self.damage, self))
				game.sound_effects["ally_laser"].play()
				
				self.last_fired_time = current_time

				# For debug
				# player.player_lost_health(self.damage)
			
			# For debug
			# if(keys[pg.K_DOWN]):
			# 	player.player_get_health(10)
		
		

	def update(self, dt_seconds):
		for engine in self.engines:
			engine.update()

		for laser in self.lasers:
			if (laser.y < 0):
				self.lasers.remove(laser)
			else:
				laser.update(dt_seconds)

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))

		for laser in self.lasers:
			laser.draw(screen)

		for engine in self.engines:
			engine.draw(screen)


class Sentinel(Spaceship):
	def __init__(self):
		image, ratio = scale_image_and_get_ratio(pg.image.load(SENTINEL_PATH), 120, 80)
		super().__init__("Sentinel", image, ratio)
		self.damage = 20
		self.speedMultiplier = 0.97

		# Lasers
		self.basic_laser_frames = [scale_and_rot_image(pg.image.load(f"assets/laser/ally_basic_laser/sprite_{i:02d}.png"), self.ratio / 4, (0)) for i in range(23)]
		self.turretPoses = [(135, 79), (211, 79)]
		self.laserCooldown = 0.18

		# Engines
		self.enginePoses = [(83, 240), (269, 240), (140, 280), (215, 280)]

		self.set_engines()
	
class Vanguard(Spaceship):
	def __init__(self):
		image, ratio = scale_image_and_get_ratio(pg.image.load(VANGUARD_PATH), 120, 80)
		super().__init__("Vanguard", image, ratio)
		self.damage = 15
		self.speedMultiplier = 0.81

		# Lasers
		self.basic_laser_frames = [scale_and_rot_image(pg.image.load(f"assets/laser/ally_basic_laser/sprite_{i:02d}.png"), self.ratio / 4, (0)) for i in range(23)]
		self.turretPoses = [(104, 23), (182, 23)]
		self.laserCooldown = 0.11

		# Engines
		self.enginePoses = [(100, 276), (197, 276)]

		self.set_engines()
		