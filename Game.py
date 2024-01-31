import pygame as pg

from Background import *
from Wave import *
from MainMenuScreen import *
from Enemy import *
from Interface import *
from Player import *

class Game:
	def __init__(self):
		pg.init()
		# It is created in the button class
		# self.iconFont = pg.font.Font("assets/fonts/icons.ttf", 18)
		self.space_assets = {
			"white_dot": pg.image.load(WHITE_DOT_PATH),
			"star": pg.image.load(STAR_PATH),
		}

		self.enemy_spaceships = {
			"Marauder": pg.transform.rotate(pg.image.load(MARAUDER_PATH), 180),
		}

		self.ally_spaceships = {
			"Sentinel": pg.image.load(SENTINEL_PATH),
			"Vanguard": pg.image.load(VANGUARD_PATH)
		}

		self.sound_effects = {
			"enemy_laser": pg.mixer.Sound("assets/sounds/basic_laser/enemy_laser_effect.ogg"),
			"ally_laser": pg.mixer.Sound("assets/sounds/basic_laser/ally_laser_effect.ogg"),
			"radio_noise": pg.mixer.Sound(RADIO_NOISE_PATH)
		}

		self.ui = {
			"main-bg": pg.image.load(MAIN_MENU_BACKGROUND),
			"shop-bg": pg.image.load(SETTINGS_MENU_BACKGROUND),
			"settings-bg": pg.image.load(SETTINGS_MENU_BACKGROUND),
			

			"start_button": pg.image.load(START_BUTTON_BACKGROUND),
			"other_main_menu_button": pg.image.load(OTHER_MAIN_MENU_BUTTON_BACKGROUND),
			"dialogue_bg": pg.image.load(DIALOG_SPLASH),
			"dialogue_header": pg.image.load(DIALOG_SPLASH_HEADER),
			"dialogue_button": pg.image.load(DIALOG_SPLASH_BUTTON),

			"back_button": pg.image.load(BACK_BUTTON),

			"health_bar_bg": pg.image.load(HEALTH_BAR_BACKGROUND),
			"health_bar_bg_mask": pg.image.load(HEALTH_BAR_BACKGROUND_MASK),
			"health_bar_left_block": pg.image.load(HEALTH_BAR_LEFT_BLOCK),
		}

		self.laser_assets = {
			"basic": [pg.image.load(f"assets/laser/ally_basic_laser/sprite_{i:02d}.png") for i in range(23)]
		}

		self.engine_assets = {
			"basic": [pg.image.load(f"assets/engine_effects/{i:02d}_vanguard.png") for i in range(32)]
		}

		self.missiles = {
			"rb4": pg.image.load(RB4_PATH),
		}

		self.fonts = {
			
			"sys-16": pg.font.SysFont(None, 16),
			"sys-20": pg.font.SysFont(None, 20),
			"sys-24": pg.font.SysFont(None, 24),

			# Icon
			"icon-18": pg.font.Font("assets/fonts/icons.ttf", 18)
		}
		self.mainmenu = MainMenuScreen(self)

		# Because it has an interface screen, we are creating it from the beginning. Even if it's in the main menu, the interface will have been formed in the background.
		self.interface = Interface(self)
		self.clock = pg.time.Clock()
		self.running = True


		self.bg_assets = []

	def run(self):
		while self.running:
			if self.mainmenu is not None:
				self.mainmenu.draw(self.interface.screen)
				self.mainmenu.update()

			self.dt = game.clock.tick(60)
			self.dt_seconds = self.dt / 1000.0
				
			pg.display.update()


	def play(self):
		self.mainmenu = None
		self.player = Player(self.interface, self)
		self.wave = Wave(self)
		self.background = Background(self)
		
		self.enemies = []

		# Like wave-based enemies
		
		# Countdown code
		
		# Start wave
		self.wave.next_wave_start()

		while self.running:
			# Attention! For debug
			# print(len(self.enemies))
			

			self.dt = game.clock.tick(60)
			self.dt_seconds = self.dt / 1000.0
			self.interface.screen.fill((11, 11, 11))

			self.background.draw()
			self.background.update()

			# For dialogue or merchant window
			self.wave.draw()
			self.wave.update()
			
			self.player.draw(self.interface.screen)
			self.player.update(self)

			
			

			for enemy in self.enemies:
				enemy.draw(self.interface.screen)
				enemy.update(self)
				
				# Enemy's laser to player collision
				for laser in enemy.lasers:
					if laser.collide(self.player.spaceship):
						# Damage player
						self.player.player_lost_health(laser.damage)
						
						# Remove laser
						enemy.lasers.remove(laser)

				# Player's laser to enemy collision
				for laser in self.player.spaceship.lasers:
					if laser.collide(enemy):
						# TODO: Add sound effect
						# Damage enemy
						enemy.health -= laser.damage
						
						# Remove enemy if health is 0
						if (enemy.health <= 0):
							self.enemies.remove(enemy)

							if (len(self.enemies) <= 0):
								self.wave.current_wave_end()
						
						# Remove laser
						self.player.spaceship.lasers.remove(laser)

				# Player's missiles to enemy collision
				for missile in self.player.spaceship.missiles:
					if missile.collide(enemy):
						# TODO: Add sound effect
						enemy.health -= missile.damage

						if (enemy.health <= 0):
							self.enemies.remove(enemy)

							if (len(self.enemies) <= 0):
								self.wave.current_wave_end()

							self.player.spaceship.missiles.remove(missile)

			self.interface.draw(self.player)
			self.interface.update(self)
			pg.display.update()

	def end_game(self):
		self.running = False
		self.game_over = True

		while self.game_over:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					self.running = False
					self.game_over = False
				elif event.type == pg.KEYDOWN:
					self.running = True
					self.game_over = False
					# Reset game


					self.mainmenu = MainMenuScreen(self)
					self.run()
			

			self.interface.screen.fill((11, 11, 11))
			self.interface.screen.blit(self.ui["shop-bg"], (0, 0))

			self.interface.screen.blit(self.fonts["sys-24"].render("GAME OVER", True, (255, 255, 255)), (WIDTH / 2 - 100, HEIGHT / 2 - 100))
			self.interface.screen.blit(self.fonts["sys-24"].render("Press any key to continue...", True, (255, 255, 255)), (WIDTH / 2 - 100, HEIGHT / 2 - 50))

			pg.display.update()



	def quit(self):
		self.running = False

			

game = Game()
game.run()