import pygame
from egitest import Egitest
import random
import math

width,height=800,600
screen = pygame.display.set_mode((width,height))
running = True
nap=Egitest(10000,40,[width/2,height/2],(255,255,0))
egitestek = [nap]
center_x, center_y = width/2, height/2

for i in range(10):
    m=random.randint(10,200)
    r=m/10
    orbit_radius = random.uniform(120, 350)
    angle = random.uniform(0, 2 * math.pi)
    pos=[center_x + math.cos(angle) * orbit_radius, center_y + math.sin(angle) * orbit_radius]
    color=(random.randint(30,255),random.randint(30,255),random.randint(30,255))

    orbit_speed = math.sqrt((0.001 * nap.m) / orbit_radius)
    tangential_speed = orbit_speed * random.uniform(0.9, 1.1)
    speed=[-math.sin(angle) * tangential_speed, math.cos(angle) * tangential_speed]

    egitestek.append(Egitest(m,r,pos,color,speed))
clock = pygame.time.Clock()
STEP = 5  # fix szimulációs lépés ms-ban, gépfüggetlen
MAX_FRAME = 100  # hosszú képkockáknál ne szaladjon el a szimuláció
accumulator = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for egitest in egitestek:
        egitest.draw(screen)
    pygame.display.flip()
    accumulator += min(clock.tick(60), MAX_FRAME)
    while accumulator >= STEP:
        for egitest1 in egitestek:
            for egitest2 in egitestek:
                if egitest1 != egitest2:
                    egitest1.calc_force(egitest2)
        for egitest in egitestek:
            egitest.update()
        accumulator -= STEP

pygame.quit()