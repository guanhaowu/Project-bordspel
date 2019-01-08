from random import randint
number = 0
numberV= 0
newRes= 0
newResV= 0
c=0
d=0
tabs= [0,1]
tabstwee=[0,1]
choices= ['3 dobbelstenen','4 dobbelstenen']
dice = []
diceRes= []
diceResV=[]
diceCount= 5
diceCountV= 4
activeTab = 'Dice'
def setup():
    global dice
    size(800,800)
    background(loadImage('background.png'))
    dice.append(loadImage( "wit.jpg"))
    fill(255)
    textSize(30)
    rect(40,200,600,50)
    fill(50,50,50)
    text('Aanvaller',40,200,150,50)
    textAlign(CENTER)
    fill(255,255,255)
    rect(40,500,600,50)
    fill(50,50,50)
    text('Verdediger',40,500,200,50)
    textAlign(CENTER)
    image(dice[0], 20, 300)
    image(dice[0],20,600)
    for i in range(1,7):
       dice.append(loadImage(str(i)+".png"))
    # noLoop()


    

def menu():
    global tabs
    global tabstwee
    for tab in tabs:
        fill(150)
        stroke(150)
        rect(300+tabs[tab]*150, 60,130, 50, 150)
        noFill()
    for tab_ in tabstwee:
        fill(150)
        stroke(150)
        rect(375+tabstwee[tab_]*275, 120,130,50 , 150)
        fill(252,252,252)
        textSize(12)
        text('Rol de dobbelstenen',377,140,130,50)
        noFill()
        textSize(13)
        text('Reset',650,140,130,50)
        textSize(12)
        fill(255,0,0)
        rect(60,60,200,100,150)
        fill(255,255,255)
        text('Kies het aantal dobbelstenen rol daarna de dobbelstenen.',80,75,175,50)
        
        
           
    
def menutext():
    global choices
    for x in range(len(choices)):   
        fill(252,252,252)
        Font = createFont ("Arial Bold Italic", 13)
        textFont(Font)
        textAlign(CENTER)
        text(choices[x], 300+(x*150), 75, 130, 50)
        noFill()
    
    
    
def draw_buttons(x,y,width,height):
    rect(x,y,width,height)

# R,G,B zijn de kleuren van 0 t/m 255
# word is de tekst
#fsize is font size(lettertype grootte)
#align is positionering van de tekst in de textbox, values zijn LEFT , CENTER, RIGHT(er kunnen twee waardes ingevoerd worden met een komma er tussen. Eerste waarden is horizontaal en tweede waarde is verticaal)
# x, y is de positie waar de textbox begint
#width is de breedt vanaf de x positie naar de ingevoerde waarde
#height is de lengte van de x positie naar de ingevoerde waarde


def draw_textbox(word, R, G, B, fsize, align, x, y, width, height):
    textAlign(*align)
    textSize(fsize)
    fill(R,G,B)   
    text(word,x,y, width, height)
    

def mousePressed():
    if mouseButton == LEFT:
        if((mouseX < 435) and (mouseX > 100) and (mouseY < 120 ) and (mouseY > 40)):
            global diceCount
            diceCount = 4
            print('Aantal dobbelstenen gebruikt aanvaller: 3')
            
        if((mouseX < 550) and (mouseX > 460) and (mouseY < 120 ) and (mouseY > 50)):
            global diceCount
            diceCount= 5
            print('Aantal dobbelstenen gebruikt aanvaller: 4')
            
        if((mouseX < 500) and (mouseX > 385) and (mouseY < 160) and (mouseY > 120)):
            reset()
            roll_dice()
            roll_diceV()
            win()
        if((mouseX < 750) and (mouseX > 650) and (mouseY < 160) and (mouseY > 120)):
            reset()
        
                      
def roll_dice():
    global diceCount
    global diceRes
    global number
    global x
    x=1
    diceRes = []
    while x < diceCount:
        number = randint(1,6)
        diceRes.append(number)
        x+=1
         # print(number)
        
def roll_diceV():
    global diceCountV
    global diceResV
    global number
    global y
    x=1
    diceResV = []
    while x < diceCountV:
        number = randint(1,6)
        diceResV.append(number)
        x+=1
        #print(number)

def reset():
    global diceRes
    global diceResV
    diceRes= []
    diceResV=[]
    return setup()
    
def win():
    global diceRes
    global diceResV
    c = sum(diceRes)
    d = sum(diceResV)
    
    fill(255,0,0)
    textSize(15)
    print('Aantal ogen aanvaller:',c)
    print('Aantal ogen verdediger:',d)
    if c >= 3 and d >= 3:
        if  c > d:
            text('Aanvaller wint!', 40,215,700,50) # display text in the input field box
        elif c < d:
            text('Verdediger wint!', 40,515,700,50) # display text in the input field box
        elif c == d:
            text('Gelijkspel, gooi nog een keer!', 40,515,700,50) # display text in the input field box
    noFill()

def layout():
    global activeTab
    if activeTab == 'Dice':
        draw_textbox("Rol de dobbelstenen", 0, 0, 0, 28, (600, CENTER), 60, 60, 200, 40)
    
            
def draw():
    global diceRes
    global diceResV
    global diceCount
    global diceCountV
    global activeTab
    x=0
    y=0     
    for a in diceRes:
        if a != 0:
            image(dice[a],20+(x*210),300)
            x+=1
    for a in diceResV:
        if a != 0:
            image(dice[a],20+(y*210),600)
            y+=1
    menu()
    menutext()




    

 
    
