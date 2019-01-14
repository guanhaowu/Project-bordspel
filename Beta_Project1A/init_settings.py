### Screen Size.
def getScreenSize():
    screen_xSize = 1200
    screen_ySize = 800
    return screen_xSize, screen_ySize

### Default page.
def getTab():
    activeTab = 0
    return activeTab

### Main Tab content.
# List of Menu items.
def getMenuList():
    #Menu button names
    tabNames = ['Overzicht', 'Duelleren', 'Shortcut', 'Kaartregels', 'Namen']
    return tabNames

### Load Background image once.
def loadBG():
    return loadImage("background_img.png")

### Background Image resizing.
def getBgImg(bgImg, xSize, ySize):
    bgImg.resize(xSize, ySize)
    x = background(bgImg)
    return x

### Card Resize settings - not used for now.
def getCardSize():
    x= 230
    y= 250
    return x,y

### Plus & Minus icon resize
def getIconSize():
    x = getTextSize(1)*1.2
    y = x
    return x,y

### OverzichtGegevens Tab content.
def OverzichtData(type):
    if type == 'data':
        # Initial Data for Namen
        player = {'speler1':{'name':'', 'data':[0, 0, 0, 0, 0, 0]},
                  'speler2':{'name':'', 'data':[0, 0, 0, 0, 0, 0]},
                  'speler3':{'name':'', 'data':[0, 0, 0, 0, 0, 0]},
                  'speler4':{'name':'', 'data':[0, 0, 0, 0, 0, 0]}}
        return player
    
    if type == 'colName':
        colName = ['Totaal', 'Gevangenis', 'Boer', 'Reeks']
        return colName
    
    if type == 'field':
        selected_field = None
        return selected_field
    
#Amount of columns excluding Name column on OverzichtGegevens.
def OvTable():
    OverzichtColumn = 8
    OverzichtRows = len(OverzichtData('data'))
    return OverzichtColumn, OverzichtRows

### Namen & OverzichtGegevens Tab content.
def getInputField(tab, args):
    ### Input_field width & height in Names.
    if tab == 'name' and args == 'width':
        inputFieldWidth = 308
        return inputFieldWidth
    if tab == 'name' and args == 'height':
        inputFieldHeight = 120
        return inputFieldHeight
    
    ### Input_field width & height in OverzichtGegevens.
    if tab =='overzicht' and args =='width':
        inputFieldWidth = 100
        return inputFieldWidth
    if tab =='overzicht' and args =='height':
        inputFieldHeight = getTextSize(1)*1.5
        return inputFieldHeight

### Reset buttons for Overzicht.
def getResetKnop(type, screen_xSize, screen_ySize):
    if type == 'ResetAll':
        #Reset alles BTN setting
        resetBtnStartX = screen_xSize*0.05
        resetBtnEndX = 200 #button width from resetBtnStartX
        resetBtnStartY = screen_ySize*0.5 #button height from top
        resetBtnEndY = 35 #height from resetBtnStartY
        return resetBtnStartX, resetBtnEndX, resetBtnStartY, resetBtnEndY

    if type == 'ResetReeks':
        #Reset Reeks BTN setting
        resetReeksBtnStartX = screen_xSize*0.76
        resetReeksBtnEndX = 150 #button width from resetReeksBtnStartX
        resetReeksBtnStartY = screen_ySize*0.5 #button height from top
        resetReeksBtnEndY = 35 #height from resetReeksBtnStartY
        return resetReeksBtnStartX, resetReeksBtnEndX, resetReeksBtnStartY, resetReeksBtnEndY
        
                
### Dueleren Tab.
# amount of dices Attacker have
def getDiceCounter():
    diceCount = 4
    return diceCount

### Standard font size.    
def getTextSize(num):
    # font size
    if num == 0: 
        textsize0 = 30 
        return textsize0
    
    if num == 1: 
        textsize1 = 24
        return textsize1
    
    if num == 2:     
        textsize2 = getTextSize(1)-2
        return textsize2
    
    if num == 3:
        textsize3 = getTextSize(2)-4
        return textsize3

### DEBUG.
def debug(type, args):
    if type == 'mouse':
        debug_MouseLoc = args
    return debug_MouseLoc
