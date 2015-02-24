import pygame
#import OpenGL
from pygame.locals import *
import sys

# init pygame

pygame.init()
pygame.mixer.init()

# variables classes functions

windowSize = (640, 480)
screen = pygame.display.set_mode(windowSize, DOUBLEBUF)

helloWorld = pygame.image.load("M:\Semester 2 Group Project\groupPygame\link.png")
helloWorldSize = helloWorld.get_size()

running = 1
pygame.display.set_caption("python app")
#pygame.mouse.set_visible(0)

UP, DOWN, LEFT, RIGHT = 0, 0, 0, 0

x, y = 0, 0
xSpeed, ySpeed = 5, 5

clock = pygame.time.Clock()

while running:

	# ensures the game runns at no more than 30 fps
	clock.tick(40)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = 0
			sys.exit()
		# pocess key presses
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				LEFT = 1
			if event.key == pygame.K_RIGHT:
				RIGHT = 1
			if event.key == pygame.K_UP:
				UP = 1
			if event.key == pygame.K_DOWN:
				DOWN = 1
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				LEFT = 0
			if event.key == pygame.K_RIGHT:
				RIGHT = 0
			if event.key == pygame.K_UP:
				UP = 0
			if event.key == pygame.K_DOWN:
				DOWN = 0


	# clear the screen a colour
	screen.fill((0, 0, 0))

	mousePosition = pygame.mouse.get_pos()

	if RIGHT:
		x += xSpeed
	if LEFT:
		x -= xSpeed
	if DOWN:
		y += ySpeed
	if UP:
		y -= ySpeed

	if x + helloWorldSize[0] > windowSize[0]:
		x = windowSize[0] - helloWorldSize[0]
	elif x < 0:
		x = 0

	if y + helloWorldSize[1] > windowSize[1]:
		y = windowSize[1] - helloWorldSize[1]
	elif y < 0:
		y = 0

	#if x + helloWorldSize[0] > windowSize[0] or x < 0:
	#	xSpeed *= -1

	#if y + helloWorldSize[1] > windowSize[1] or y < 0:
	#	ySpeed *= -1

	screen.blit(helloWorld, (x, y))

	# update the screen
	pygame.display.update()