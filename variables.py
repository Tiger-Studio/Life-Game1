FPS = 10000 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
TrueWINDOWHEIGHT=540
REVEALSPEED = 8 # speed boxes' sliding reveals and covers
BOXSIZE = 5 # size of box height & width in pixels
GAPSIZE = 2 # size of gap between boxes in pixels
BOARDWIDTH = 80 # number of columns of icons
BOARDHEIGHT = 50 # number of rows of icons
BUTTONCOUNT = 3
BUTTONGAP=20
BUTTONWIDTH=62
BUTTONHEIGHT=31
lifeMax=3
lifeMin=3
#assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)


DIE=0
LIVE=1

CIRCLE= 'circle'
RECT= 'rect'

Button_Auto="  run  "

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = BLACK
HIGHLIGHTCOLOR = BLUE
BUTTONCOLOR = WHITE

