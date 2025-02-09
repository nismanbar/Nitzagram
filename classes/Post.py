import pygame

from classes import Comment
from constants import *
from helpers import screen


class Post:

    __username: str
    __location: str
    __description: str
    __likes: int
    __NumComments: int
    __comments: list[Comment]

    def __init__(self, name, loc, desc):
        self.__username = name
        self.__location = loc
        self.__description = desc
        self.__likes = 0
        self.__NumComments = 0

    def AddLikes(self):
        self.__likes += 1

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """

        pass
    def display_likes(self):
        likes = f"Liked by {self.__likes} users"
        likes_font = pygame.font.SysFont('chalkduster.ttf', )


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.__comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments", True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.__comments)):
            if position_index >= len(self.__comments):
                position_index = 0
            self.__comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



