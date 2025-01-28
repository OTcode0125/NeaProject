import pygame


pygame.init()

class Sprites(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

class MainMenuSprite(Sprites):
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

class UniversalSprite(Sprites):
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

class GameScreenSprite(Sprites):
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
