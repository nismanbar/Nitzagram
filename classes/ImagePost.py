from classes import Post
from constants import *
import pygame

class ImagePost(Post):

    def __init__(self, Img, name, loc, desc):
        super().__init__(name, loc, desc)
        self.Img = Img

    def Display(self):
        super().Display()
        pic = pygame.transform.scale(pygame.image.load(f"Images/noa_kirel.png"), (POST_WIDTH, POST_HEIGHT))
        screen.blit(pic, (POST_X_POS, POST_Y_POS))
