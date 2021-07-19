import pygame
pygame.init()

class Label:
    def __init__(self, parent, x, y, text, font="arial", font_size=12, **kwargs):
        self.x = x
        self.y = y
        self._parent = parent
        self.text = text
        self.font = font
        self.font_size = font_size
        self.color = kwargs.get("color") if kwargs.get("color") is not None else (0,0,0)
        self.background = kwargs.get("background")
    
    def draw(self):
        # displaying background
        if self.background is not None:
            if isinstance(self.background, (tuple, list, set)):
                pygame.draw.rect(self._parent, self.background, [(self.x, self.y), self.get_size()])
            else:
                image = pygame.transform.scale(self.background, self.get_size())
                self._parent.blit(image, [self.x, self.y])
        
        # displaying text
        font = pygame.font.SysFont(self.font, self.font_size)
        txt = font.render(self.text, True, self.color)
        self._parent.blit(txt, (self.x, self.y))
    
    def get_size(self):
        font = pygame.font.SysFont(self.font, self.font_size)
        return font.size(self.text)