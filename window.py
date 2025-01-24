import pygame
import pygame_textinput

from game import Game
from sprites import Sprites


pygame.init()

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
        self.wording_font = pygame.font.Font("bubble_font.ttf", 50)
        self.number_font = pygame.font.SysFont("Roman",30)
        #mainmenusprites
        self.initialscreen = Sprites("main_menu_screen.png", 0,0, 1920,1080)
        self.esc = Sprites("esc.png",10,10, 100,100)
        self.initialscreen_sprites = pygame.sprite.Group()
        self.initialscreen_sprites.add(self.initialscreen, self.esc)

        #universally used spites
        self.generalscreen = Sprites("general_screen.png",0,0,1920,1080)
        self.universal_sprites = pygame.sprite.Group()
        self.universal_sprites.add(self.generalscreen,self.esc)
        #game screen sprites
        self.timer = Sprites("timer.png",50,10,50,50)
        self.mole = Sprites("mole.png",1500,10,50,50)
        self.gamesprites = pygame.sprite.Group()
        self.gamesprites.add(self.generalscreen,self.timer,self.mole)

        self.current_input_choice = "login"
        self.game = None

    def new_game(self, difficulty):
        self.game = Game(difficulty)
        self.current_screen = "game"
