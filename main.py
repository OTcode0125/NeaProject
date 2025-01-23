import pygame
import random
import pygame_textinput

pygame.init()

display = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Farmsweeper")
clock = pygame.time.Clock()
current_screen = "initial_screen"
running = True

number_of_columns = 20
number_of_rows = 20
border_width = 1
square_size = 35
space_between_squares = 0
starting_position_x = 600
starting_position_y = 190
number_of_mines = 50
total_cells = number_of_columns*number_of_rows
free_cells = total_cells-number_of_mines
logintext = pygame_textinput.TextInputVisualizer()
passwordtext = pygame_textinput.TextInputVisualizer()
current_input_choice = "login"
game_over = False

pygame.font.init()
wording_font = pygame.font.Font("bubble_font.ttf", 50)
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

def init_game():
    global cell_data, number_of_columns, number_of_rows, number_of_mines, free_cells, total_cells

    #reset grid variables
    number_of_columns = 20
    number_of_rows = 20
    number_of_mines = 30
    total_cells = number_of_columns * number_of_rows
    free_cells = total_cells - number_of_mines

    #re init grid
    cell_data = []
    for row in range(number_of_rows):
        cell_data.append([])
        for column in range(number_of_columns):
            cell_data[row].append(Cell())

    #random mine placement
    random_mine_placement(cell_data, total_cells, number_of_columns, number_of_mines)

def read_tutorial_txt_files(file_path):
    with open(file_path,"r") as file:
        return file.readlines()
    
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
    
class Sprites(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)


    
#mainmenusprites
initialscreen = Sprites("main_menu_screen.png", 0,0, 1920,1080)
esc = Sprites("esc.png",10,10, 100,100)
initialscreen_sprites = pygame.sprite.Group()
initialscreen_sprites.add(initialscreen, esc)
pygame.init()
#universally used spites
generalscreen = Sprites("general_screen.png",0,0,1920,1080)
universal_sprites = pygame.sprite.Group()
universal_sprites.add(generalscreen,esc)
#game screen sprites
timer = Sprites("timer.png",50,10,50,50)
mole = Sprites("mole.png",1500,10,50,50)
gamesprites = pygame.sprite.Group()
gamesprites.add(generalscreen,timer,mole)

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
    if current_screen == "initial_screen":
        init_game()
        initialscreen_sprites.draw(display)

        instruction_text = wording_font.render("PRESS (ENTER) TO START", True, (0, 0, 0))
        display.blit(instruction_text, (600, 1000))

        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                current_screen = "main_menu"
#main menu screen
    elif current_screen == "main_menu":

        universal_sprites.draw(display)

        main_menu_text = wording_font.render("MAIN MENU SCREEN", True, (0,0,0))
        display.blit(main_menu_text,(650,10))

        login_text = wording_font.render("PRESS 1 (LOGIN)", True, (255,255,255))
        display.blit(login_text,(150,300))
        
        tutorial_text = wording_font.render("PRESS 2 (TUTORIAL)", True, (255,255,255))
        display.blit(tutorial_text,(150,450))

        play_as_guest = wording_font.render("PRESS (ENTER) TO PLAY AS GUEST", True, (0,0,0))
        display.blit(play_as_guest, (500,1000))
        if key_press[pygame.K_1]:
            current_screen = "log_in"
        if key_press[pygame.K_ESCAPE]:
            running = False
        if key_press[pygame.K_2]:
            current_screen = "tutorial"
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                current_screen = "choose_difficulty"
        
#login screen
    elif current_screen == "log_in":
        list_of_text_events = []
        for event in list_of_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    current_screen = "create_login"
                elif event.key != pygame.K_TAB:
                    list_of_text_events.append(event)
                else:
                    #pressing tab changes from login to password visa versa
                    if current_input_choice == "login":
                        current_input_choice = "password"
                    elif current_input_choice == "password":
                        current_input_choice = "login"
        
        if current_input_choice == "login":
            logintext.update(list_of_text_events)
        
        elif current_input_choice == "password":
            passwordtext.update(list_of_text_events)
        
        universal_sprites.draw(display)
        
        title_surface = wording_font.render("LOGIN SCREEN", True, (0, 0, 0))
        display.blit(title_surface, (700, 10))

        username_text_surface = wording_font.render("Enter Username:", True, (0,0,0))
        display.blit(username_text_surface,(300,400))

        password_text_surface = wording_font.render("Enter Password", True, (0,0,0))
        display.blit(username_text_surface,(300,500))

        create_account_text = wording_font.render("PRESS (CTRL) TO CREATE A NEW ACCOUNT", True, (0, 0, 0))
        display.blit(create_account_text, (300, 1000))


        display.blit(logintext.surface, (850,420))
        display.blit(passwordtext.surface, (850,520))
        
        if key_press[pygame.K_ESCAPE]:
            running = False

        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                entered_username = logintext.value.strip()
                entered_password = passwordtext.value.strip()

                #open txt file
                try:
                    with open("users.txt", "r") as file:
                        valid_credentials = False
                        for line in file:
                            username, password = line.strip().split(":")
                            if entered_username == username and entered_password == password:
                                valid_credentials = True
                                break

                    if valid_credentials:
                        current_screen = "logged_in_screen"
                    else:
                        current_screen = "failed_login"

                except FileNotFoundError:
                    print("Error: User data file not found.")


    elif current_screen == "logged_in_screen":
        universal_sprites.draw(display)

        logged_in_text = wording_font.render(f"HEY {username} YOU ARE LOGGED IN", True,(0,0,0))
        display.blit(logged_in_text,(400,10))

        proceed_text = wording_font.render("PRESS (ENTER) TO PROCEED TO DIFFICULTY SCREEN", True,(0,0,0))
        display.blit(proceed_text,(200,1000))

        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                current_screen = "choose_difficulty"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                current_screen = "initial_screen"
    
    elif current_screen == "create_login":
        list_of_text_events = []
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key != pygame.K_TAB:
                list_of_text_events.append(event)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                current_input_choice = "password" if current_input_choice == "login" else "login"

        if current_input_choice == "login":
            logintext.update(list_of_text_events)
        elif current_input_choice == "password":
            passwordtext.update(list_of_text_events)

        universal_sprites.draw(display)
        
        title_surface = wording_font.render("CREATE NEW ACCOUNT", True, (0, 0, 0))
        display.blit(title_surface, (700, 10))

        title_surface = wording_font.render("PRESS (TAB) TO SWAP BETWEEN USERNAME AND PASSWORD", True, (0, 0, 0))
        display.blit(title_surface, (100, 1000))

        username_text_surface = wording_font.render("Enter New Username:", True, (0, 0, 0))
        display.blit(username_text_surface, (230, 400))

        password_text_surface = wording_font.render("Enter New Password:", True, (0, 0, 0))
        display.blit(password_text_surface, (230, 500))

        display.blit(logintext.surface, (950, 420))
        display.blit(passwordtext.surface, (950, 520))

        if key_press[pygame.K_ESCAPE]:
            running = False

        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                new_username = logintext.value.strip()
                new_password = passwordtext.value.strip()
#making sure the input not empty 
                if new_username and new_password:
                    try:
                        with open("users.txt", "a") as file:
                            file.write(f"\n{new_username}:{new_password}")
                        current_screen = "log_in"
                    except Exception as e:
                        print(f"Error saving new account: {e}")
                else:
                    print("Error: Username and password cannot be empty.")


        
    
    elif current_screen == "tutorial":
        universal_sprites.draw(display)

        tut_welcome_text = wording_font.render("WELCOME TO THE TUTORIAL", True, (0,0,0))
        display.blit(tut_welcome_text,(500,10))

        tutorial_text_1 = read_tutorial_txt_files("tut.txt")

        tutorial_txt_x_pos = 100
        tutorial_txt_y_pos = 200
        space_between_lines = 5

        for line in tutorial_text_1:
            rendered_line = wording_font.render(line.strip(), True, (0,0,0))
            display.blit(rendered_line, (tutorial_txt_x_pos, tutorial_txt_y_pos))
            tutorial_txt_y_pos += space_between_lines


        if key_press[pygame.K_ESCAPE]:
            current_screen = "initial_screen"



    elif current_screen == "choose_difficulty":
        universal_sprites.draw(display)
        
        easy_selection_text = wording_font.render("PRESS (1) FOR EASY", True, (255, 255, 255))
        display.blit(easy_selection_text, (150, 300))

        hard_selection_text = wording_font.render("PRESS (2) FOR HARD", True, (255, 255, 255))
        display.blit(hard_selection_text, (150, 400))

        for event in list_of_events:
            if event.type == pygame.KEYDOWN:
#easy difficulty
                if event.key == pygame.K_1:
                    #having to reinitialse cell data so that the variables can change
                    init_game()
                    number_of_columns = 10
                    number_of_rows = 10
                    number_of_mines = 25
                    square_size = 70
                    game_over = False
                    start_ticks = pygame.time.get_ticks()
                    random_mine_placement(cell_data, number_of_columns * number_of_rows, number_of_columns, number_of_mines)
                    current_screen = "game"
#hard difficulty
                elif event.key == pygame.K_2:
                    init_game()
                    number_of_columns = 20
                    number_of_rows = 20
                    number_of_mines = 50
                    square_size = 35
                    game_over = False
                    start_ticks = pygame.time.get_ticks()
                    random_mine_placement(cell_data, number_of_columns * number_of_rows, number_of_columns, number_of_mines)
                    current_screen = "game"
        
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                current_screen = "initial_screen"
        

    
    elif current_screen == "lose":
        universal_sprites.draw(display)

        you_lost_text = wording_font.render("YOU LOST", True, (0,0,0))
        display.blit(you_lost_text,(750,200))
        
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                current_screen = "initial_screen"
    
    elif current_screen == "win":
        universal_sprites.draw(display)

        you_won_text = wording_font.render("YOU WON THE GAME!", True, (0,0,0))
        display.blit(you_won_text,(750,200))

        score = timer_text
        score_rendered_text = wording_font.render(f"SCORE: {score}", True, (0,0,0))
        display.blit(score_rendered_text,(800,400))


        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                current_screen = "initial_screen"


    elif current_screen == "game":
        for event in list_of_events:
            #clicking controls
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click_x, mouse_click_y = getting_mouse_position()
                row = (mouse_click_y - starting_position_y) // square_size
                column = (mouse_click_x - starting_position_x) // square_size
                if 0 <= row < number_of_rows and 0 <= column < number_of_columns:
                    #right click
                    if event.button == 3:
                        if not cell_data[row][column].is_revealed():
                            if not cell_data[row][column].is_flag():
                                cell_data[row][column].set_color(pygame.Color("blue"))
                                cell_data[row][column].set_flag(True)
                            else:
                                cell_data[row][column].set_flag(False)
                                cell_data[row][column].set_color(pygame.Color("white"))
                    #Left click DOCUMENT EXCEPTION HANDLING WITH FREE_CELLS
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
                                game_over = True
                                current_screen = "lose"
                            if free_cells == 0:
                                game_over = True 
                                current_scren = "win"
                                
        
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                current_screen = "initial_screen"
                game_over = True
        
        if game_over:
            elapsed_time = 0
            minutes = 0
            seconds = 0

        else:
            elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000
            minutes = elapsed_time // 60
            seconds = elapsed_time % 60


                            
        gamesprites.draw(display)

        timer_text = f"{minutes:02}:{seconds:02}"
        rendered_timer_text = wording_font.render(timer_text, False, (0, 0, 0))
        display.blit(rendered_timer_text, (110,10))
        
        free_cells_text = f"FREE CELLS: {free_cells}"
        free_cells_surface = wording_font.render(free_cells_text, False, (0,0,0))
        display.blit(free_cells_surface, (700, 10))

        moles_remaining_text = f"MOLES: {number_of_mines}"
        moles_remaining_text_surface = wording_font.render(moles_remaining_text, False, (0,0,0))
        display.blit(moles_remaining_text_surface, (1560, 10))

        quit_text = wording_font.render("PRESS (ESC) TO QUIT", False, (0,0,0))
        display.blit(quit_text,(650,1000))

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
