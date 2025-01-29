import pygame
import pygame_textinput

from game import Game
from sprites import MainMenuSprite,UniversalSprite,GameScreenSprite


pygame.init()
#window class used for holding aesthetic variables and sprites
class Window():
    def __init__(self):
        self.border_width = 1
        self.space_between_squares = 0
        self.starting_position_x = 600
        self.starting_position_y = 190

        self.logintext = pygame_textinput.TextInputVisualizer()
        self.passwordtext = pygame_textinput.TextInputVisualizer()
        self.current_input_choice = "login"
        self.current_screen = "initial_screen"
        self.running = True
        self.logged_in = False
        self.wording_font = pygame.font.Font("bubble_font.ttf", 50)
        self.number_font = pygame.font.SysFont("Roman",30)
        self.small_wording_font = pygame.font.Font("bubble_font.ttf",25)
        #mainmenusprites
        self.initialscreen = MainMenuSprite("main_menu_screen.png", 0,0, 1920,1080)
        self.esc = MainMenuSprite("esc.png",10,10, 100,100)
        self.initialscreen_sprites = pygame.sprite.Group()
        self.initialscreen_sprites.add(self.initialscreen, self.esc)

        #universally used spites
        self.generalscreen = UniversalSprite("general_screen.png",0,0,1920,1080)
        self.universal_sprites = pygame.sprite.Group()
        self.universal_sprites.add(self.generalscreen,self.esc)
        #game screen sprites 
        self.timer = GameScreenSprite("timer.png",50,10,50,50)
        self.mole = GameScreenSprite("mole.png",1500,10,50,50)
        self.gamesprites = pygame.sprite.Group()
        self.gamesprites.add(self.generalscreen,self.timer,self.mole)

        self.current_input_choice = "login"
        self.game = None
        self.recommendation_shown = False
        self.selected_recommendation = None
#re-inits new game when difficulty selected by user
    def new_game(self, difficulty):
        self.game = Game(difficulty)
        self.current_screen = "game"
