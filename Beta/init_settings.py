### Screen Size.
def getScreenSize():
    screen_xSize = 1200
    screen_ySize = 900
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

### OverzichtGegevens Tab content.
def OverzichtData(type):
    if type == 'data':
        # Initial Data for Namen
        player = {
                       'speler1':{'name':'', 'data':[0, 1, 2, 3, 4, 5]},
                       'speler2':{'name':'', 'data':[0, 5, 0, 1, 2, 2]},
                       'speler3':{'name':'', 'data':[0, 6, 0, 5, 4, 9]},
                       'speler4':{'name':'', 'data':[0, 7, 0, 2, 8, 3]}
                       }
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
def debug(type, *args):
    if type == 'mouse':
        debug_MouseLoc = True
    return debug_MouseLoc
