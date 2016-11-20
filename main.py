def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption('Life Game')

    mainBoard = getInitialBoard()


    DISPLAYSURF.fill(BGCOLOR)
    drawBoard(mainBoard)

    while True: # main game loop
        mouseClicked = False

        DISPLAYSURF.fill(BGCOLOR) # drawing the window
        drawBoard(mainBoard)

        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy != None:
            # The mouse is currently over a box.
            if mainBoard[boxx][boxy]==DIE:
                drawHighlightBox(boxx, boxy)
            if mainBoard[boxx][boxy]==DIE and mouseClicked:
                mainBoard[boxx][boxy] = LIVE # set the box as "revealed"

        pygame.display.update()
        FPSCLOCK.tick(FPS)