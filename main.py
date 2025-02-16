import pygame
from helpers import screen
import buttons
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, LIGHT_GRAY, GREY
from classes import ImagePost, TextPost


def main():
    pygame.init()
    pygame.display.set_caption('Nitzagram')
    clock = pygame.time.Clock()

    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

    post1 = TextPost.TextPost("Test", LIGHT_GRAY, GREY, "bar", "ashkelon", "test")
    post2 = ImagePost.ImagePost('Images/noa_kirel.jpg', "liron", "ashkelon", "test")
    post3 = ImagePost.ImagePost('Images/ronaldo.jpg', "liron", "ashkelon", "test")

    p = [post1, post2, post3]
    cnt = 0
    post = p[cnt]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if buttons.click_post_button.is_hovered(mouse_pos):
                    if cnt >= len(p) - 1:
                        cnt = 0
                    else:
                        cnt += 1
                    post = p[cnt]

                if buttons.like_button.is_hovered(mouse_pos):
                    post.AddLikes()

                if buttons.comment_button.is_hovered(mouse_pos):
                    post.AddComment()

                if buttons.view_more_comments_button.is_hovered(mouse_pos):
                    post.view_more_comments()

        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        post.Display()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


main()
