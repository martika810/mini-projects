import random, pygame, sys

BLUE     = (  0,   0, 255)
RED      = (255,   0,   0)
NAVYBLUE = ( 60,  60, 100)


SQUARE = 'square'
DIAMOND = 'diamond'


def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (39 + 1)
    top = boxy * (39 + 1)
    return (left, top)

def draw_square_panel(display):
    BOXSIZE= 39
    for row in range(1,10):
        for col in range(1,10):
            left, top = leftTopCoordsOfBox(row, col)
            pygame.draw.rect(display, (0,0,0), (left, top, BOXSIZE, BOXSIZE))


def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((440,440))
    DISPLAYSURF.fill(NAVYBLUE)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_square_panel(DISPLAYSURF)
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.time.Clock().tick(40)
    pygame.quit()

main()
