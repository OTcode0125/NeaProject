import pygame
import random

from cell import Cell


pygame.init()
#game class used to re-initialise the grid of cells, and allows changing difficulty.
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
        self.first_click = True

        self.cell_data = []
        for row in range(self.number_of_rows):
            self.cell_data.append([])
            for column in range(self.number_of_columns):
                self.cell_data[row].append(Cell())
        
        self.first_click = True

        #random mole placement and no death on first click
    def place_moles(self, first_click_position):
        

        first_click_row, first_click_column = first_click_position
        first_click_index = first_click_row * self.number_of_columns + first_click_column
        

        surrounding_cells = set()
        #update first click logic (done)
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                row, col = first_click_row + r, first_click_column + c
                if 0 <= row < self.number_of_rows and 0 <= col < self.number_of_columns:
                    surrounding_cells.add(row * self.number_of_columns + col)
        
        mole_positions = random.sample(range(self.total_cells), self.number_of_moles)

        #no mole placement on first click or the surrounding cells
        while any(pos in surrounding_cells for pos in mole_positions):
            mole_positions = random.sample(range(self.total_cells), self.number_of_moles)

        for pos in mole_positions:
            row = pos // self.number_of_columns
            column = pos % self.number_of_columns
            self.cell_data[row][column].set_is_mole()
