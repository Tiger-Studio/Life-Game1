def getNext_generation(board):
    newboard = [] 
    for boxx in range(BOARDWIDTH):
        column=[]
        for boxy in range(BOARDHEIGHT):
            column.append(board[boxx][boxy])
        newboard.append(column)
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            lifeCount=0
            if board[boxx][boxy]==LIVE:
                lifeCount=lifeCount+1
            if (boxx-1)>=0 and (boxy-1)>=0 and board[boxx-1][boxy-1]==LIVE:
                lifeCount=lifeCount+1
            if (boxx-1)>=0 and board[boxx-1][boxy]==True:
                lifeCount=lifeCount+1
            if (boxx-1)>=0 and (boxy+1)<BOARDHEIGHT and board[boxx-1][boxy+1]==LIVE:
                lifeCount=lifeCount+1
            if (boxy-1)>=0 and board[boxx][boxy-1]==LIVE:
                lifeCount=lifeCount+1
            if (boxy+1)<BOARDHEIGHT and board[boxx][boxy+1]==LIVE:
                lifeCount=lifeCount+1
            if (boxx+1)<BOARDWIDTH and (boxy-1)>=0 and board[boxx+1][boxy-1]==LIVE:
                lifeCount=lifeCount+1
            if (boxx+1)<BOARDWIDTH and board[boxx+1][boxy]==LIVE:
                lifeCount=lifeCount+1
            if (boxx+1)<BOARDWIDTH and (boxy+1)<BOARDHEIGHT and board[boxx+1][boxy+1]==LIVE:
                lifeCount=lifeCount+1
            if(lifeCount<=lifeMax and lifeCount>=lifeMin):
                newboard[boxx][boxy]=LIVE
            else:
                newboard[boxx][boxy]=DIE
    return newboard
