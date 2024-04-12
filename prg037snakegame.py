import random

class SnakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2)]
        self.food = self.generate_food()

    def generate_food(self):
        while True:
            food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if food not in self.snake:
                return food

    def move_snake(self, direction):
        head = self.snake[0]
        if direction == 'up':
            new_head = (head[0], head[1] - 1)
        elif direction == 'down':
            new_head = (head[0], head[1] + 1)
        elif direction == 'left':
            new_head = (head[0] - 1, head[1])
        elif direction == 'right':
            new_head = (head[0] + 1, head[1])

        if (new_head in self.snake or
            new_head[0] < 0 or new_head[0] >= self.width or
            new_head[1] < 0 or new_head[1] >= self.height):
            return False  # Konec hry
        else:
            self.snake.insert(0, new_head)
            if new_head == self.food:
                self.food = self.generate_food()
            else:
                self.snake.pop()
            return True  # Hra pokračuje

# Inicializace hry
game = SnakeGame(10, 10)

# Příklad hraní hry
while True:
    print("Snake:", game.snake)
    print("Food:", game.food)
    direction = input("Enter direction (up/down/left/right): ")
    if game.move_snake(direction):
        print("Continue playing")
    else:
        print("Game over")
        break