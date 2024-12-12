import pygame 

number_of_columns = 5
number_of_rows = 3
border_width = 1
square_size = 100
space_between_squares = 5
starting_position_x = 100
starting_position_y = 100

pygame.font.init()
wording_font = pygame.font.SysFont("Roman", 70)

def draw_square_with_border(border_color,square_color,x,y,square_size,border_width):
    fill_size = square_size - border_width*2
    pygame.draw.rect(display, border_color, (x, y, square_size,square_size), width = border_width)
    pygame.draw.rect(display, square_color, (x + border_width, y + border_width, fill_size,fill_size))

pygame.init()

display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Minesweeper")

exit = False

cell_colors = []
for row in range(number_of_rows): # 0, 1
    cell_colors.append([])
    for column in range(number_of_columns):
        cell_colors[row].append(pygame.Color("grey"))

cell_colors[0][0] = pygame.Color("blue")

while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
        


    display.fill(pygame.Color("white"))

    text_surface = wording_font.render("Farmsweeper", False, (0,0,0))
    display.blit(text_surface, (0,0))
   
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            cell_color = cell_colors[row][column]

            draw_square_with_border(pygame.Color("black"),cell_color, starting_position_x + (square_size + space_between_squares)*column, starting_position_y + (square_size + space_between_squares)*row,square_size,border_width)
            '''pygame.draw.rect(display, pygame.Color("black"), ((square_size + space_between_squares)*column, (square_size + space_between_squares)*row, square_size,square_size), width = border_width)
            pygame.draw.rect(display, pygame.Color("grey"), ((square_size + space_between_squares)*column + border_width, (square_size + space_between_squares)*row + border_width, fill_size,fill_size))'''




    pygame.display.update()
