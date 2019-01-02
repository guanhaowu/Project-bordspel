spelerNamen = {"speler1":"", "speler2":"", "speler3":"", "speler4":""}
selected_field = None
font_size = 18

def setup():
    global selected_field
    size(800,700)

def fonts(font_size):
    return textFont(createFont("Arial",font_size, True))

def field_colors(field):
    if field == 1: return fill(255,0,0)
    if field == 2: return fill(0,255,0)
    if field == 3: return fill(50,70,255)
    if field == 4: return fill(255,255,0)   

def keyPressed():
    global spelerNamen
    global selected_field
    
    # shift keyCode = 16 pressed; 
    if key==65535 and keyCode == 16:
        pass
    # keyCode 17 = CTRL, 18 = ALT pressed
    elif key == 65535:
        if (keyCode == 17 or keyCode == 18):
            pass
    # keyCode 9 = TAB
    elif keyCode==9:
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
        pass
    else:
        if len(spelerNamen["speler"+str(selected_field)]) < 44:
                spelerNamen["speler"+str(selected_field)] = spelerNamen["speler"+str(selected_field)] + str(key)
    
def mousePressed():
    global selected_field
    if mouseButton == LEFT:
        if mouseX >198 and mouseY > 140 and mouseX <598 and mouseY < 160:
            selected_field = 1
            
        if mouseX >198 and mouseY > 160 and mouseX <598 and mouseY < 180:
            selected_field = 2
            
        if mouseX >198 and mouseY > 180 and mouseX <598 and mouseY < 200:
            selected_field = 3
            
        if mouseX >198 and mouseY > 200 and mouseX <598 and mouseY < 220:
            selected_field = 4
            
def draw():
    global selected_field
    global spelerNamen
    background(255,255,255)
    
    textAlign(CENTER)
    stroke(0,0,0)
    fill(0,0,0)
    rect(90,120,508,20)
    fill(255,255,255)
    fonts(20)
    text("Vul uw naam hier onder in:", 200, 120, 398,25)
    noFill()
    noStroke()
    
    fonts(18)
    for x in range(len(spelerNamen)):
        stroke(0,0,0)
        field_colors(x+1)
        rect(90, 140+(x*20), 108, 20)  #column 1
        noFill()
        rect(198, 140+(x*20), 400, 20) #column 2
        noStroke()

    for x in range(len(spelerNamen)):
        fill(0,0,0)
        textAlign(LEFT)
        text("speler" + str(x), 100, 155+(x*20))
        text(str(spelerNamen["speler"+str(x+1)]), 200, 155+(x*20))
        noFill()
