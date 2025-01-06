import pygame
from main_menu import main_menu_screen
from login import login_screen

pygame.init()

display = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Farmsweeper")
clock = pygame.time.Clock()

current_screen = "main_menu"
running = True

#loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen logic
    if current_screen == "main_menu":
        result = main_menu_screen(display)
        if result == "log_in":
            current_screen = "log_in"
        elif result == "quit":
            running = False

    elif current_screen == "log_in":
        login_screen(display)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
