import pygame
import math

G = 0.001


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

    def calc_force(self, other):
        dx = other.pos[0] - self.pos[0]
        dy = other.pos[1] - self.pos[1]
        d2 = dx * dx + dy * dy
        if d2 == 0:
            dx = 1
            dy = 0
            d2 = 1

        d = math.sqrt(d2)
        if d < self.r + other.r:
            nx = dx / d
            ny = dy / d
            overlap = self.r + other.r - d
            total_mass = self.m + other.m
            self_move = overlap * other.m / total_mass
            other_move = overlap * self.m / total_mass

            self.pos[0] -= nx * self_move
            self.pos[1] -= ny * self_move
            other.pos[0] += nx * other_move
            other.pos[1] += ny * other_move

            rel_vx = other.v[0] - self.v[0]
            rel_vy = other.v[1] - self.v[1]
            rel_speed = rel_vx * nx + rel_vy * ny
            if rel_speed < 0:
                restitution = 0.8
                impulse = -(1 + restitution) * rel_speed / (1 / self.m + 1 / other.m)
                self.v[0] -= (impulse / self.m) * nx
                self.v[1] -= (impulse / self.m) * ny
                other.v[0] += (impulse / other.m) * nx
                other.v[1] += (impulse / other.m) * ny
            return

        a = G * other.m / d2
        self.a[0] += dx / d * a
        self.a[1] += dy / d * a

    def update(self):
        self.v[0] += self.a[0]
        self.v[1] += self.a[1]
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
        self.a=[0,0]
