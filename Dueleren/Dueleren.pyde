from random import randint
number = 0
dice = []
diceRes= []
diceCount= 5
activeTab = 'Dice'
def setup():
    global dice
    size(800,800)
    background(loadImage("background.png"))
    dice.append(loadImage("wit.jpg"))
    fill(255)
    textSize(30)
    text('Speler 1',50,200,150,50)
    textAlign(CENTER)
    image(dice[0], 20, 300)
    for i in range(1,7):
       dice.append(loadImage(str(i)+".png"))
    # noLoop()
    
    

    
    
    
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
        if((mouseX < 260) and (mouseX > 60) and (mouseY < 140) and (mouseY > 60)):
            roll_dice()
            

                      
def roll_dice():
    global diceCount
    global diceRes
    global number
    x=1
    diceRes = []
    while x < diceCount:
        number = randint(1,6)
        diceRes.append(number)
        x+=1
         # print(number)
    print(diceRes)


def layout():
    global activeTab
    if activeTab == 'Dice':
        draw_textbox("Start the Duel", 0, 0, 0, 28, (CENTER, CENTER), 60, 60, 200, 40)
            
def draw():
    global diceRes
    global diceCount
    global activeTab
    layout()
    if activeTab == "Duel":
        draw_buttons(60,60,200,40)
    x = 0         
    for a in diceRes:
        if a != 0:
            image(dice[a],20+(x*210),300)
            x+=1 

    
