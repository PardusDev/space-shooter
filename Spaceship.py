import pygame as pg
from settings import *

spaceships = [
	#Name      , Asset        ,DMG
	["Sentinel", SENTINEL_PATH, 15, 0.67] # -> Sentinel 0
]

class Spaceship:
	def __init__(self, spaceship):
		self.spaceship = spaceship
		self.spaceshipName = spaceships[self.spaceship][0]
		self.image = self.scale_image(pg.image.load(spaceships[self.spaceship][1]), 120, 80)
		self.damage = spaceships[self.spaceship][2]
		self.speedMultiplier = spaceships[self.spaceship][3]
		self.width, self.height = self.image.get_size()
		self.x = (WIDTH / 2) - (self.width / 2)
		self.y = (HEIGHT - self.height) - 10

	def scale_image (self, image, target_width, target_height):
		original_width, original_height = image.get_size()

		ratio = min(target_width / original_width, target_height / original_height)
		new_width = int(original_width * ratio)
		new_height = int(original_height * ratio)

		return pg.transform.scale(image, (new_width, new_height))
	
	def move(self, player, keys, dt_seconds):
		if keys[pg.K_LEFT]:
			if (self.x >= 0):
				self.x -= (player.speed * self.speedMultiplier) * dt_seconds
		if keys[pg.K_RIGHT]:
			if (self.x + self.width <= WIDTH):
				self.x += (player.speed * self.speedMultiplier) * dt_seconds

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))

	