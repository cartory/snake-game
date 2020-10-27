import pygame
# from pygame import * as pygame

from models import *

GAME_TITLE = "SNAKE GAME"
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480


def main():
    game = Game(
        GAME_TITLE,
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
    )
    game.start()


class Game():
    grid_size = 20
    GAME_OVER = False

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.food = Food()
        self.snake = Snake((width/2, height/2))

    def __handle_keys(self):
        for event in pygame.event.get():
            # print(event)
            self.GAME_OVER = event.type == pygame.QUIT
            if (event.type == pygame.KEYDOWN):
                self.GAME_OVER = event.key == pygame.K_ESCAPE
                if event.key == pygame.K_UP:
                    self.snake.turn(Direction.UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.turn(Direction.DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.turn(Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.turn(Direction.RIGHT)

    def __draw(self, surface):
        rows = self.width / self.grid_size
        cols = self.height / self.grid_size

        for i in range(0, int(rows)):
            for j in range(0, int(cols)):
                rect = pygame.Rect(
                    (i * self.grid_size, j * self.grid_size),
                    (self.grid_size, self.grid_size)
                )
                if (i + j) % 2 == 0:
                    pygame.draw.rect(surface, (93, 216, 228), rect)
                else:
                    pygame.draw.rect(surface, (84, 194, 205), rect)

        self.food.draw(surface, self.grid_size)
        self.snake.draw(surface, self.grid_size)

    def __load_food(self):
        self.food.random_position(
            self.width/self.grid_size,
            self.height/self.grid_size,
            self.grid_size
        )

    def start(self):
        pygame.init()
        pygame.display.set_caption(self.title)

        clock = pygame.time.Clock()
        myfont = pygame.font.SysFont("comicsansms", 18)
        surface = pygame.display.set_mode((self.width, self.height))
        self.__load_food()
        while not self.GAME_OVER:
            clock.tick(10)
            self.__handle_keys()
            self.snake.move(self.width, self.height, self.grid_size)

            if (self.snake.hit_food(self.food)):
                self.__load_food()

            text = myfont.render(
                "Your Score " + str(self.snake.score),
                True, (0, 0, 0)
            )

            self.__draw(surface)
            surface.blit(text, (10, 10))

            pygame.display.update()
        #
        pygame.quit()


main()
