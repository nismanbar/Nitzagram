import pygame
from helpers import screen, read_comment_from_user
from constants import FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS, COMMENT_LINE_HEIGHT, COMMENT_TEXT_SIZE, BLACK


class Comment:
    def __init__(self):
        self.__text = read_comment_from_user()

    def Display(self, index):
        y_position = FIRST_COMMENT_Y_POS + index * COMMENT_LINE_HEIGHT
        txt_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        render = txt_font.render(self.__text, True, BLACK)
        screen.blit(render, (FIRST_COMMENT_X_POS, y_position))
