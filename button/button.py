import pygame
pygame.init()

class Button(pygame.Rect):
    def __init__(self, parent, x, y, width, height, **kwargs):
        super().__init__(x, y, width, height)
        self._parent = parent

        self.background = kwargs.get("background") if kwargs.get("background") is not None else (0,0,0)
        for key in ["click_bg", "hover_bg"]:
            if isinstance(self.background, (tuple, list, set)):
                bg = kwargs.get(key) if kwargs.get(key) is not None else self.background
            else:
                bg = self.background
            setattr(self, key, bg)
        self.current_bg = self.background

        for key in ["border_radius"]:
            num = kwargs.get(key) if kwargs.get(key) is not None else 0
            setattr(self, key, num)
        
        self.callback = kwargs.get("callback") if kwargs.get("callback") is not None else self.__do_nothing

    @staticmethod
    def __do_nothing():
        pass

    def draw(self):
        if isinstance(self.background, (tuple, list, set)):
            pygame.draw.rect(self._parent, self.current_bg, self, width=0, border_radius=self.border_radius)
        else:
            image = pygame.transform.scale(self.background, [self.width, self.height])
            self._parent.blit(image, [self.x, self.y])
            
    
    def listen(self, event):
        pos = pygame.mouse.get_pos()
        self.current_bg = self.background
        if self.collidepoint(pos):
            self.current_bg = self.hover_bg
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.current_bg = self.click_bg
                self.callback()
    
    def set_callback(self, callback):
        self.callback = callback