from constants import *
from Post import *


class TextPost(Post):

    def __init__(self, Text, TextColor, BackgroundColor, name, loc, desc):
        super().__init__(name, loc, desc)
        self.Text = Text
        self.TextColor = TextColor
        self.BackgroundColor = BackgroundColor

    def Display(self):
        super().Display()
        desc = f"{self.__description}"
        square = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.BackgroundColor, square)
        font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        text = font.render(desc, True, BLACK)








