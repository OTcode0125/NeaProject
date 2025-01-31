import pygame
import random
from window import Window


pygame.init()
pygame.font.init()

display = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Farmsweeper")
clock = pygame.time.Clock()
#func to draw each cell with a border around it
def draw_square_with_border(border_color, square_color, x, y, square_size, border_width):
    fill_size = square_size - border_width * 2
    pygame.draw.rect(display, border_color, (x, y, square_size, square_size), width=border_width)
    pygame.draw.rect(display, square_color, (x + border_width, y + border_width, fill_size, fill_size))

def getting_mouse_position():
    return pygame.mouse.get_pos()
#read from txt file of users choice
def read_tutorial_txt_files(file_path):
    with open(file_path,"r") as file:
        return file.readlines()

def read_help_txt_files(file_path):
    with open(file_path,"r") as file:
        return file.readlines()
#used to output text in the exact center screen
def center_text(display,text,font,color,screen_width,y):
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect(center=(screen_width // 2,y))
    display.blit(text_surface,text_rect)
#XOR hashing algorithm
def hashing(input_string):
    hash_value = 0
    for char in input_string:
        hash_value ^=ord(char)
        hash_value = (hash_value << 5) | (hash_value >> (32 - 5))
    return str(hash_value)


window = Window()

#loop
while window.running:
    list_of_events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window.running = False
        else:
            list_of_events.append(event)
    key_press = pygame.key.get_pressed()

#all screen switching logic
    if window.current_screen == "initial_screen":
        window.initialscreen_sprites.draw(display)
        esc_text = window.small_wording_font.render("PRESSING (ESC) AT ANY TIME WILL RETURN YOU TO THIS SCREEN", True, (0,0,0))
        display.blit(esc_text,(120,50))
        
        center_text(display,"PRESS (ENTER) TO START",window.wording_font,(0,0,0),1920,1000)

        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                window.running = False
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                window.current_screen = "main_menu"
#main menu screen
    elif window.current_screen == "main_menu":

        window.universal_sprites.draw(display)

        center_text(display,"MAIN MENU SCREEN",window.wording_font,(0,0,0),1920,50)
        center_text(display,"PRESS (1) TO LOGIN",window.wording_font,(0,0,0),1920,300)
        center_text(display,"PRESS (2) TUTORIAL",window.wording_font,(0,0,0),1920,450)
        center_text(display,"PRESS (ENTER) TO PLAY AS GUEST",window.wording_font,(0,0,0),1920,1000)

        if key_press[pygame.K_1]:
            window.current_screen = "log_in"
        if key_press[pygame.K_ESCAPE]:
            window.running = False
        if key_press[pygame.K_2]:
            window.current_screen = "tutorial"
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                window.current_screen = "choose_difficulty"
        
#login screen
    elif window.current_screen == "log_in":
        list_of_text_events = []
        for event in list_of_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    window.current_screen = "create_login"
                elif event.key != pygame.K_TAB:
                    list_of_text_events.append(event)
                else:
                    #pressing tab changes from login to password visa versa
                    if window.current_input_choice == "login":
                        window.current_input_choice = "password"
                    elif window.current_input_choice == "password":
                        window.current_input_choice = "login"
        
        if window.current_input_choice == "login":
            window.logintext.update(list_of_text_events)
        
        elif window.current_input_choice == "password":
            window.passwordtext.update(list_of_text_events)
        
        window.universal_sprites.draw(display)
        
        center_text(display,"LOGIN SCREEN",window.wording_font,(0,0,0),1920,50)
        center_text(display,"PRESS(CTRL) TO CREATE A NEW ACCOUNT",window.wording_font,(0,0,0),1920,1000)

        username_text_surface = window.wording_font.render("Enter Username:", True, (0,0,0))
        display.blit(username_text_surface,(300,400))

        password_text_surface = window.wording_font.render("Enter Password:", True, (0,0,0))
        display.blit(password_text_surface,(300,500))


        display.blit(window.logintext.surface, (850,420))
        display.blit(window.passwordtext.surface, (850,520))
        
        if key_press[pygame.K_ESCAPE]:
            window.running = False
        #if user presses enter then information checked
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                entered_username = window.logintext.value.strip()
                entered_password = window.passwordtext.value.strip()
                entered_password_hashed = hashing(entered_password)
                #open txt file
                try:
                    with open("users.txt", "r") as file:
                        valid_credentials = False
                        for line in file:
                            username, stored_hashed_password = line.strip().split(":")
                            if entered_username == username and entered_password_hashed == stored_hashed_password:
                                valid_credentials = True
                                break

                    if valid_credentials:
                        window.current_screen = "logged_in_screen"
                    else:
                        window.current_screen = "failed_login"

                except FileNotFoundError:
                    print("Error: User data file not found.")

#logged in screen
    elif window.current_screen == "logged_in_screen":
        window.universal_sprites.draw(display)

        window.logged_in = True

        center_text(display,f"HEY {username} YOU ARE LOGGED IN",window.wording_font,(0,0,0),1920,50)
        center_text(display,"PRESS (ENTER) TO PROCEED TO DIFFICULTY SCREEN",window.wording_font,(0,0,0),1920,1000)

        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                window.current_screen = "choose_difficulty"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                window.current_screen = "initial_screen"
#create login screen
    elif window.current_screen == "create_login":
        list_of_text_events = []
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key != pygame.K_TAB:
                list_of_text_events.append(event)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                window.current_input_choice = "password" if window.current_input_choice == "login" else "login"

        if window.current_input_choice == "login":
            window.logintext.update(list_of_text_events)
        elif window.current_input_choice == "password":
            window.passwordtext.update(list_of_text_events)

        window.universal_sprites.draw(display)
        
        center_text(display,"CREATE NEW ACCOUNT",window.wording_font,(0,0,0),1920,50)
        center_text(display,"PRESS (TAB) TO SWAP BETWEEN USERNAME AND PASSWORD",window.wording_font,(0,0,0),1920,1000)

        username_text_surface = window.wording_font.render("Enter New Username:", True, (0,0,0))
        display.blit(username_text_surface, (230, 400))

        password_text_surface = window.wording_font.render("Enter New Password:", True, (0,0,0))
        display.blit(password_text_surface, (230, 500))

        display.blit(window.logintext.surface, (950, 420))
        display.blit(window.passwordtext.surface, (950, 520))

        if key_press[pygame.K_ESCAPE]:
            window.running = False

        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                new_username = window.logintext.value.strip()
                new_password = window.passwordtext.value.strip()
                hashed_password = hashing(new_password)
#making sure the input not empty 
                if new_username and new_password:
                    try:
                        with open("users.txt", "a") as file:
                            file.write(f"\n{new_username}:{hashed_password}")
                        window.current_screen = "log_in"
                    except Exception as e:
                        print(f"Error saving new account: {e}")
                else:
                    print("Error: Username and password cannot be empty.")
#failed login screen   
    elif window.current_screen == "failed_login":
        window.universal_sprites.draw(display)

        center_text(display,"FAILED TO LOGIN",window.wording_font,(0,0,0),1920,50)
        center_text(display,"PRESS (ESC) TO RETURN TO INITIAL SCREEN",window.wording_font,(0,0,0),1920,1000)

        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                window.current_screen = "initial_screen"



        
#tutorial screen
    elif window.current_screen == "tutorial":
        window.universal_sprites.draw(display)

        center_text(display,"WELCOME TO THE TUTORIAL",window.wording_font,(0,0,0),1920,50)

        tutorial_text_1 = read_tutorial_txt_files("tut.txt")

        tutorial_txt_x_pos = 200
        tutorial_txt_y_pos = 200
        space_between_lines = 50
        #reading from tut.txt
        for line in tutorial_text_1:
            rendered_line = window.small_wording_font.render(line.strip(), True, (0,0,0))
            display.blit(rendered_line, (tutorial_txt_x_pos, tutorial_txt_y_pos))
            tutorial_txt_y_pos += space_between_lines


        if key_press[pygame.K_ESCAPE]:
            window.current_screen = "initial_screen"


#choose difficulty screen
    elif window.current_screen == "choose_difficulty":
        window.universal_sprites.draw(display)
        center_text(display,"CHOOSE DIFFICULTY SCREEN",window.wording_font,(0,0,0),1920,50)
        center_text(display,"PRESS (1) FOR EASY",window.wording_font,(0,0,0),1920,300)
        center_text(display,"PRESS (2) FOR HARD",window.wording_font,(0,0,0),1920,400)

        for event in list_of_events:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    #having to reinitialse cell data so that the variables can change
                    #easy
                    window.new_game("easy")

                elif event.key == pygame.K_2:
                    #hard
                    window.new_game("hard")

        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                window.current_screen = "initial_screen"
        

#lose not logged in screen
    elif window.current_screen == "lose" and window.logged_in == False:
        window.universal_sprites.draw(display)

        center_text(display,"YOU LOST",window.wording_font,(0,0,0),1920,200)
        center_text(display,"PRESS (ENTER) TO REPLAY",window.wording_font,(0,0,0),1920,1000)
        
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                window.current_screen = "initial_screen"
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                window.current_screen = "choose_difficulty"
        
#lose and logged in screen
    elif window.current_screen == "lose" and window.logged_in == True:
        window.universal_sprites.draw(display)

        center_text(display,"YOU LOST, WHILE LOGGED IN... YOU GET RECOMMENDATIONS",window.wording_font,(0,0,0),1920,200)
        center_text(display,f"FREE CELLS LEFT:{window.game.free_cells}",window.small_wording_font,(0,0,0),1920,600)
        center_text(display,"PRESS (ENTER) TO REPLAY",window.wording_font,(0,0,0),1920,1000)

        if not window.recommendation_shown:
            help_lines = read_help_txt_files("help.txt")
            if help_lines:
                window.selected_recommendation = random.choice(help_lines).strip()
            else:
                window.selected_recommendation = "None Available"
            window.recommendation_shown = True

        center_text(display,f"{window.selected_recommendation}",window.small_wording_font,(0,0,0),1920,400)
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                window.current_screen = "initial_screen"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                window.current_screen = "choose_difficulty"

#win screen
    elif window.current_screen == "win":
        window.universal_sprites.draw(display)

        center_text(display,"YOU WON THE GAME",window.wording_font,(0,0,0),1920,200)

        score = timer_text
        
        center_text(display,f"SCORE: {score}",window.small_wording_font,(0,0,0),1920,400)
        center_text(display,"PRESS (ENTER) TO REPLAY",window.wording_font,(0,0,0),1920,1000)



        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                current_screen = "initial_screen"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                window.current_screen = "choose_difficulty"
            

#game screen
    elif window.current_screen == "game":
        for event in list_of_events:
            #clicking controls
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click_x, mouse_click_y = getting_mouse_position()
                row = (mouse_click_y - window.starting_position_y) // window.game.square_size
                column = (mouse_click_x - window.starting_position_x) // window.game.square_size
                if 0 <= row < window.game.number_of_rows and 0 <= column < window.game.number_of_columns:
                    #right click
                    if event.button == 3:
                        if not window.game.cell_data[row][column].is_revealed():
                            if not window.game.cell_data[row][column].is_flag():
                                window.game.cell_data[row][column].set_color(pygame.Color("blue"))
                                window.game.cell_data[row][column].set_flag(True)
                            else:
                                window.game.cell_data[row][column].set_flag(False)
                                window.game.cell_data[row][column].set_color(pygame.Color("white"))
                    #Left click DOCUMENT EXCEPTION HANDLING WITH FREE_CELLS
                    elif event.button == 1:
                        if window.game.first_click:
                            window.game.first_click = False
                            window.game.place_moles((row, column))

                        if not window.game.cell_data[row][column].is_revealed() and not window.game.cell_data[row][column].is_flag():
                            window.game.cell_data[row][column].reveal()
                            window.game.free_cells -= 1 
                            if not window.game.cell_data[row][column].is_mole():
                                surrounding_moles = 0
                                #bottom right
                                if row < window.game.number_of_rows-1 and column < window.game.number_of_columns-1 and window.game.cell_data[row+1][column+1].is_mole():
                                    surrounding_moles += 1
                                #bottom left
                                if row < window.game.number_of_rows-1 and column > 0 and window.game.cell_data[row+1][column-1].is_mole():
                                    surrounding_moles += 1
                                #right
                                if column < window.game.number_of_columns-1 and window.game.cell_data[row][column+1].is_mole():
                                    surrounding_moles += 1
                                #left
                                if column >0 and window.game.cell_data[row][column-1].is_mole():
                                    surrounding_moles += 1
                                #below
                                if row < window.game.number_of_rows-1 and window.game.cell_data[row+1][column].is_mole():
                                    surrounding_moles += 1
                                #top
                                if row > 0 and window.game.cell_data[row-1][column].is_mole():
                                    surrounding_moles += 1
                                #top left
                                if row >0 and column > 0 and window.game.cell_data[row-1][column-1].is_mole():
                                    surrounding_moles += 1
                                #top right
                                if row > 0 and column < window.game.number_of_columns-1 and window.game.cell_data[row-1][column+1].is_mole():
                                    surrounding_moles += 1
                                window.game.cell_data[row][column].set_surrounding_moles(surrounding_moles)
                            
                            else:
                                window.current_screen = "lose"
                            if window.game.free_cells == 0:
                                window.current_screen = "win"
                                
        
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                window.current_screen = "initial_screen"
        
        
        elapsed_time = (pygame.time.get_ticks() - window.game.start_ticks) // 1000
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60

        window.gamesprites.draw(display)

        timer_text = f"{minutes:02}:{seconds:02}"
        rendered_timer_text = window.wording_font.render(timer_text, False, (0, 0, 0))
        display.blit(rendered_timer_text, (110,10))
        
        free_cells_text = f"FREE CELLS: {window.game.free_cells}"
        free_cells_surface = window.wording_font.render(free_cells_text, False, (0,0,0))
        display.blit(free_cells_surface, (700, 10))

        moles_remaining_text = f"MOLES: {window.game.number_of_moles}"
        moles_remaining_text_surface = window.wording_font.render(moles_remaining_text, False, (0,0,0))
        display.blit(moles_remaining_text_surface, (1560, 10))

        quit_text = window.wording_font.render("PRESS (ESC) TO QUIT", False, (0,0,0))
        display.blit(quit_text,(650,1000))
#draws squares with borders, displays surrounding cells and chooses where grid starts
        for row in range(window.game.number_of_rows):
            for column in range(window.game.number_of_columns):
                cell_x = window.starting_position_x + (window.game.square_size + window.space_between_squares) * column
                cell_y = window.starting_position_y + (window.game.square_size + window.space_between_squares) * row
                cell_color = window.game.cell_data[row][column].get_color()
                draw_square_with_border(pygame.Color("black"),cell_color,cell_x,cell_y,window.game.square_size,window.border_width)
                if window.game.cell_data[row][column].is_revealed():
                    surrounding_moles = window.game.cell_data[row][column].get_surrounding_moles()
                    if surrounding_moles > 0:
                        number_of_surrounding_moles_surface = window.number_font.render(str(surrounding_moles), False, (0, 0, 0))
                        display.blit(number_of_surrounding_moles_surface, (cell_x,cell_y))
                    


    pygame.display.flip()
    clock.tick(30)

pygame.quit()
