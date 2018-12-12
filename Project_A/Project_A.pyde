tabs = [0, 1, 2, 3, 4]
names = ['Spelergegevens', 'Duel', 'Rad', 'Kaartregels', 'Rad']
click = 0
def setup():
    size(800, 800)
    background(0)
    noStroke()
    fill(102)
    global names
    global tabs
    for tab in tabs:
        fill(133, 133, 133)
        stroke(150)
        rect(50+tabs[tab]*150, 10, 100, 50)
    for x in range(len(names)):   
        fill(0)
        text(names[x], 50+(x*150), 30, 100, 50)
        textAlign(CENTER)

def mousePressed():
    global tabs
    if mouseButton == LEFT:
        if((mouseX > 50)) and (mouseX < 150)) and (mouseY > 10) and (mouseY < 60))): 
            fill(180)
            rect(0,100,800,800)
        if((mouseX > 200)) and (mouseX < 300)) and (mouseY > 10) and (mouseY < 60))):
            fill(180)
            rect(0,100,800,800)
        if((mouseX > 350)) and (mouseX < 450)) and (mouseY > 10) and (mouseY < 60))):
            fill(180)
            rect(0,100,800,800)
        if((mouseX > 500)) and (mouseX < 600)) and (mouseY > 10) and (mouseY < 60))):
            fill(180)
            rect(0,100,800,800)
        if((mouseX > 650)) and (mouseX < 750)) and (mouseY > 10) and (mouseY < 60))):
            fill(180)
            rect(0,100,800,800)



        
        
    
    
def draw():
    mousePressed()
