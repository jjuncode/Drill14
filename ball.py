from pico2d import *
import game_world
import game_framework
import random

import server


class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(-500, 500)
        self.y = y if y else random.randint(-500, 500)

    def draw(self):
        sx, sy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.draw(sx, sy)
        draw_rectangle(*self.get_bb())

    def update(self):
        print(self.x,self.y)

    def get_bb(self):
        sx, sy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        return sx - 10, sy - 10, sx + 10, sy + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                other.ball = self # 소년이 볼을 소유하도록.
                pass
            case 'zombie:ball':
                other.ball = self

    def set_background(self, bg):
        # fill here
        self.bg = bg
        self.x += self.bg.w//2
        self.y += self.bg.h//2