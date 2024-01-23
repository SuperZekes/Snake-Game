import tkinter as tk
import random

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        
        self.canvas = tk.Canvas(self.window, width=400, height=400)
        self.canvas.pack()
        
        self.snake = [[50, 50], [40, 50], [30, 50]]
        self.food = [random.randint(0, 39) * 10, random.randint(0, 39) * 10]
        
        self.direction = 'right'
        self.score = 0
        
        self.display_snake()
        self.display_food()
        
        self.window.bind('<Key>', self.change_direction)
        
    def display_snake(self):
        self.canvas.delete('snake')
        for pos in self.snake:
            x, y = pos
            self.canvas.create_rectangle(x, y, x+10, y+10, fill='green', tag='snake')
            
    def display_food(self):
        self.canvas.delete('food')
        x, y = self.food
        self.canvas.create_rectangle(x, y, x+10, y+10, fill='red', tag='food')
        
    def change_direction(self, event):
        if event.keysym == 'Up' and self.direction != 'down':
            self.direction = 'up'
        elif event.keysym == 'Down' and self.direction != 'up':
            self.direction = 'down'
        elif event.keysym == 'Left' and self.direction != 'right':
            self.direction = 'left'
        elif event.keysym == 'Right' and self.direction != 'left':
            self.direction = 'right'
            
    def move_snake(self):
        head = self.snake[0]
        if self.direction == 'up':
            new_head = [head[0], head[1] - 10]
        elif self.direction == 'down':
            new_head = [head[0], head[1] + 10]
        elif self.direction == 'left':
            new_head = [head[0] - 10, head[1]]
        elif self.direction == 'right':
            new_head = [head[0] + 10, head[1]]
            
        self.snake.insert(0, new_head)
        
        if self.snake[0] == self.food:
            self.score += 1
            self.food = [random.randint(0, 39) * 10, random.randint(0, 39) * 10]
        else:
            self.snake.pop()
        
        self.display_snake()
        self.display_food()
        
        self.check_game_over()
        self.window.after(100, self.move_snake)
        
    def check_game_over(self):
        if self.snake[0][0] < 0 or self.snake[0][0] > 390 or self.snake[0][1] < 0 or self.snake[0][1] > 390:
            self.game_over()
        for pos in self.snake[1:]:
            if pos == self.snake[0]:
                self.game_over()
                
    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(150, 200, text="Game Over!", font=('Arial', 30))
        self.canvas.create_text(150, 250, text=f"Score: {self.score}", font=('Arial', 20))
        
game = SnakeGame()
game.move_snake()
game.window.mainloop()
