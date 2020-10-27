import pygame, random

from abc import ABC, abstractmethod


class Direction:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Drawable(ABC):
    color = (0, 0, 0)
    @abstractmethod
    def draw(self, surface): pass


class Food(Drawable):
    def __init__(self):
        super().__init__()
        self.points = 10
        self.position = (0, 0)
        self.color = (223, 163, 49)

    def random_position(self, WIDTH, HEIGHT, size):
        self.position = (
            random.randint(0, WIDTH - 1) * size,
            random.randint(0, HEIGHT - 1) * size,
        )

    def draw(self, surface, size):
        (x, y) = self.position
        rect = pygame.Rect((x, y), (size, size))
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, (93, 216, 228), rect, 1)


class Snake(Drawable):
    # constructor
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color = (17, 24, 47)
        self.positions = [position]
        self.direction = Direction.RIGHT

    def __can_turn(self, direction):
        return self.direction[0] != direction[0] and self.direction[1] != direction[1]

    def turn(self, direction):
        if (self.__can_turn(direction)):
            self.direction = direction

    def hit_food(self, food):
        if (self.positions[0] == food.position):
            self.score += food.points
            self.positions.append(food.position)
            return True
        return False

    def __valid_position(self, width, height, position):
        (i, j) = position
        return not position in self.positions and 0 <= i and i < width and 0 <= j and j < height

    def __reset(self, width, height):
        self.score = 0
        self.direction = Direction.RIGHT
        self.positions = [(width/2, height/2)]

    def move(self, width, height, size):
        a, b = self.positions[0]
        x, y = self.direction
        new_position = (
            (a + (x * size)),
            (b + (y * size))
        )
        if (self.__valid_position(width, height, new_position)):
            self.positions.insert(0, new_position)
            self.positions.pop()
        else:
            self.__reset(width, height)

    def draw(self, surface, size):
        for position in self.positions:
            (x, y) = position
            rect = pygame.Rect((x, y), (size, size))
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, (93, 216, 228), rect, 1)
