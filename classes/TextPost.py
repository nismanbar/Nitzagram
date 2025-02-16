from constants import *
from classes.Post import Post
from helpers import screen
import pygame


class TextPost(Post):

    __txt: str
    __txtColor: tuple
    __bgColor: tuple

    def __init__(self, txt, txtColor, bgColor, name, loc, desc):
        super().__init__(name, loc, desc)
        self.__txt = txt
        self.__txtColor = txtColor
        self.__bgColor = bgColor

    def Display(self):
        super().Display()
        surface = pygame.Surface((int(POST_WIDTH), int(POST_HEIGHT)))
        surface.fill(self.__bgColor)
        txt = self.__txt
        txt_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        render = txt_font.render(txt, True, self.__txtColor)
        x = POST_WIDTH/2 + POST_X_POS
        y = POST_HEIGHT/2 + POST_Y_POS
        screen.blit(render, (x, y))
