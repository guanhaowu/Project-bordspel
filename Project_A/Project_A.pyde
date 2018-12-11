tabs = [0, 1, 2, 3, 4]
names = ['Spelergegevens', 'Duelleren', 'Rad', 'Kaartregels', 'name5']
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


    
        
        
    
    
def draw():
    pass
        
# def mouseClicked():
#     global click
#     if mouseButton == LEFT:
