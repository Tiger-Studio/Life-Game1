def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, TrueWINDOWHEIGHT))

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    MouseButton=0
    down=1
    up=2
    clickstate=None
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
                MouseButton=down
            if event.type == MOUSEBUTTONUP: 
                mousex, mousey = event.pos 
                BUTTON_CLICK=True
                MouseButton=up
                
                ####mouseClicked = True
        
        boxx, boxy = getBoxAtPixel(mousex, mousey)
        buttonNum=getButtonAtPixel(mousex, mousey)
        if MouseButton==down:
            if boxx != None and boxy !=None and clickstate==None:
                if mainBoard[boxx][boxy]==DIE:
                    clickstate=DIE
                    mainBoard[boxx][boxy] = LIVE
                elif mainBoard[boxx][boxy]==LIVE:
                    clickstate=LIVE  
                    mainBoard[boxx][boxy] = DIE 
            elif boxx != None and boxy !=None and clickstate==DIE:
                if mainBoard[boxx][boxy]==DIE:
                    mainBoard[boxx][boxy] = LIVE
            elif boxx != None and boxy !=None and clickstate==LIVE:
                if mainBoard[boxx][boxy]==LIVE:
                    mainBoard[boxx][boxy] = DIE
        if MouseButton==up:
            clickstate=None
        if boxx != None and boxy != None: 
            drawHighlightBox(boxx, boxy)
        #print MouseButton,clickstate
        
        if buttonNum!=None and BUTTON_CLICK==True:            
            #mainBoard=getNextBoard()
            if buttonNum==1:
                mainBoard =getInitialBoard()
                  ##### if firstSelection == None: # the current box was the first box clicked

        pygame.display.update()
        FPSCLOCK.tick(FPS)
