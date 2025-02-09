from helpers import screen, read_comment_from_user
import pygame
from constants import *
from Post import *


class Comment:
    __text: str

    def __init__(self):
        self.__text = read_comment_from_user()

    def Display(self):
        txt = f"{self.__text}"
        txt_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        screen.blit(txt_font.render(txt, True, BLACK(FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS)))