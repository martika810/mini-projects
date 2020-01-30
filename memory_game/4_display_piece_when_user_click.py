import random, pygame, sys
from pygame.locals import *

BLUE     = (  0,   0, 255)
RED      = (255,   0,   0)
NAVYBLUE = ( 60,  60, 100)

BOXSIZE = 39
SQUARE = 'square'
DIAMOND = 'diamond'

def find_box_clicked(x, y):
    if(x==-1 and y==-1):
        return (None,None)
    for boxx in range(10):
        for boxy in range(10):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE , BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)

def draw_game_piece(display, shape, color, boxx, boxy):
    BOXSIZE = 39
    quarter = int(BOXSIZE * 0.25) # syntactic sugar
    half =    int(BOXSIZE * 0.5)  # syntactic sugar

    left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from board coords
    # Draw the shapes
    if shape == SQUARE:
        pygame.draw.rect(display, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
    else:
        pygame.draw.polygon(display, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))

def create_matrix_unresolved_boxes():
    return create_empty_board()

def mark_pair_as_resolved_in(board, box1, box2):
    board[box1[0]][box1[1]] = 1
    board[box2[0]][box2[1]] = 1
    return board

def find_all_possible_game_pieces():
    pieces = []
    for color in [RED,BLUE]:
        for shape in [SQUARE,DIAMOND]:
            pieces.append( (shape, color) )
    return pieces

def pick_random_game_piece():
    allPieces = find_all_possible_game_pieces()
    randomNumber = random.randint(0,len(allPieces)-1)
    return allPieces[randomNumber]

def pick_random_box_in_board():
    return (random.randint(0,9), random.randint(0,9))

def find_random_empty_box_in(board):
    if(not(is_board_full(board))):
        random_box = pick_random_box_in_board()
        trylimit=0
        while(is_box_empty_in(board,random_box[0],random_box[1]) and trylimit<5):
            trylimit=+1
            return random_box

    return -1


def create_empty_board():
    board = []
    for row in range(0,10):
        emptyRow = []
        for col in range(0,10):
            emptyRow.append(0)
        board.append(emptyRow)
    return board

def is_board_full(board):
    for row in range(0,10):
        index = board[row].index(0) if 0 in board[row] else -1
        if(index!=-1):
            return False
    return True

def is_box_empty_in(board, row,column):
    return board[row][column]==0


def find_empty_box_in(board):
    for row in range(0,10):
        index = board[row].index(0) if 0 in board[row] else -1
        if(index!=-1):
            return (row,index)
    return -1

def fill_game_board(board):
    while(not(is_board_full(board))):
        pieceToInsertInBoard = pick_random_game_piece()
        firstEmptyBox = find_empty_box_in(board)
        secondEmptyBox = find_random_empty_box_in(board)
        if(firstEmptyBox!=-1 and secondEmptyBox !=-1):
            board[firstEmptyBox[0]][firstEmptyBox[1]] = pieceToInsertInBoard
            board[secondEmptyBox[0]][secondEmptyBox[1]] = pieceToInsertInBoard

    return board

def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (39 + 1)
    top = boxy * (39 + 1)
    return (left, top)

def draw_board(display, board, clicked_boxes):
    BOXSIZE= 39
    for row in range(1,10):
        for col in range(1,10):
            if (row, col) in clicked_boxes:
                game_piece = board[row][col]
                draw_game_piece(display, game_piece[0], game_piece[1], row, col)
            else:
                left, top = leftTopCoordsOfBox(row, col)
                pygame.draw.rect(display, (0,0,0), (left, top, BOXSIZE, BOXSIZE))



def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((440,440))
    DISPLAYSURF.fill(NAVYBLUE)
    running = True
    resolved_boxes_matrix = create_matrix_unresolved_boxes()
    board = create_empty_board()
    board= fill_game_board(board)
    clicked_boxes = []
    mousex=-1
    mousey=-1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        boxx, boxy = find_box_clicked(mousex, mousey)
        if boxx != None and boxy != None: # This means the mouse is over a box
            if mouseClicked:
                clicked_boxes.append((boxx, boxy))
        draw_board(DISPLAYSURF, board, clicked_boxes)
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.time.Clock().tick(40)
    pygame.quit()


main()


