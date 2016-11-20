def leftTopCoordsOfButton(buttonNum):
    # Convert board coordinates to pixel coordinates
    left = WINDOWWIDTH-XMARGIN-BUTTONWIDTH*(buttonNum+1)-BUTTONGAP*buttonNum
    top = WINDOWHEIGHT
    return (left, top)

def getButtonAtPixel(x, y):
    for buttonNum in range(BUTTONCOUNT):
        left, top = leftTopCoordsOfButton(buttonNum)
        boxRect = pygame.Rect(left, top, BUTTONWIDTH, BUTTONHEIGHT)
        if boxRect.collidepoint(x, y):
            return buttonNum
    return None

def drawButton(buttonNum):
    left,top=leftTopCoordsOfButton(buttonNum)
    if buttonNum==NextButton:
        basicFont = pygame.font.SysFont(None, 35)  
        text = basicFont.render(Button_Next, True, BLACK, GRAY) 
        textRect = text.get_rect()     
        textRect.centerx = left+BUTTONWIDTH/2
        textRect.centery = top+BUTTONHEIGHT/2  
        DISPLAYSURF.blit(text, textRect)
    if buttonNum==ResetButton:
        basicFont = pygame.font.SysFont(None, 35)  
        text = basicFont.render(Button_Reset, True, BLACK, GRAY) 
        textRect = text.get_rect()     
        textRect.centerx = left+BUTTONWIDTH/2
        textRect.centery = top+BUTTONHEIGHT/2  
        DISPLAYSURF.blit(text, textRect) 
    if buttonNum==RunButton:
        basicFont = pygame.font.SysFont(None, 35)  
        text = basicFont.render(Button_Run, True, BLACK, GRAY) 
        textRect = text.get_rect()     
        textRect.centerx = left+BUTTONWIDTH/2
        textRect.centery = top+BUTTONHEIGHT/2  
        DISPLAYSURF.blit(text, textRect) 
    if buttonNum==HelpButton:
        basicFont = pygame.font.SysFont(None, 35)  
        text = basicFont.render(Button_Help, True, BLACK, GRAY) 
        textRect = text.get_rect()     
        textRect.centerx = left+BUTTONWIDTH/2
        textRect.centery = top+BUTTONHEIGHT/2  
        DISPLAYSURF.blit(text, textRect) 
