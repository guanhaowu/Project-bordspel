name = {0:"", 1:"", 2:"", 3:""}
Text = {"player1":"Fill your name","player2":"Fill your name","player3":"Fill your name","player4":"Fill your name"}
selected_field = None
def setup():
    global f
    global name
    global Text
    size(800,700)
    f = createFont("Arial",16, True)
    for x in range(len(name)):
        name[x]="Speler "+str(x) + ": \n"
    
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
    global name
    background(255,255,255)
    
    stroke(175)
    
    textFont(f)
    fill(0,0,0)
    
    textAlign(LEFT)
    for x in range(len(name)):
        text(str(name[x]), 100, 60+(x*20))
        text(str(Text["player"+str(x+1)]), 200, 60+(x*20))
