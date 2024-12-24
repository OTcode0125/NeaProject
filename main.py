import pygame 

number_of_columns = 20
number_of_rows = 20
border_width = 1
square_size = 25
space_between_squares = 0
starting_position_x = 1300
starting_position_y = 300
number_of_mines = 15

pygame.font.init()
wording_font = pygame.font.SysFont("Roman", 70)

def draw_square_with_border(border_color,square_color,x,y,square_size,border_width):
    fill_size = square_size - border_width*2
    pygame.draw.rect(display, border_color, (x, y, square_size,square_size), width = border_width)
    pygame.draw.rect(display, square_color, (x + border_width, y + border_width, fill_size,fill_size))

def getting_mouse_position():
    return pygame.mouse.get_pos()

class Cell():
    def __init__(self):
        self.__color = pygame.Color("white")
        self.__is_mine = False
    def get_color(self):
        return self.__color
    def set_color(self,new_color):
        self.__color = new_color
    def set_is_mine(self):
        self.__is_mine = True


pygame.init()

display = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Minesweeper")

exit = False

clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()


cell_data = []
for row in range(number_of_rows): # 0, 1
    cell_data.append([])
    for column in range(number_of_columns):
        cell_data[row].append(Cell())

cell_data[0][8].set_is_mine()
while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
        #click control
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_x, mouse_click_y = getting_mouse_position()
            row = (mouse_click_y-starting_position_y)//square_size
            column = (mouse_click_x-starting_position_x)//square_size
            #right click
            if event.button == 3:
                cell_data[row][column].set_color(pygame.Color("blue")) 
            #left click
            elif event.button == 1:
                cell_data[row][column].set_color(pygame.Color("red"))
    display.fill(pygame.Color("grey"))
    #timer math/display
    elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000
    minutes = elapsed_time // 60
    seconds = elapsed_time % 60
    timer_text = f"{minutes:02}:{seconds:02}"
    rendered_timer_text = wording_font.render(timer_text, False, (0,0,0))
    display.blit(rendered_timer_text,(100,250))
    
    text_surface = wording_font.render("Farmsweeper", False, (0,0,0))
    display.blit(text_surface, (0,0))
    
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            cell_color = cell_data[row][column].get_color()

            draw_square_with_border(pygame.Color("black"),cell_color, starting_position_x + (square_size + space_between_squares)*column, starting_position_y + (square_size + space_between_squares)*row,square_size,border_width)





    pygame.display.update()
