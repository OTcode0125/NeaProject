import pygame 

number_of_columns = 5
number_of_rows = 3
border_width = 1
square_size = 100
space_between_squares = 5




def draw_square_with_border(border_color,square_color,x,y,square_size,border_width):
    fill_size = square_size - border_width*2
    pygame.draw.rect(display, border_color, (x, y, square_size,square_size), width = border_width)
    pygame.draw.rect(display, square_color, (x + border_width, y + border_width, fill_size,fill_size))

pygame.init()

display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Minesweeper")

exit = False

while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True


    display.fill(pygame.Color("white"))

   
    for column in range(number_of_columns):
        for row in range(number_of_rows):
            draw_square_with_border(pygame.Color("black"),pygame.Color("grey"),(square_size + space_between_squares)*column,(square_size + space_between_squares)*row,square_size,border_width)
            '''pygame.draw.rect(display, pygame.Color("black"), ((square_size + space_between_squares)*column, (square_size + space_between_squares)*row, square_size,square_size), width = border_width)
            pygame.draw.rect(display, pygame.Color("grey"), ((square_size + space_between_squares)*column + border_width, (square_size + space_between_squares)*row + border_width, fill_size,fill_size))'''




    pygame.display.update()
