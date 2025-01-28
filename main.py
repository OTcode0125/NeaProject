import pygame

from window import Window


pygame.init()
pygame.font.init()

display = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Farmsweeper")
clock = pygame.time.Clock()

def draw_square_with_border(border_color, square_color, x, y, square_size, border_width):
    fill_size = square_size - border_width * 2
    pygame.draw.rect(display, border_color, (x, y, square_size, square_size), width=border_width)
    pygame.draw.rect(display, square_color, (x + border_width, y + border_width, fill_size, fill_size))

def getting_mouse_position():
    return pygame.mouse.get_pos()

def read_tutorial_txt_files(file_path):
    with open(file_path,"r") as file:
        return file.readlines()


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

    #screen logic
    if window.current_screen == "initial_screen":
        window.initialscreen_sprites.draw(display)

        instruction_text = window.wording_font.render("PRESS (ENTER) TO START", True, (0, 0, 0))
        display.blit(instruction_text, (600, 1000))

        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                window.running = False
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                window.current_screen = "main_menu"
#main menu screen
    elif window.current_screen == "main_menu":

        window.universal_sprites.draw(display)

        main_menu_text = window.wording_font.render("MAIN MENU SCREEN", True, (0,0,0))
        display.blit(main_menu_text,(650,10))

        login_text = window.wording_font.render("PRESS 1 (LOGIN)", True, (255,255,255))
        display.blit(login_text,(150,300))
        
        tutorial_text = window.wording_font.render("PRESS 2 (TUTORIAL)", True, (255,255,255))
        display.blit(tutorial_text,(150,450))

        play_as_guest = window.wording_font.render("PRESS (ENTER) TO PLAY AS GUEST", True, (0,0,0))
        display.blit(play_as_guest, (500,1000))
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
        
        title_surface = window.wording_font.render("LOGIN SCREEN", True, (0, 0, 0))
        display.blit(title_surface, (700, 10))

        username_text_surface = window.wording_font.render("Enter Username:", True, (0,0,0))
        display.blit(username_text_surface,(300,400))

        password_text_surface = window.wording_font.render("Enter Password", True, (0,0,0))
        display.blit(password_text_surface,(300,500))

        create_account_text = window.wording_font.render("PRESS (CTRL) TO CREATE A NEW ACCOUNT", True, (0, 0, 0))
        display.blit(create_account_text, (300, 1000))


        display.blit(window.logintext.surface, (850,420))
        display.blit(window.passwordtext.surface, (850,520))
        
        if key_press[pygame.K_ESCAPE]:
            window.running = False

        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                entered_username = window.logintext.value.strip()
                entered_password = window.passwordtext.value.strip()

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
                        window.current_screen = "logged_in_screen"
                    else:
                        window.current_screen = "failed_login"

                except FileNotFoundError:
                    print("Error: User data file not found.")


    elif window.current_screen == "logged_in_screen":
        window.universal_sprites.draw(display)

        window.logged_in = True

        logged_in_text = window.wording_font.render(f"HEY {username} YOU ARE LOGGED IN", True,(0,0,0))
        display.blit(logged_in_text,(400,10))

        proceed_text = window.wording_font.render("PRESS (ENTER) TO PROCEED TO DIFFICULTY SCREEN", True,(0,0,0))
        display.blit(proceed_text,(200,1000))

        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                window.current_screen = "choose_difficulty"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                window.current_screen = "initial_screen"
    
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
        
        title_surface = window.wording_font.render("CREATE NEW ACCOUNT", True, (0, 0, 0))
        display.blit(title_surface, (700, 10))

        title_surface = window.wording_font.render("PRESS (TAB) TO SWAP BETWEEN USERNAME AND PASSWORD", True, (0, 0, 0))
        display.blit(title_surface, (100, 1000))

        username_text_surface = window.wording_font.render("Enter New Username:", True, (0, 0, 0))
        display.blit(username_text_surface, (230, 400))

        password_text_surface = window.wording_font.render("Enter New Password:", True, (0, 0, 0))
        display.blit(password_text_surface, (230, 500))

        display.blit(window.logintext.surface, (950, 420))
        display.blit(window.passwordtext.surface, (950, 520))

        if key_press[pygame.K_ESCAPE]:
            window.running = False

        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                new_username = window.logintext.value.strip()
                new_password = window.passwordtext.value.strip()
#making sure the input not empty 
                if new_username and new_password:
                    try:
                        with open("users.txt", "a") as file:
                            file.write(f"\n{new_username}:{new_password}")
                        window.current_screen = "log_in"
                    except Exception as e:
                        print(f"Error saving new account: {e}")
                else:
                    print("Error: Username and password cannot be empty.")


        
    
    elif window.current_screen == "tutorial":
        window.universal_sprites.draw(display)

        tut_welcome_text = window.wording_font.render("WELCOME TO THE TUTORIAL", True, (0,0,0))
        display.blit(tut_welcome_text,(500,10))

        tutorial_text_1 = read_tutorial_txt_files("tut.txt")

        tutorial_txt_x_pos = 100
        tutorial_txt_y_pos = 200
        space_between_lines = 5

        for line in tutorial_text_1:
            rendered_line = window.wording_font.render(line.strip(), True, (0,0,0))
            display.blit(rendered_line, (tutorial_txt_x_pos, tutorial_txt_y_pos))
            tutorial_txt_y_pos += space_between_lines


        if key_press[pygame.K_ESCAPE]:
            window.current_screen = "initial_screen"



    elif window.current_screen == "choose_difficulty":
        window.universal_sprites.draw(display)
        
        easy_selection_text = window.wording_font.render("PRESS (1) FOR EASY", True, (255, 255, 255))
        display.blit(easy_selection_text, (150, 300))

        hard_selection_text = window.wording_font.render("PRESS (2) FOR HARD", True, (255, 255, 255))
        display.blit(hard_selection_text, (150, 400))

        for event in list_of_events:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    #having to reinitialse cell data so that the variables can change
                    #easy difficulty
                    window.new_game("easy")

                elif event.key == pygame.K_2:
                    #hard difficulty
                    window.new_game("hard")

        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                window.current_screen = "initial_screen"
        

    
    elif window.current_screen == "lose" and window.logged_in == False:
        window.universal_sprites.draw(display)

        you_lost_text = window.wording_font.render("YOU LOST", True, (0,0,0))
        display.blit(you_lost_text,(750,200))
        
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                window.current_screen = "initial_screen"

    elif window.current_screen == "lose" and window.logged_in == True:
        window.universal_sprites.draw(display)

        you_lost_text = window.wording_font.render("YOU LOST, BUT BECAUSE YOU LOGGED IN... YOU GET RECOMMENDATIONS", True, (0,0,0))
        display.blit(you_lost_text,(50,200))
        
        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                window.current_screen = "initial_screen"

    
    elif window.current_screen == "win":
        window.universal_sprites.draw(display)

        you_won_text = window.wording_font.render("YOU WON THE GAME!", True, (0,0,0))
        display.blit(you_won_text,(750,200))

        score = timer_text
        score_rendered_text = window.wording_font.render(f"SCORE: {score}", True, (0,0,0))
        display.blit(score_rendered_text,(800,400))


        for event in list_of_events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                current_screen = "initial_screen"


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
                        if not window.game.cell_data[row][column].is_revealed() and not window.game.cell_data[row][column].is_flag():
                            window.game.cell_data[row][column].reveal()
                            window.game.free_cells -= 1 
                            if not window.game.cell_data[row][column].is_mine():
                                surrounding_mines = 0
                                #bottom right
                                if row < window.game.number_of_rows-1 and column < window.game.number_of_columns-1 and window.game.cell_data[row+1][column+1].is_mine():
                                    surrounding_mines += 1
                                #bottom left
                                if row < window.game.number_of_rows-1 and column > 0 and window.game.cell_data[row+1][column-1].is_mine():
                                    surrounding_mines += 1
                                #right
                                if column < window.game.number_of_columns-1 and window.game.cell_data[row][column+1].is_mine():
                                    surrounding_mines += 1
                                #left
                                if column >0 and window.game.cell_data[row][column-1].is_mine():
                                    surrounding_mines += 1
                                #below
                                if row < window.game.number_of_rows-1 and window.game.cell_data[row+1][column].is_mine():
                                    surrounding_mines += 1
                                #top
                                if row > 0 and window.game.cell_data[row-1][column].is_mine():
                                    surrounding_mines += 1
                                #top left
                                if row >0 and column > 0 and window.game.cell_data[row-1][column-1].is_mine():
                                    surrounding_mines += 1
                                #top right
                                if row > 0 and column < window.game.number_of_columns-1 and window.game.cell_data[row-1][column+1].is_mine():
                                    surrounding_mines += 1
                                window.game.cell_data[row][column].set_surrounding_mines(surrounding_mines)
                            
                            else:
                                window.current_screen = "lose"
                            if window.game.free_cells == 0:
                                window.current_scren = "win"
                                
        
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

        moles_remaining_text = f"MOLES: {window.game.number_of_mines}"
        moles_remaining_text_surface = window.wording_font.render(moles_remaining_text, False, (0,0,0))
        display.blit(moles_remaining_text_surface, (1560, 10))

        quit_text = window.wording_font.render("PRESS (ESC) TO QUIT", False, (0,0,0))
        display.blit(quit_text,(650,1000))

        for row in range(window.game.number_of_rows):
            for column in range(window.game.number_of_columns):
                cell_x = window.starting_position_x + (window.game.square_size + window.space_between_squares) * column
                cell_y = window.starting_position_y + (window.game.square_size + window.space_between_squares) * row
                cell_color = window.game.cell_data[row][column].get_color()
                draw_square_with_border(pygame.Color("black"),cell_color,cell_x,cell_y,window.game.square_size,window.border_width)
                if window.game.cell_data[row][column].is_revealed():
                    surrounding_mines = window.game.cell_data[row][column].get_surrounding_mines()
                    if surrounding_mines > 0:
                        number_of_surrounding_mines_surface = window.number_font.render(str(surrounding_mines), False, (0, 0, 0))
                        display.blit(number_of_surrounding_mines_surface, (cell_x,cell_y))
                    


    pygame.display.flip()
    clock.tick(30)

pygame.quit()
