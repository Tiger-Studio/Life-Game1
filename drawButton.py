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
    if buttonNum==0:
        basicFont = pygame.font.SysFont(None, 35)  
        text = basicFont.render(" next  ", True, BLACK, GRAY) 
        textRect = text.get_rect()     
        textRect.centerx = left+BUTTONWIDTH/2
        textRect.centery = top+BUTTONHEIGHT/2  
        DISPLAYSURF.blit(text, textRect)
    if buttonNum==1:
        basicFont = pygame.font.SysFont(None, 35)  
        text = basicFont.render(" reset ", True, BLACK, GRAY) 
        textRect = text.get_rect()     
        textRect.centerx = left+BUTTONWIDTH/2
        textRect.centery = top+BUTTONHEIGHT/2  
        DISPLAYSURF.blit(text, textRect) 
    if buttonNum==2:
        basicFont = pygame.font.SysFont(None, 35)  
        text = basicFont.render(Button_Auto, True, BLACK, GRAY) 
        textRect = text.get_rect()     
        textRect.centerx = left+BUTTONWIDTH/2
        textRect.centery = top+BUTTONHEIGHT/2  
        DISPLAYSURF.blit(text, textRect) 
