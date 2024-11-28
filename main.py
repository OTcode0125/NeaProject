import pygame 
#constant
BLUE = (0,0,225)
WHITE = (255,255,255)
pygame.init() 

display = pygame.display.set_mode((500, 500))



pygame.display.set_caption("Minesweeper") 
exit = False

while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
	
    pygame.draw.rect(display,BLUE,(200,100,100,100),width=1)
    pygame.draw.rect(display,BLUE,(300,100,100,100),width=1)
  
    pygame.display.update()