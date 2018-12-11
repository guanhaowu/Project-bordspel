name = {}
Text = ""
backspaceCounter = 0
def setup():
    global f
    global Text
    global name
    size(800,700)
    f = createFont("Arial",16, True)
    names = {1:"", 2:"", 3:"", 4:""}
    for x in range(len(names)):
        name[x]="Speler "+str(x+1) + ": " + Text + "\n"

def keyPressed():
    global Text
    global backspaceCounter
    print(len(Text))
    
    if(key==BACKSPACE):
        if len(Text) > 0:
            backspaceCounter += 1
            Text = Text[:len(Text)-1]
    # keyCode 17 = CTRL, 18 = ALT, 9 = TAB
    if(keyCode==17 or keyCode==18 or keyCode==9):
         print(key)
         print(chr(keyCode))
    if(key==ENTER or key==RETURN):
        Text = Text + "\n"
    else:
        Text = Text + key
        print(Text)    
            
def draw():
    global f
    global Text
    global name
    global backspaceCounter
    background(255,255,255)
    
    stroke(175)
    
    textFont(f)
    fill(0,0,0)
    
    textAlign(CENTER)
    for x in range(len(name)):
        text(str(name[x]), 100 , 60+(x*20))
        text(str(Text),200, 60+(x*20))
    if len(Text) > 0:
        if(backspaceCounter > 0):   
            lastLetter = len(Text)
            Text = Text[:lastLetter - 1]
            backspaceCounter =0
        
  

    
    
    
