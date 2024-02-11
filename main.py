import sys
from time import sleep
from random import randint
import keyboard
from datetime import datetime

HEIGHT, WIDTH = 15,15
SPEED = 0.5

class Game():
    def __init__(self):
        self.board = [[' ' for point in range(WIDTH)] for row in range(HEIGHT)]
        self.snake = Snake(self.board)
        self.keys = {
            'w': (0,-1),
            's': (0,+1),
            'a': (-1,0),
            'd': (+1,0)
        }
        self.clock = None

    def Run(self):
        self.clock = datetime.now()
        while not self.snake.died:
            print('\n\x1b[2J\x1b[H\033[0 Q'+((('\n'.join([''.join(row) for row in self.board])).replace(' ', '\033[100m  \033[0m')).replace('#',  '\033[102m  \033[0m')).replace('@',  '\033[101m  \033[0m')+f'\n\033[1mscore\033[0m {self.snake.apples}',flush = True,end ='')
            for key in self.keys:
                if keyboard.is_pressed(key):
                    if len(self.snake.bodies)<2:
                        self.snake.direction = self.keys[key]
                    else:
                        if not (self.snake.bodies[0][0] + self.keys[key][0],self.snake.bodies[0][1] + self.keys[key][1]) == self.snake.bodies[1]:
                            self.snake.direction = self.keys[key]
                        else:
                            pass
            if keyboard.is_pressed('esc'):
                sys.exit()
            if round(datetime.now().timestamp()-self.clock.timestamp(),1) >= SPEED and self.snake.direction is not (0,0):
                self.snake.Update()
                self.clock = datetime.now()

class Snake():
    def __init__(self, board:list):
        self.board = board
        self.bodies = [(randint(0,WIDTH-1), randint(0,HEIGHT-1))]
        self.board[self.bodies[0][1]][self.bodies[0][0]] = '#'
        self.direction = (0,0)
        self.died = False
        self.apples = 0
        self.NewApple()

    def Update(self):
        if (0 <= self.bodies[0][0] + self.direction[0] < WIDTH and
            0 <= self.bodies[0][1] + self.direction[1] < HEIGHT):
            self.bodies.insert(0,(self.bodies[0][0] + self.direction[0] , self.bodies[0][1] + self.direction[1]))
            if self.board[self.bodies[0][1]][self.bodies[0][0]] == '#':
                self.died = True
            elif self.board[self.bodies[0][1]][self.bodies[0][0]] == '@':
                self.NewApple()
                self.apples+=1
            else:
                curret = self.bodies.pop()
                self.board[curret[1]][curret[0]] = ' '
            self.board[self.bodies[0][1]][self.bodies[0][0]] = '#'
        else:
            self.died = True

    def NewApple(self):
        while True:
            randomPoint = ((randint(0,WIDTH-1), randint(0,HEIGHT-1)))
            if self.board[randomPoint[1]][randomPoint[0]] != '#':
                self.board[randomPoint[1]][randomPoint[0]] = '@'
                return

if __name__ == '__main__':
    Game = Game()
    Game.Run()
