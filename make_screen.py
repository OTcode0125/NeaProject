import pygame

full_screen_width = 1920
full_screen_height = 1080
class Screen:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.Surface((self.width, self.height))  # Create an off-screen surface

    def fill(self, color):
        self.screen.fill(color)

class Button:
    def __init__(self, text , x, y, font, action = None):
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.action = action

    def control(self,main_menu_screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Hover check to put a * over it later
        is_hovered = self.x <= mouse[0] <= self.x + self.font.size(self.text)[0] and self.y <= mouse[1] <= self.y + self.font.size(self.text)[1]

        # Draw button text
        if is_hovered:
            display_text = f"* {self.text} *"
        else:
            display_text = self.text

        text_surf = self.font.render(display_text, True, "Black")
        screen.blit(text_surf, (self.x, self.y))

        # Handle click (exception)
        if is_hovered and click[0] == 1 and self.action is not None:
            self.action()

    
