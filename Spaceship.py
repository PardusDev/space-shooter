import pygame as pg
from Engine import *
from Laser import *
from utilities import *
from settings import *

spaceships = [
	#Name      , Asset        ,DMG,  SPD, TURRET POSITIONS      , CLDW, ENGINE POS
	["Sentinel", SENTINEL_PATH, 15, 0.81, [(135, 79), (211, 79)], 0.26   , [(83, 240), (269, 240), (140, 280), (215, 280)], ENGINE_PATH], # -> Sentinel 0
	["Vanguard", VANGUARD_PATH, 20, 0.97, [(104, 23), (182, 23)], 0.11, [(100, 276), (197, 276)], ENGINE_PATH] # -> Vanguard 1
]

class Spaceship:
	def __init__(self, spaceship):
		self.spaceship = spaceship
		self.spaceshipName = spaceships[self.spaceship][0]
		self.image = scale_image(pg.image.load(spaceships[self.spaceship][1]), 120, 80)
		self.ratio = get_ratio(pg.image.load(spaceships[self.spaceship][1]), 120, 80)
		self.damage = spaceships[self.spaceship][2]
		self.speedMultiplier = spaceships[self.spaceship][3]
		self.width, self.height = self.image.get_size()
		self.x = (WIDTH / 2) - (self.width / 2)
		self.y = (HEIGHT - self.height) - 40
		

		# Weapons
		self.lasers = []
		self.turretPoses = spaceships[self.spaceship][4]
		self.laserCooldown = spaceships[self.spaceship][5]
		self.last_fired_time = 0
		

		# Engines
		self.engines = []
		self.enginePoses = spaceships[self.spaceship][6]

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

	def fire(self, player):
		current_time = pg.time.get_ticks() / 1000.0
		if current_time - self.last_fired_time >= self.laserCooldown:
			keys = pg.key.get_pressed()
			if keys[pg.K_UP]:
				for xy in self.turretPoses:
					turretX, turretY = xy
					turretX = self.x + (turretX * self.ratio)
					turretY = self.y + (turretY * self.ratio)
					self.lasers.append(Laser(turretX, turretY, self.damage))
				
				self.last_fired_time = current_time

	def update(self):
		for engine in self.engines:
			engine.update()

		for laser in self.lasers:
			if (laser.y < 0):
				self.lasers.remove(laser)
			else:
				laser.update()

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))

		for laser in self.lasers:
			laser.draw(screen)

		for engine in self.engines:
			engine.draw(screen)

	