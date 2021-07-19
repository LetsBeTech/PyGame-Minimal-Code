import pygame
pygame.init()

#Colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#Creating game window
screen_width = 900
screen_height = 500
GameWindow = pygame.display.set_mode((screen_width,screen_height))

#Game specific variables
exit_game = False
game_over = False

#Game Loop

while not exit_game:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        exit_game = True

pygame.quit()
quit()
