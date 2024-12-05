import pygame 

# constants
BLUE = (0, 0, 225)
WHITE = (255, 255, 255)

pygame.init()

display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Minesweeper")

exit = False

while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True


    display.fill(WHITE)

    pygame.draw.rect(display, BLUE, (100, 100, 100, 100), width=1)#Row 1, 
    pygame.draw.rect(display, BLUE, (205, 100, 100, 100), width=1)
    pygame.draw.rect(display, BLUE, (310, 100, 100, 100), width=1)

    pygame.draw.rect(display, BLUE, (100, 205, 100, 100), width=1)#Row 2, 
    pygame.draw.rect(display, BLUE, (205, 205, 100, 100), width=1) 
    pygame.draw.rect(display, BLUE, (310, 205, 100, 100), width=1)  

    pygame.draw.rect(display, BLUE, (100, 310, 100, 100), width=1)#Row 3
    pygame.draw.rect(display, BLUE, (205, 310, 100, 100), width=1)  
    pygame.draw.rect(display, BLUE, (310, 310, 100, 100), width=1)  

    pygame.display.update()
