import pygame
import random
from egitest import Egitest
width,height=1000,800
screen = pygame.display.set_mode((width,height))
running = True
nap=Egitest(10000,30,[width/2,height/2],(255,255,0))
#fold=Egitest(5,10,[width/2,height/8],(0,255,0),[0.67,0])
#hold=Egitest(0.06,3,[width/2+20,height/8],(200,200,200),[0.67,0.05])
clock = pygame.time.Clock()
STEP = 5
MAX_FRAME = 100 
accumulator = 0
egitestek=[nap]
for i in range(20):
    m=random.randint(1,1000)/10
    r=min(m+1,20)
    pos=[random.randint(0,width),random.randint(0,height)]
    color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    v=[random.randrange(-100,100)/100,random.randrange(-100,100)/100]
    egitest=Egitest(m,r,pos,color,v)
    egitestek.append(egitest)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #screen.fill((0, 0, 0))
    for egitest in egitestek:
        egitest.draw(screen)
    pygame.display.flip()
    accumulator += min(clock.tick(60), MAX_FRAME)
    while accumulator >= STEP:
        for egitest1 in egitestek:
            for egitest2 in egitestek:
                if egitest1 is not egitest2:
                    egitest1.cal_force(egitest2)
        for egitest in egitestek:
            egitest.update()
        accumulator -= STEP

pygame.quit()