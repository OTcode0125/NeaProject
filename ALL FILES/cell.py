#imports
import pygame


pygame.init()
#cell class is used to control cell behavior on the grid. e.g. set it as a mine or set it as flagged.
class Cell():
    def __init__(self):
        self.__color = pygame.Color("white")
        self.__is_mole = False
        self.__is_revealed = False
        self.__surrounding_moles = 0
        self.__flag = False

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def set_is_mole(self):
        self.__is_mole = True

    def is_mole(self):
        return self.__is_mole

    def set_flag(self, flag):
        self.__flag = flag
        
    def is_flag(self):
        return self.__flag
    
    def reveal(self):
        self.__is_revealed = True
        if self.is_mole():
            self.set_color(pygame.Color("black"))  # Mark mole cell
        else:
            self.set_color(pygame.Color("grey"))
    
    def is_revealed(self):
        return self.__is_revealed
    
    def set_surrounding_moles(self, surrounding_moles):
        self.__surrounding_moles = surrounding_moles
    
    def get_surrounding_moles(self):
        return self.__surrounding_moles
