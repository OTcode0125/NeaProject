import pygame

def choose_difficulty_screen(display):
    display.fill(pygame.Color("grey"))

    big_font = pygame.font.SysFont("Roman", 36)
    
    title_surface = big_font.render("Difficulty:", True, (0, 0, 0))
    display.blit(title_surface, (10, 10))
