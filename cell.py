import pygame


pygame.init()

class Cell():
    def __init__(self):
        self.__color = pygame.Color("white")
        self.__is_mine = False
        self.__is_revealed = False
        self.__surrounding_mines = 0
        self.__flag = False

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def set_is_mine(self):
        self.__is_mine = True

    def is_mine(self):
        return self.__is_mine

    def set_flag(self, flag):
        self.__flag = flag
        
    def is_flag(self):
        return self.__flag
    
    def reveal(self):
        self.__is_revealed = True
        if self.is_mine():
            self.set_color(pygame.Color("black"))  # Mark mine cell
        else:
            self.set_color(pygame.Color("grey"))
    
    def is_revealed(self):
        return self.__is_revealed
    
    def set_surrounding_mines(self, surrounding_mines):
        self.__surrounding_mines = surrounding_mines
    
    def get_surrounding_mines(self):
        return self.__surrounding_mines
