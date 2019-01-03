#screensize:
screen_xSize = 1200
screen_ySize = 800
buttonWidth = 12.5
buttonHeight = 5
tabs = [0, 1, 2, 3, 4]
tabNames = ['Spel overzicht', 'Dueleren', 'Rad', 'Kaartregels', 'Namen']
spelerNamen = {"speler1":"", "speler2":"", "speler3":"", "speler4":""}
activeTab = 0
selected_field = None

def setup():
    global screen_xSize, screen_ySize
    global bg_img
    size(screen_xSize, screen_ySize)
    bg_img = loadImage("background_img.png")
    noStroke()  

def menuButton():
    global tabs
    for tab in tabs:
        fill(150)
        stroke(150)
        rect(50+tabs[tab]*150, 10, 125, 50, 10)
        noStroke()
        noFill()

def menuText():
    global tabNames
    for x in range(len(tabNames)):   
        fill(0,0,0)
        fonts("Arial Bold Italic", 13, True)
        textAlign(CENTER)
        text(tabNames[x], 50+(x*150), 30, 125, 50)
        noFill()

def draw_bg(x, screen_xSize, screen_ySize):
    redraw()
    x.resize(screen_xSize, screen_ySize)
    x = background(x)
    return x

def active(tab):
    global screen_xSize, screen_ySize, buttonWidth
    fill(255,255,0)
    stroke(150)
    rect(50+(tab*150), 10, 125, 50, 10)
    noFill()
    
def fonts(font_type,font_size, state):
    return textFont(createFont(font_type,font_size, state))

def OverzichtGegevens():
    fill(0)
    #code
    noFill()


def Duel():
    fill(0)
    #code
    noFill()

def Rad1():
    fill(150)
    # code
    noFill()

def Names():
    global spelerNamen
    
    def field_colors(field):
        if field == 1: return fill(255,0,0)
        if field == 2: return fill(0,255,0)
        if field == 3: return fill(50,70,255)
        if field == 4: return fill(255,255,0)
        
    textAlign(CENTER)
    stroke(0,0,0)
    fill(0,0,0)
    rect(90,120,508,20)
    fill(255,255,255)
    fonts("Arial Bold", 18, True)
    text("Vul uw naam hier onder in:", 200, 120, 398,25)
    noFill()
    noStroke()
    
    fonts("Arial", 16, True)
    for x in range(len(spelerNamen)):
        stroke(0,0,0)
        field_colors(x+1)
        rect(90, 140+(x*20), 108, 20)  #column 1
        fill(255,255,255)
        rect(198, 140+(x*20), 400, 20) #column 2
        noFill()
        noStroke()

    for x in range(len(spelerNamen)):
        fill(0,0,0)
        textAlign(LEFT)
        text("speler" + str(x+1), 100, 155+(x*20))
        text(str(spelerNamen["speler"+str(x+1)]), 200, 155+(x*20))
        noFill()


def mousePressed():
    global activeTab
    global selected_field
    if mouseButton == LEFT:
        if mouseX > 50 and mouseX < 175 and mouseY > 10 and mouseY < 60:
            activeTab = 0
        if mouseX > 200 and mouseX < 325 and mouseY > 10 and mouseY < 60:
            activeTab = 1
        if mouseX > 350 and mouseX < 475 and mouseY > 10 and mouseY < 60:
            activeTab = 2
        if mouseX > 500 and mouseX < 625 and mouseY > 10 and mouseY < 60:   
            activeTab = 3
        if mouseX > 650 and mouseX < 775 and mouseY > 10 and mouseY < 60: 
            activeTab = 4
        
        if activeTab == 4:
            if mouseX >198 and mouseY > 140 and mouseX <598 and mouseY < 160:
                selected_field = 1
                return selected_field
            
            if mouseX >198 and mouseY > 160 and mouseX <598 and mouseY < 180:
                selected_field = 2
                return selected_field
            
            if mouseX >198 and mouseY > 180 and mouseX <598 and mouseY < 200:
                selected_field = 3
                return selected_field
            
            if mouseX >198 and mouseY > 200 and mouseX <598 and mouseY < 220:
                selected_field = 4
                return selected_field
        else:
            selected_field = None
                            
def keyPressed():
    global spelerNamen
    global selected_field
    global activeTab
    
    if activeTab == 1:
        pass
    
    if activeTab == 4 and selected_field != None:
        # SHIFT keyCode = 16;
        # keyCode 17 = CONTROL, 18 = ALT pressed
        # keyCode 9 = TAB
        if key == TAB:
            if selected_field > 3:
                selected_field = 1
            else:
                selected_field = selected_field +1
        elif key==BACKSPACE:
            if len(spelerNamen["speler"+str(selected_field)]) > 0:
                spelerNamen["speler"+str(selected_field)] = spelerNamen["speler"+str(selected_field)][:len(spelerNamen["speler"+str(selected_field)])-1]
        elif key==ENTER or key==RETURN:
            # Enter new line, not used in this program.
            # spelerNamen["speler"+str(selected_field)] = spelerNamen["speler"+str(selected_field)] + "\n"
            selected_field = None
        elif (key >= 'A' and key <='Z') or (key >='a' and key <= 'z') or keyCode == 32 or key == SHIFT:
            if len(spelerNamen["speler"+str(selected_field)]) < 44:
                spelerNamen["speler"+str(selected_field)] = spelerNamen["speler"+str(selected_field)] + str(key)
        
                                    
def draw():    
    draw_bg(bg_img, screen_xSize, screen_ySize)
    menuButton()
    active(activeTab)
    menuText()
    
    if activeTab == 0:
        OverzichtGegevens()
    elif activeTab == 1:
        Duel()
    elif activeTab == 2:
        Rad1()
    elif activeTab == 3:
        # Kaartregels()
        pass
    elif activeTab == 4:
        Names()
