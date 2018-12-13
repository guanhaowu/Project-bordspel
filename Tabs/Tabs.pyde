tabs = [0, 1, 2, 3, 4]
names = ['Spelergegevens', 'Duel', 'Rad', 'Kaartregels', 'Name']
activeTab = 0
kaart = []
def active(tab):
    fill(255,255,0)
    stroke(150)
    rect(50+(tab*150), 10, 125, 50, 10)
    noFill()

def Spelergegevens():
    global activeTab
    activeTab = 0
    noLoop()
    


def Duel():
    global activeTab
    activeTab = 1
    noLoop()

    

def Rad1():
    global activeTab
    activeTab = 2
    fill(150)
    rect(200,400,300,300)
    noFill()
    noLoop()
    
def Kaartregels():
    global kaart
    global activeTab
    activeTab = 3
     
     
    j = 0
    for heigh in range(4):
        for wed in range(5):
            if j < 13:
                image(kaart[j],wed*150,100+(heigh*200))
                j+=1

    fill(140,0,0)
    Font = createFont ("Arial Bold Italic", 14)
    textFont(Font)
    textAlign (LEFT)
    Aas = text(" Een pion uit het\n startveld op eigen\n startpositie (vlag\n icoontje) zetten of\n een pion een plaats\n vooruit zetten.",0,150)
    Twee = text(" Bij deze kaart moet\n je je pion twee\n stappen vooruit\n zetten.",150,160)
    Drie = text(" Bij deze kaart moet\n je je pion drie\n stappen vooruit\n zetten.",150*2,160)
    Vier = text(" Bij deze kaart moet\n je je pion vier\n stappen achteruit\n zetten.",150*3,160)
    Vijf = text(" Bij deze kaart moet\n je je pion vijf\n stappen vooruit\n zetten.",150*4,160)
    Zes = text(" Bij deze kaart moet\n je je pion zes\n stappen vooruit\n zetten.",0,360)
    Zeven = text(" Bij deze kaart kan\n je je pion zeven\n stappen vooruit\n zetten of splietsen\n over twee pionnen.",150,360)
    Acht = text(" Bij deze kaart moet\n je je pion acht\n stappen vooruit\n zetten.",150*2,360)
    Negen = text(" Bij deze kaart moet\n je je pion negen\n stappen vooruit\n zetten.",150*3,360)
    Tien =  text(" Bij deze kaart moet\n je je pion tien\n stappen vooruit\n zetten.",150*4,360)
    Boer = text(" Een eigen pion\n met een pion van\n een andere speler\n omruilen.",0,560)
    Vrouw = text(" Een pion twaalf\n plaatsen vooruit\n zetten.",150,560)
    Heer = text(" Een pion uit het\n startveld op eigen\n startpositie(vlag\n icoontje) zetten.",150*2,560)
    noFill()
    noLoop()


def Names():
    global activeTab
    activeTab = 4
    noLoop()

    
def setup():
    global kaart
    size(800, 800)
    background(0)
    noStroke()
    fill(102)

    for i in range (1,14):
        kaart.append(loadImage(str(i)+".jpg"))    

def menu():
    global tabs
    for tab in tabs:
        fill(150)
        stroke(150)
        rect(50+tabs[tab]*150, 10, 125, 50, 10)
        noFill()
def menutext():
    global names
    for x in range(len(names)):   
        fill(252,252,252)
        Font = createFont ("Arial Bold Italic", 13)
        textFont(Font)
        textAlign(CENTER)
        text(names[x], 50+(x*150), 30, 125, 50)
        noFill()


def mousePressed():
    if mouseButton == LEFT:
        
        if mouseX > 50 and mouseX < 175 and mouseY > 10 and mouseY < 60:
            redraw()
            Spelergegevens()
        if mouseX > 200 and mouseX < 325 and mouseY > 10 and mouseY < 60:
            redraw()
            Duel()
        if mouseX > 350 and mouseX < 475 and mouseY > 10 and mouseY < 60:
            redraw()
            Rad1()
        if mouseX > 500 and mouseX < 625 and mouseY > 10 and mouseY < 60:   
            redraw()
            Kaartregels()
        if mouseX > 650 and mouseX < 775 and mouseY > 10 and mouseY < 60: 
            redraw()
            Names()
        
        

            
def draw():
    background(loadImage("backgroundd.jpg"))
    mousePressed()
    menu()
    active(activeTab)
    menutext()
