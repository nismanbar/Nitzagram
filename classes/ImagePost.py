from classes.Post import Post
from constants import *
from helpers import screen
import pygame


class ImagePost(Post):
    def __init__(self, Img, name, loc, desc):
        super().__init__(name, loc, desc)
        self.Img = Img

    def Display(self):
        super().Display()
        img = f"{self.Img}"
        pic = pygame.transform.scale(pygame.image.load(img), (POST_WIDTH, POST_HEIGHT))
        screen.blit(pic, (POST_X_POS, POST_Y_POS))
