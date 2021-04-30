from main_screen import MainScreen
import pygame

# (width, height) = (1600, 1600)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# screen = pygame.display.set_mode((width, height))
pygame.display.flip()
running = True

main_screen = MainScreen(["Quit", "Continue", "New Game"])
main_screen.aff_menu(screen, 750, 700)
key = False
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
        elif key == False and event.key == pygame.K_n: 
        	key = True
        elif key == False and event.key == pygame.K_c:
          key = True
        elif event.key == pygame.K_q:
          running = False
        if key == True:
          screen.fill((0,0,0))
  pygame.display.flip()