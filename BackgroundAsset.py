from utilities import *

class BackgroundAsset:
	def __init__(self, x, y, asset, scale, opacity):
		self.x, self.y = x, y
		self.asset = scale_and_rot_image(asset, scale, 0)
		self.scale = scale
		self.opacity = opacity

		# Setting opacity
		self.asset.set_alpha(self.opacity)

	def move(self, dt_seconds):
		self.y += 100 * dt_seconds * self.scale
		if self.y > HEIGHT:
			self.y = -30
	
	def update(self, dt_seconds):
		self.move(dt_seconds)

	def draw(self, screen):
		screen.blit(self.asset, (self.x, self.y))