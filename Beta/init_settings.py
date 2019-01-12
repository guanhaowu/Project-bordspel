# Screen Size:
def getScreenSize():
    screen_xSize = 1200
    screen_ySize = 800
    return screen_xSize, screen_ySize

#Default page
def getTab():
    activeTab = 0
    return activeTab

def getMenuList():
    #Menu button names
    tabNames = ['Spel overzicht', 'Duelleren', 'Shortcut', 'Kaartregels', 'Namen']
    return tabNames

def loadBG():
    return loadImage("background_img.png")

#Image resizing
def getBgImg(bgImg, xSize, ySize):
    bgImg.resize(xSize, ySize)
    x = background(bgImg)
    return x

def init(type,*args):
    # Input_field width in Names
    if type == 'inputFieldBtn':
        inputFieldWidth = 308
        return inputFieldWidth
    
    # Initial Data for Namen
    if type == 'TabNamen':
        spelerNamen = {"speler1":"", "speler2":"", "speler3":"", "speler4":""}
        selected_field = None
        return spelerNamen, selected_field
    
    # Initial Data for Dueleren
    # amount of dices Attacker have
    if type == 'DiceCounter':
        diceCount = 4
        return diceCount
    
def getTextSize(num):
    # font size
    if num == 1: 
        textsize0 = 30 
        return textsize0
    
    if num == 2: 
        textsize1 = 24
        return textsize1
    
    if num == 3:     
        textsize2 = getTextSize(1)-2
        return textsize2
    
    if num == 4:
        textsize3 = getTextSize(2)-4
        return textsize3

### DEBUG ####
def debug(type, *args):
    if type == 'mouse':
        debug_MouseLoc = True
    return debug_MouseLoc
