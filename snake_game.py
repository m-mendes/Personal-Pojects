import pygame
from pygame.constants import *
import time
import random

SIZE = 25
class Apple:
    def __init__(self, habitat) -> None:
        self.apple_x = SIZE * 3
        self.apple_y =  SIZE * 3
        self.habitat = habitat
        self.apple_height = 25
        self.apple_weight = 25

    def draw(self):
        pygame.draw.rect(self.habitat, (255,255,255), (self.apple_x, self.apple_y, self.apple_height, self.apple_weight))
        pygame.display.flip()

    def move(self):
        self.apple_y = random.randint(0,15)*SIZE
        self.apple_x = random.randint(0,20)*SIZE

class Snake:
    def __init__(self,surface, lenght) -> None:
        self.lenght = lenght
        self.habitat = surface
        self.snake_x = [25] * lenght 
        self.snake_y = [25] * lenght
        self.snake_height = 25
        self.snake_weight = 25
        self.direction = 'down'

    def increase_lenght(self):
        self.lenght+=1
        self.snake_x.append(-1)
        self.snake_y.append(-1)  

    def draw_snake(self):

        for i in range(self.lenght):
            pygame.draw.rect(self.habitat, (255,0,0), (self.snake_x[i],self.snake_y[i],self.snake_height,self.snake_weight))  
        pygame.display.flip()

    def move_right(self):
        self.direction = 'right'

    def move_left(self):
        self.direction = 'left'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move(self):

        for i in range(self.lenght -1 ,0,-1):
            self.snake_x[i] = self.snake_x[i-1]
            self.snake_y[i] = self.snake_y[i-1]

        if self.direction == 'left':
            self.snake_x[0] -= 25
            self.move_left()
        if self.direction == 'right':
            self.snake_x[0] += 25
            self.move_right()
        if self.direction == 'up':
            self.snake_y[0] -= 25
            self.move_up()
        if self.direction == 'down':
            self.snake_y[0] += 25
            self.move_down()
        self.draw_snake()



class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,800))
        self.surface.fill((0,0,255))
        self.snake = Snake(self.surface,1)
        self.snake.draw_snake()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_colision(self,x1,x2,y1,y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
    
    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f'Score: {self.snake.lenght}', True, (200,200,200))
        self.surface.blit(score, (800,10))

    def play(self):
        self.snake.move()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_colision(self.snake.snake_x[0],self.apple.apple_x,self.snake.snake_y[0],self.apple.apple_y):
            self.snake.increase_lenght()
            self.apple.move()            

        for i in range(1,self.snake.lenght):
            if self.is_colision(self.snake.snake_x[0],self.snake.snake_x[i],self.snake.snake_y[0],self.snake.snake_y[i]):
                raise "Game Over"

    def show_game_over(self):
        self.surface.fill((0,0,0))
        font = pygame.font.SysFont('arial',30)
        line1 = font.render(f'Score: {self.snake.lenght}', True, (200,200,200))
        self.surface.blit(line1, (200,300))
        line2 = font.render("To play again press Enter, To exit press ESC", True, (200,200,200))
        self.surface.blit(line2, (250,350))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface,1)
        
        self.apple = Apple(self.surface)



    def run(self):
        running = True
        pause = False
        while running:
            self.surface.fill((0,0,255))

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False
                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down ()
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                    
                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(0.4)

if __name__ == "__main__":
    game = Game()
    game.run()
    


