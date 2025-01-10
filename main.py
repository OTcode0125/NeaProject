import pygame
import random
import pygame_textinput

pygame.init()

display = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Farmsweeper")
clock = pygame.time.Clock()

current_screen = "main_menu"
running = True

number_of_columns = 20
number_of_rows = 20
border_width = 1
square_size = 25
space_between_squares = 0
starting_position_x = 1300
starting_position_y = 300
number_of_mines = 50
total_cells = number_of_columns*number_of_rows
free_cells = total_cells-number_of_mines


pygame.font.init()
wording_font = pygame.font.SysFont("Roman", 70)
number_font = pygame.font.SysFont("Roman", square_size -5)
def draw_square_with_border(border_color, square_color, x, y, square_size, border_width):
    fill_size = square_size - border_width * 2
    pygame.draw.rect(display, border_color, (x, y, square_size, square_size), width=border_width)
    pygame.draw.rect(display, square_color, (x + border_width, y + border_width, fill_size, fill_size))

def getting_mouse_position():
    return pygame.mouse.get_pos()
#random mine placement func / number_of_columns here and not rows bc used in lines 32,33
def random_mine_placement(cell_data, total_cells, number_of_columns, number_of_mines):
    mine_positions = random.sample(range(total_cells), number_of_mines)

    for pos in mine_positions:
        #maths behind converting index to a specific cell (document)
        row = pos // number_of_columns
        column = pos % number_of_columns
        cell_data[row][column].set_is_mine()

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
            self.set_color(pygame.Color("red"))
    
    def is_revealed(self):
        return self.__is_revealed
    
    def set_surrounding_mines(self, surrounding_mines):
        self.__surrounding_mines = surrounding_mines
    
    def get_surrounding_mines(self):
        return self.__surrounding_mines
    
class Sprites(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

pygame.init()

clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

display = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Minesweeper")

#mainmenusprites
'''mainmenuscreen = Sprites("main_menu_screen.png", 0,0, 1920,1080)
mainmenu_sprites = pygame.sprite.Group()
mainmenu_sprites.add(mainmenuscreen)'''

cell_data = []
for row in range(number_of_rows):
    cell_data.append([])
    for column in range(number_of_columns):
        cell_data[row].append(Cell())

random_mine_placement(cell_data, total_cells,number_of_columns, number_of_mines)

textinput = pygame_textinput.TextInputVisualizer()
#loop
while running:
    list_of_events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            list_of_events.append(event)
    key_press = pygame.key.get_pressed()

    #screen logic
    if current_screen == "main_menu":
        display.fill(pygame.Color("grey"))

        big_font = pygame.font.SysFont("Roman", 70)
        small_font = pygame.font.SysFont("Roman", 36)
        instruction_font = pygame.font.SysFont("Arial", 30)

        title_surface = big_font.render("FARMSWEEPER", True, (0, 0, 0))
        display.blit(title_surface, (10, 10))

        sub_title_surface = small_font.render("Discover all the cells free of the moles to win the game!", True, (0, 0, 0))
        display.blit(sub_title_surface, (10, 100))

        instruction_text = instruction_font.render("PRESS (ENTER) TO PLAY GAME AS GUEST", True, (0, 0, 0))
        display.blit(instruction_text, (650, 1000))

        login_text = big_font.render("(1)LOGIN", True, (0, 0, 0))
        display.blit(login_text, (10, 400))
        
        quit_text = big_font.render("(2)QUIT", True, (0, 0, 0))
        display.blit(quit_text, (10, 600))

        '''mainmenu_sprites.draw(display)
        
        if key_press[pygame.K_1]:
            current_screen = "log_in"
        elif key_press[pygame.K_2]:
            running = False
        elif key_press[pygame.K_RETURN]:
            current_screen = "choose_difficulty"

    elif current_screen == "log_in":
        textinput.update(list_of_events)
        display.fill(pygame.Color("grey"))

        big_font = pygame.font.SysFont("Roman", 36)
        
        title_surface = big_font.render("Login:", True, (0, 0, 0))
        display.blit(title_surface, (10, 10))

        display.blit(textinput.surface, (500,500))
    elif current_screen == "choose_difficulty":
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                current_screen = "game"

        
        display.fill(pygame.Color("grey"))

        big_font = pygame.font.SysFont("Roman", 36)
    
        title_surface = big_font.render("Difficulty:", True, (0, 0, 0))
        display.blit(title_surface, (10, 10))

    elif current_screen == "game":
        for event in list_of_events:
            # Click control
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click_x, mouse_click_y = getting_mouse_position()
                row = (mouse_click_y - starting_position_y) // square_size
                column = (mouse_click_x - starting_position_x) // square_size
                if 0 <= row < number_of_rows and 0 <= column < number_of_columns:
                    # Right click
                    if event.button == 3:
                        if not cell_data[row][column].is_revealed():
                            if not cell_data[row][column].is_flag():
                                cell_data[row][column].set_color(pygame.Color("blue"))
                                cell_data[row][column].set_flag(True)
                            else:
                                cell_data[row][column].set_flag(False)
                                cell_data[row][column].set_color(pygame.Color("white"))
                    # Left click DOCUMENT EXCEPTION HANDLING WITH FREE_CELLS
                    elif event.button == 1:
                        if not cell_data[row][column].is_revealed() and not cell_data[row][column].is_flag():
                            cell_data[row][column].reveal()
                            free_cells -= 1 
                            if not cell_data[row][column].is_mine():
                                surrounding_mines = 0
                                #bottom right
                                if row < number_of_rows-1 and column < number_of_columns-1 and cell_data[row+1][column+1].is_mine():
                                    surrounding_mines += 1
                                #bottom left
                                if row < number_of_rows-1 and column > 0 and cell_data[row+1][column-1].is_mine():
                                    surrounding_mines += 1
                                #right
                                if column < number_of_columns-1 and cell_data[row][column+1].is_mine():
                                    surrounding_mines += 1
                                #left
                                if column >0 and cell_data[row][column-1].is_mine():
                                    surrounding_mines += 1
                                #below
                                if row < number_of_rows-1 and cell_data[row+1][column].is_mine():
                                    surrounding_mines += 1
                                #top
                                if row > 0 and cell_data[row-1][column].is_mine():
                                    surrounding_mines += 1
                                #top left
                                if row >0 and column > 0 and cell_data[row-1][column-1].is_mine():
                                    surrounding_mines += 1
                                #top right
                                if row > 0 and column < number_of_columns-1 and cell_data[row-1][column+1].is_mine():
                                    surrounding_mines += 1
                                cell_data[row][column].set_surrounding_mines(surrounding_mines)
                            else:
                                print("You died")
                            
                            if free_cells == 0:
                                print("CONGRATS! YOU BEAT THE MOLES")


                            
                        
                        
                        


        display.fill(pygame.Color("grey"))

        elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        
        timer_text = f"Timer: {minutes:02}:{seconds:02}"
        rendered_timer_text = wording_font.render(timer_text, False, (0, 0, 0))
        display.blit(rendered_timer_text, (100, 250))

        title_surface = wording_font.render("Farmsweeper", False, (0, 0, 0))
        display.blit(title_surface, (0, 0))
        
        free_cells_text = f"Free Cells: {free_cells}"
        free_cells_surface = wording_font.render(free_cells_text, False, (0,0,0))
        display.blit(free_cells_surface, (100, 450))

        for row in range(number_of_rows):
            for column in range(number_of_columns):
                cell_x = starting_position_x + (square_size + space_between_squares) * column
                cell_y = starting_position_y + (square_size + space_between_squares) * row
                cell_color = cell_data[row][column].get_color()
                draw_square_with_border(pygame.Color("black"),cell_color,cell_x,cell_y,square_size,border_width)
                if cell_data[row][column].is_revealed():
                    surrounding_mines = cell_data[row][column].get_surrounding_mines()
                    if surrounding_mines > 0:
                        number_of_surrounding_mines_surface = number_font.render(str(surrounding_mines), False, (0, 0, 0))
                        display.blit(number_of_surrounding_mines_surface, (cell_x,cell_y))
                    


    pygame.display.flip()
    clock.tick(30)

pygame.quit()
