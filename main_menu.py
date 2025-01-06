import pygame

def main_menu_screen(display):
    display.fill(pygame.Color("lightblue"))

    font = pygame.font.SysFont("Roman", 70)
    title_surface = font.render("fARMSWEEPER", True, (0, 0, 0))
    display.blit(title_surface, (400, 100))

    instruction_font = pygame.font.SysFont("Arial", 50)
    instruction_text = instruction_font.render("Press Enter to Start the Game", True, (0, 0, 0))
    display.blit(instruction_text, (500, 400))

    '''keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        return (needs to be made into game_code)

    return "main_menu"'''
