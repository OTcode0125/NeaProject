import pygame

def main_menu_screen(display):
    display.fill(pygame.Color("grey"))

    big_font = pygame.font.SysFont("Roman", 70)
    small_font = pygame.font.SysFont("Roman", 36)
    instruction_font = pygame.font.SysFont("Arial", 30)

    title_surface = big_font.render("FARMSWEEPER", True, (0, 0, 0))
    display.blit(title_surface, (10,10))

    sub_title_surface = small_font.render("Discover all the cells free of the moles to win the game!", True, (0,0,0))
    display.blit(sub_title_surface, (10,100))

    instruction_text = instruction_font.render("PRESS (ENTER) TO PLAY GAME AS GUEST", True, (0, 0, 0))
    display.blit(instruction_text, (650, 1000))

    '''keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        return (needs to be made into game_code)

    return "main_menu"'''
