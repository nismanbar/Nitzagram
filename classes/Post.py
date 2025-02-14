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
    __comments_display_index: int

    def __init__(self, name, loc, desc):
        self.__username = name
        self.__location = loc
        self.__description = desc
        self.__likes = 0
        self.__NumComments = 0
        self.__comments_display_index = 0
        self.__comments = []

    def AddLikes(self):
        self.__likes += 1

    def AddComment(self):
        new_comment = Comment.Comment()
        self.__comments.append(new_comment)
        self.__NumComments += 1

    def Display(self):
        self.DisplayLocation()
        self.DisplayDescription()
        self.DisplayLikes()
        self.DisplayComments()
        self.DisplayUserName()

    def DisplayLikes(self):
        likes = f"Liked by {self.__likes} users"
        likes_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        render = likes_font.render(likes, True, BLACK)
        screen.blit(render, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))

    def DisplayLocation(self):
        loc = f"{self.__location}"
        loc_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        render = loc_font.render(loc, True, BLACK)
        screen.blit(render, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

    def DisplayDescription(self):
        desc = f"{self.__description}"
        desc_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        render = desc_font.render(desc, True, BLACK)
        screen.blit(render, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))

    def DisplayUserName(self):
        name = f"{self.__username}"
        name_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        render = name_font.render(name, True, BLACK)
        screen.blit(render, (USER_NAME_X_POS, USER_NAME_Y_POS))

    def DisplayComments(self):
        position_index = self.__comments_display_index
        if len(self.__comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments", True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.__comments)):
            if position_index >= len(self.__comments):
                position_index = 0
            self.__comments[position_index].Display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break
    def MoreComments(self):
        pass

