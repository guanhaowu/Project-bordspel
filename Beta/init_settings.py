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
#Amount of columns excluding Name column on OverzichtGegevens.
def OvTable():
    OverzichtColumn = 8
    OverzichtRows = 4
    return OverzichtColumn, OverzichtRows

def OverzichtData(type):
    if type == 'name':
        # Initial Data for Namen
        spelerNamen = {"speler1":"", "speler2":"", "speler3":"", "speler4":""}
        return spelerNamen
    
    if type == 'field':
        selected_field = None
        return selected_field
    
    if type =='data':
        # Initial Data for GegevensOverzicht
        player1 = { 'RoodvGroen': 0, 'RoodvBlauw' : 0, 'RoodvGeel' : 0, 'jail':0, 'jack':0, 'streak': 0 }
        player2 = { 'GroenvRood': 0, 'GroenvBlauw': 0, 'GroenvGeel': 0, 'jail':0, 'jack':0, 'streak': 0 }
        player3 = { 'BlauwvRood': 0, 'BlauwvGroen': 0, 'BlauwvGeel': 0, 'jail':0, 'jack':0, 'streak': 0 }
        player4 = { 'GeelvRood' : 0, 'GeelvGroen' : 0, 'GeelvBlauw': 0, 'jail':0, 'jack':0, 'streak': 0 }
        return player1, player2, player3, player4

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
