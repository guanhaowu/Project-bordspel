Text = {"player1":"Fill your name", "player2":"Fill your name", "player3":"Fill your name", "player4":"Fill your name"}
nameKey = Text.keys()
selected_field = None
def setup():
    global f
    size(800,700)
    f = createFont("Arial",16, True)

def field_colors(field):
    if field == 1: return fill(255,0,0)
    if field == 2: return fill(0,255,0)
    if field == 3: return fill(50,70,255)
    if field == 4: return fill(255,255,0)   
        
def keyPressed():
    global Text
    global selected_field
            
    if(key==BACKSPACE):
        if len(Text[selected_field]) > 0:
            Text[selected_field] = Text[selected_field][:len(Text)-1]
    # keyCode 17 = CTRL, 18 = ALT, 9 = TAB
    elif(keyCode==17 or keyCode==18 or keyCode==9):
         print(key)
         print(chr(keyCode))
    elif(key==ENTER or key==RETURN):
        Text[selected_field] = Text[selected_field] + "\n"
    else:
        Text[selected_field] = Text[selected_field] + key
   
def mousePressed():
    global selected_field
    if mouseButton == LEFT:
        if mouseX >200 and mouseY > 50 and mouseX <400 and mouseY < 60:
            selected_field = "player1"
            if(key):
                Text["player1"] = ""
            else:
                Text["player1"]
        if mouseX >200 and mouseY > 70 and mouseX <400 and mouseY < 80:
            selected_field = "player2"
            if(key):
                Text["player2"] = ""
            else:
                Text["player2"]
        if mouseX >200 and mouseY > 90 and mouseX <400 and mouseY < 100:
            selected_field = "player3"
            if(key):
                Text["player3"] = ""
            else:
                Text["player3"]
        if mouseX >200 and mouseY > 110 and mouseX <400 and mouseY < 120:
            selected_field = "player4"
            if(key):
                Text["player4"] = ""
            else:
                Text["player4"]


         
            
def draw():
    global selected_field
    global f
    global Text
    global nameKey
    background(255,255,255)
    
    stroke(175)
    
    textFont(f)
    textAlign(LEFT)

    for x in range(len(Text)):
        field_colors(x+1)
        rect(90, 45+(x*20), 108, 20)
        rect(198, 45+(x*20), 200, 20)
        noFill()

    for x in range(len(nameKey)):
        fill(0,0,0)
        text(str(nameKey[x]), 100, 60+(x*20))
        text(str(Text["player"+str(x+1)]), 200, 60+(x*20))
        noFill()
        
