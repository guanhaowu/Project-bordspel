from random import randint
number = 0
dice = []
activeTab = 'Dice'
def setup():
    global dice
    size(800,800)
    background(100,100,100)
    dice.append(loadImage("dice.jpg"))
    image(dice[0], 300, 300)
    for i in range(1,7):
        dice.append(loadImage(str(i)+".jpg"))
    # noLoop()
    
    
    
def draw_buttons(x,y,width,height):
    rect(x,y,width,height)

def draw_textbox(word, R, G, B, fsize, align, x, y, width, height):
    textAlign(*align)
    textSize(fsize)
    fill(R,G,B)
    text(word,x,y, width, height)
    noFill()
    

# def mousePressed():
#     if mouseButton == LEFT:
        # if((mouseX < 260) and (mouseX > 60) and (mouseY < 140) and (mouseY > 60)):
        #     roll_dice()
                      
def roll_dice():
    global dice
    global number
    number = randint(1,6)
    print(number)

def layout():
    global activeTab
    if activeTab == 'Dice':
        # draw_buttons(60,60,200,40)
        draw_textbox("Roll the Dice", 0, 0, 0, 28, (CENTER, CENTER), 60, 60, 200, 40)
            
def draw():
    global number
    global activeTab
    draw_buttons(60,10,200,40)
    draw_textbox("Dice", 0, 0, 0, 28, (LEFT,CENTER), 60, 40, 200, 20)
    layout()
    if activeTab == "Dice":
        draw_buttons(60,60,200,40)
            
    if((mouseX < 260) and (mouseX > 60) and (mouseY < 140) and (mouseY > 60) and mouseButton == LEFT):
        roll_dice()
         
    # if((mouseX < 260) and (mouseX > 60) and (mouseY < 90) and (mouseY > 10)):
             
    redraw()       
    if number != 0:
        image(dice[number],300,300)
               
