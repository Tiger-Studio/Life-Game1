def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, TrueWINDOWHEIGHT))

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    firstclick=0
    pygame.button_down = False
    pygame.display.set_caption('Life Game')

    mainBoard = getInitialBoard()

    #####firstSelection = None # stores the (x, y) of the first box clicked.

    DISPLAYSURF.fill(BGCOLOR)
    drawBoard(mainBoard)

    while True: # main game loop
    

        DISPLAYSURF.fill(BGCOLOR) # drawing the window
        drawBoard(mainBoard)
        BUTTON_CLICK=False
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                pygame.button_down = True
                firstclick=1
            if event.type == MOUSEBUTTONUP: 
                mousex, mousey = event.pos 
                pygame.button_down = False
                BUTTON_CLICK=True
                firstclick=2
                
                ####mouseClicked = True
        
        boxx, boxy = getBoxAtPixel(mousex, mousey)
        buttonNum=getButtonAtPixel(mousex, mousey)
        if boxx != None and boxy != None and pygame.button_down == True:
            if mainBoard[boxx][boxy]==DIE:
                 mainBoard[boxx][boxy] = LIVE
        elif boxx != None and boxy != None and BUTTON_CLICK==True:
            if mainBoard[boxx][boxy]==LIVE:
                 mainBoard[boxx][boxy] = DIE
                 drawHighlightBox(boxx, boxy)
        elif boxx != None and boxy != None: 
             drawHighlightBox(boxx, boxy)
                # set the box as "revealed"
        if buttonNum!=None and BUTTON_CLICK==True:            
            #mainBoard=getNextBoard()
            if buttonNum==1:
                mainBoard =getInitialBoard()
                  ##### if firstSelection == None: # the current box was the first box clicked

        pygame.display.update()
        FPSCLOCK.tick(FPS)
