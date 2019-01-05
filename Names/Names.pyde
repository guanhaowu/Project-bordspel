spelerNamen = {"speler1":"", "speler2":"", "speler3":"", "speler4":""}
selected_field = None
blinkTime = millis()
blinkOn = True
blinkLine = ""

def setup():
    size(800,700)

def fonts(font_type,font_size, state):
    return textFont(createFont(font_type,font_size, state))

def field_colors(field):
    if field == 1: return fill(255,0,0)
    if field == 2: return fill(0,255,0)
    if field == 3: return fill(50,70,255)
    if field == 4: return fill(255,255,0)   

def keyPressed():
    global spelerNamen
    global selected_field
    
    # SHIFT keyCode = 16;
    # keyCode 17 = CONTROL, 18 = ALT pressed
    # keyCode 9 = TAB
    if selected_field != None:
        if key == TAB:
            if selected_field >= len(spelerNamen):
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
    
def mousePressed():
    global selected_field
    if mouseButton == LEFT:
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
            
def draw():
    global selected_field
    global spelerNamen
    global blinkTime, blinkOn, blinkLine
    background(255,255,255)
    
    # Table name
    textAlign(CENTER)
    stroke(0,0,0)
    fill(0,0,0)
    rect(90,120,508,20)
    fill(255,255,255)
    fonts("Arial Bold", 20, True)
    text("Vul uw naam hier onder in:", 200, 120, 398,25)
    noFill()
    noStroke()
    
    fonts("Arial", 16, True)
    
    #draw columns
    for x in range(len(spelerNamen)):
        stroke(0,0,0)
        field_colors(x+1)
        rect(90, 140+(x*20), 108, 20)  #column 1
        
        fill(0,0,0)# Text color
        textAlign(LEFT) # text alignment
        text("speler" + str(x+1), 100, 155+(x*20)) #player1-4 column 1
        noFill()
        if (x+1) == selected_field:
            fill(255,255,160)
            rect(198, 140+(x*20), 400, 20) #column 2
            fill(0,0,0)
            text(str(spelerNamen["speler"+str(x+1)])+blinkLine, 200, 155+(x*20)) # display text in the input field box
        else:
            fill(255,255,255)
            rect(198, 140+(x*20), 400, 20) #column 2
            fill(0,0,0)
            text(str(spelerNamen["speler"+str(x+1)]), 200, 155+(x*20))
        noFill()
        noStroke()
    
    if blinkOn:
        fill(0,0,0)
        blinkLine = "|"
        noFill()
    else:
        blinkLine = ""
        
    
    if (millis() - 250 > blinkTime):
        blinkTime = millis()
        blinkOn = not blinkOn
