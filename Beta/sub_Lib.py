def fonts(font_type,font_size, state):
    return textFont(createFont(font_type,font_size, state))

def field_colors(field):
    if field == 1: return fill(255,0,0)
    if field == 2: return fill(0,255,0)
    if field == 3: return fill(50,70,255)
    if field == 4: return fill(255,255,0)
    
def button(x1,y1,x2,y2,radius = 0, R=0,G=0,B=0, A=255):
    fill(R,G,B,A)
    rect(x1,y1,x2,y2,radius)
    noFill()

def getCoord():
    if mouseButton == LEFT:
        stroke(155)
        fill (0)
        ellipse(mouseX, mouseY,5,5)
        print(str(mouseX)+":"+str(mouseY))
        noFill()  
            
def getMouseClickLoc(status):
    ## mouse position debugger
    if status == True:
        getCoord()
            
