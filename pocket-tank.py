import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Snake')

gameExit = False

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0
clock = pygame.time.Clock()


while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				lead_x_change = -1
				lead_y_change = 0
			elif event.key == pygame.K_RIGHT:
				lead_x_change = 1
				lead_y_change = 0

			elif event.key == pygame.K_UP:
				lead_y_change = -1
				lead_x_change = 0
			elif event.key == pygame.K_DOWN:
				lead_y_change = 1
				lead_x_change = 0

	if lead_x >= 800 or lead_x <= 0 or lead_y >= 600 or lead_y <= 0:
		gameExit = True


	lead_x += lead_x_change
	lead_y += lead_y_change

	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,5,5])
	pygame.display.update()

	clock.tick(60)






pygame.quit()
quit()