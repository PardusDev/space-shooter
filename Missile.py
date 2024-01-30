from utilities import *

class Missile:
	def __init__(self, x, y, rotation, speed, damage, image):
		self.x = x
		self.y = y
		self.rotation = rotation
		self.speed = speed
		self.damage = damage
		self.image = image

		self.width, self.height = self.image.get_size()

	def move(self, dt_seconds):
		self.y -= self.speed * dt_seconds

	def collide(self, enemy):
		return pg.Rect(self.x, self.y, self.width, self.height).colliderect(pg.Rect(enemy.x, enemy.y, enemy.width, enemy.height))

	def update(self, dt_seconds):
		self.move(dt_seconds)

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))

class RB4(Missile):
	def __init__(self, game, x, y, speed, damage):
		rotation = 270
		speed = 300
		damage = 50
		image = scale_image(pg.transform.rotate(game.missiles["rb4"], rotation), 20, 20)

		super().__init__(x, y, rotation, speed, damage, image)

	def collide(self, enemy):
		return super().collide(enemy)

	def update(self, dt_seconds):
		super().update(dt_seconds)

	def draw(self, screen):
		super().draw(screen)


