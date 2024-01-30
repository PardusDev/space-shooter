import pygame as pg
import random
from settings import *

def scale_image (image, target_width, target_height):
		original_width, original_height = image.get_size()

		ratio = min(target_width / original_width, target_height / original_height)
		new_width = int(original_width * ratio)
		new_height = int(original_height * ratio)

		return pg.transform.scale(image, (new_width, new_height))
	
def get_ratio (image, target_width, target_height):
	original_width, original_height = image.get_size()

	ratio = min(target_width / original_width, target_height / original_height)

	return ratio

def scale_image_and_get_ratio (image, target_width, target_height):
		original_width, original_height = image.get_size()

		ratio = min(target_width / original_width, target_height / original_height)
		new_width = int(original_width * ratio)
		new_height = int(original_height * ratio)

		return pg.transform.scale(image, (new_width, new_height)), ratio

def scale_and_rot_image (image, ratio, rotation):
	original_width, original_height = image.get_size()

	new_width = int(original_width * ratio)
	new_height = int(original_height * ratio)

	return pg.transform.rotate(pg.transform.scale(image, (new_width, new_height)), rotation)

def get_random_pos_for_enemies():
	# The coordinates of -500, -100 have been changed for debugging.
	return random.randrange(10, WIDTH - 100), random.randrange(-200, -10)

def blit_text(surface, text, pos, font, color=pg.Color('black'), max_width = None, max_height = None):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    if (max_width is None or max_height is None):
        max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height