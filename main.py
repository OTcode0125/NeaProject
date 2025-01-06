# main.py
import pygame

from main_menu import main_menu_screen
pygame.init()

display = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Farmsweeper")
clock = pygame.time.Clock()

current_screen = "main_menu"
running = True

#main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #decide which screen in use
    if current_screen == "main_menu":
        result = main_menu_screen(display)

    # Update the display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
