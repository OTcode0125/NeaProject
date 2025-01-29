import pygame
import random

from cell import Cell


pygame.init()

class Game():
    def __init__(self, difficulty):
        if difficulty == "easy":
            self.number_of_columns = 10
            self.number_of_rows = 10
            self.number_of_moles = 10
            self.square_size = 70

        elif difficulty == "hard":
            self.number_of_columns = 20
            self.number_of_rows = 20
            self.number_of_moles = 50
            self.square_size = 35

        self.total_cells = self.number_of_columns*self.number_of_rows
        self.free_cells = self.total_cells-self.number_of_moles
        self.start_ticks = pygame.time.get_ticks()

        self.cell_data = []
        for row in range(self.number_of_rows):
            self.cell_data.append([])
            for column in range(self.number_of_columns):
                self.cell_data[row].append(Cell())
        
        self.place_moles()
        self.first_click = True

        #random mole placement and first click logic
    def place_moles(self, first_click_position=None):
        mole_positions = random.sample(range(self.total_cells), self.number_of_moles)
        
        if first_click_position:
            first_click_row, first_click_column = first_click_position
            mole_positions = random.sample(range(self.total_cells - 1), self.number_of_moles)
            while (first_click_row * self.number_of_columns + first_click_column) in mole_positions:
                mole_positions = random.sample(range(self.total_cells - 1), self.number_of_moles) 

        else:
            mole_positions = random.sample(range(self.total_cells), self.number_of_moles)
        
        for pos in mole_positions:
            #maths behind converting index to a specific cell (document)
            row = pos // self.number_of_columns
            column = pos % self.number_of_columns
            self.cell_data[row][column].set_is_mole()
