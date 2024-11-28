import pygame
import make_screen
import sys


def main_menu():
    pygame.init()
    #make my main display
    display = pygame.display.set_mode((make_screen.full_screen_width, make_screen.full_screen_height))
    display.fill((255,255,255))
    pygame.display.set_caption("Main Menu")

    wording_font = pygame.font.SysFont("Roman", 72)
    #make small screen that goes ontop
    small_screen = make_screen.Screen(500, 1000, "Main Menu")
    small_screen.fill((1, 1, 1))

#creating menu buttons

    main_menu_buttons = [
        make_screen.Button("Login",50,250,wording_font)
    ]

    #main loop that keeps the window open
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.fill((255,255,255))
        small_screen.fill((1,1,1))

    
        display.blit(small_screen.screen, (1400, 40))

        title_draw = wording_font.render("FARMSWEEPER", True, "Black")
        display.blit(title_draw, (50,50))

        for i in main_menu_buttons:
            i.draw(display)

        # Update the display
        pygame.display.flip()

    pygame.quit()

main_menu()
