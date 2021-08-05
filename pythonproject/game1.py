import pygame
x = pygame.init()
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
x = 45
y = 50
sz = 10
fps = 45
clock = pygame.time.Clock()
window = pygame.display.set_mode((1280,720))
name  = pygame.display.set_caption(("Game Of Snake"))
exit = False
while not exit:
    for work in pygame.event.get():
        if work.type==pygame.QUIT:
            exit = True
        if work.type==pygame.KEYDOWN:
            print("Sangam")
    window.fill(red)
    pygame.draw.rect(window,black,[x,y,sz,sz])
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
