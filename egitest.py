import pygame
import math

G = 0.01


class Egitest:
    def __init__(self, m, r, pos, color, v=None):
        self.m = m
        self.r = r
        self.pos = list(pos)
        self.color = color
        self.v = list(v) if v is not None else [0, 0]
        self.a = [0, 0]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.r)

    def cal_force(self, other):
        dx = other.pos[0] - self.pos[0]
        dy = other.pos[1] - self.pos[1]
        d2 = dx * dx + dy * dy
        if d2 == 0:
            self.a = [0, 0]
            return
        d = math.sqrt(d2)
        a = G * other.m / d2
        self.a[0] += dx / d * a
        self.a[1] += dy / d * a

    def update(self):
        self.v[0] += self.a[0]
        self.v[1] += self.a[1]
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
        self.a=[0,0]
