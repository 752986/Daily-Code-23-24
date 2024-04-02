# Fishing minigame based on stardew valley fishing using model-view-controller pattern

import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.surface import Surface


# config:
FRAMERATE = 60
SCREEN_SIZE = Vector2(1200, 800)
PADDLE_SIZE = 0.2


# pygame init:
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Fishing Game")


# definitions:
class FishingGame:
	WIDTH = 64
	HEIGHT = 500
	PROGRESS_WIDTH = 12
	PADDING = 8

	# model:
	progress: float
	fishPos: float
	paddlePos: float
	pos: Vector2

	def __init__(self, pos: Vector2):
		self.progress = 0.25
		self.fishPos = 0.0
		self.paddlePos = 0.0
		self.pos = pos

	# view:
	def draw(self, surface: Surface):
		# static elements
		borderBox = Rect(
			self.pos, 
			Vector2(
				self.WIDTH, 
				self.HEIGHT
			)
		)

		fishBox = Rect(
			self.pos + Vector2(self.PADDING), 
			Vector2(
				self.WIDTH - self.PROGRESS_WIDTH - self.PADDING * 2, 
				self.HEIGHT - self.PADDING * 2
			)
		)

		progressBox = Rect(
			fishBox.topright,
			Vector2(
				self.PROGRESS_WIDTH,
				self.HEIGHT - self.PADDING * 2
			)
		)

		pygame.draw.rect(surface, "#b9b9b9", borderBox) # background / border
		pygame.draw.rect(surface, "#1f9ecd", fishBox) # water background
		pygame.draw.rect(surface, "#9e9e9e", progressBox) # progress background

		# dynamic elements
		progressHeight = progressBox.height * self.progress
		progressBar = Rect(
			Vector2(
				progressBox.left,
				progressBox.top + (progressBox.height - progressHeight)
			),
			Vector2(
				self.PROGRESS_WIDTH,
				progressHeight
			)
		)

		paddleHeight = PADDLE_SIZE * fishBox.height
		paddleY = (fishBox.height - paddleHeight) * (1 - self.paddlePos)
		paddleBox = Rect(
			Vector2(
				fishBox.left,
				fishBox.top + paddleY
			),
			Vector2(
				fishBox.width,
				paddleHeight
			)
		)

		#TODO: make this code work with arbitrary height fish images
		fishY = fishBox.height * (1 - self.paddlePos)
		fish = Rect(
			Vector2(
				fishBox.left,
				fishBox.top + fishY
			),
			Vector2(
				fishBox.width,
				4
			)
		)

		pygame.draw.rect(surface, "#f5b700", progressBar) # progress bar
		pygame.draw.rect(surface, "#24bd75", paddleBox) # paddle
		pygame.draw.rect(surface, "#ac85cf", fish) # fish

	# controller:
	def update(self, delta: float):
		


def main():
	# game setup:
	clock = pygame.time.Clock()
	game = FishingGame(Vector2(32, 32))

	# main loop:
	running = True
	while running:
		delta = clock.tick(FRAMERATE) / 1000

		# input:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# draw:
		screen.fill("#000000")
		game.draw(screen)

		pygame.display.flip()

if __name__ == "__main__":
	main()
