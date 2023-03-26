from math import *
import pygame

def scale_img(img : pygame.image, factor : int):
    size = img.get_width() * factor, img.get_height() * factor
    return pygame.transform.scale(img, size)


def blit_rotate_image(win : pygame.Surface, image : pygame.image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = top_left).center)
    win.blit(rotated_image, new_rect.topleft)

def angle(pos1, pos2):
    x = pos1[0] - pos2[0]
    y = pos1[1] - pos2[1]
    angle = 0
    
    if x != 0 and y != 0:
        a = y/x
        b = tan(a)
        angle = degrees(atan(b))
        
    return angle

def distance_to(pos1, pos2):
    return (round(sqrt(abs((pos1[0] - pos2[0])**2 + abs((pos1[1] - pos2[1])**2)))))

def get_tile(x, y, sizeOneTile, spritesheet : pygame.image):
    
    rect = pygame.Rect(x * sizeOneTile[0], y * sizeOneTile[1], sizeOneTile[0], sizeOneTile[1])
    subsurface = pygame.Surface.subsurface(spritesheet, rect)
    return subsurface

class Signal:
    def __init__(self):
        self.callbacks = []

    def connect(self, callback, *binds):
        print(callback, binds)
        self.callbacks.append([callback, binds])

    def emit(self, **kwargs):
        for callback in self.callbacks:
            callback[0](*callback[1], **kwargs)
