import pygame
from pygame.transform import scale


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.images = []
        self.index = 0

        for i in range(3):
            image = scale(pygame.image.load(f"imgs/damage/damage0{i}.png"), (40, 40))
            self.images.append(image)

    def draw_explosion(self, screen):
        screen.blit(self.images[self.index], (self.rect.x, self.rect.y))
        pygame.display.flip()