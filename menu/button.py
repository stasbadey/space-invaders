import pygame

from render.util.RenderProperties import WINDOW


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (88, 54, 200)
        self.active_color = (164, 176, 200)

    def draw(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(WINDOW, self.active_color, (x, y, self.width, self.height))

            if click[0] == 1 and action is not None:
                action()

        else:
            pygame.draw.rect(WINDOW, self.inactive_color, (x, y, self.width, self.height))

        print_text(message=message, x=x + 10, y=y + 10, font_size=font_size)



def print_text(message, x, y, font_color=(0, 0, 0), font_size=10):
    font_type = pygame.font.SysFont('comicsans', font_size)
    text = font_type.render(message, True, font_color)
    WINDOW.blit(text, (x, y))