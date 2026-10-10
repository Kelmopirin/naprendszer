import pygame
from egitest import Egitest
width,height=800,600
screen = pygame.display.set_mode((width,height))
running = True
nap=Egitest(10000,30,[width/2,height/2],(255,255,0))
fold=Egitest(5,10,[width/2
                   ,height/4],(0,255,0),[0.25,0])
clock = pygame.time.Clock()
STEP = 5  # fix szimulációs lépés ms-ban, gépfüggetlen
MAX_FRAME = 100  # hosszú képkockáknál ne szaladjon el a szimuláció
accumulator = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    nap.draw(screen)
    fold.draw(screen)
    pygame.display.flip()
    accumulator += min(clock.tick(60), MAX_FRAME)
    while accumulator >= STEP:
        fold.cal_force(nap)
        nap.cal_force(fold)
        nap.update()
        fold.update()
        accumulator -= STEP

pygame.quit()