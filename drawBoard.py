def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)

def drawBox(board, boxx, boxy):
    half = int(BOXSIZE * 0.5)  # syntactic sugar
    
    shape, color=getBoxShapeAndColor(board, boxx, boxy)
    left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from board coords
    # Draw the shapes
    if shape == CIRCLE:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half)
    if shape == RECT:
        pygame.draw.rect(DISPLAYSURF,color,(left,top,BOXSIZE,BOXSIZE))
    


def getBoxShapeAndColor(board, boxx, boxy):
    # shape value for x, y spot is stored in board[x][y][0]
    # color value for x, y spot is stored in board[x][y][1]
    if board[boxx][boxy]==LIVE:
        return CIRCLE,RED
    else:
        return RECT,BOXCOLOR


def drawBoard(board):
    # Draws all of the boxes in their covered or revealed state.
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            drawBox(board, boxx, boxy)
                
    for buttonNum in range(BUTTONCOUNT):
        left,top=leftTopCoordsOfButton(buttonNum)
        pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BUTTONWIDTH, BUTTONHEIGHT))
        drawButton(buttonNum)
