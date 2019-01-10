from random import randint
number = 0
rad = []
activeTab = '2'

def setup():
    global rad
    size(800,800)
    background(100,100,100)
    rad.append(loadImage("dice.jpg"))
    image(rad[0], 300, 300)
    for i in range(1, 3):
        rad.append(loadImage(str(i)+".jpg"))
    
def draw_buttons(x,y,width,height):
    rect(x,y,width,height)

def draw_textbox(word, R, G, B, fsize, align, x, y, width, height):
    textAlign(*align)
    textSize(fsize)
    fill(R,G,B)
    text(word,x,y, width, height)
    noFill()
    
# def mousePressed():
#     global RotatingTime, Rotate
#     if mouseButton == LEFT:
#         if((mouseX < 260) and (mouseX > 60) and (mouseY < 140) and (mouseY > 60)):
#             x = 0
#             RotatingTime = 10000
#             Rotate = True 
#             while Rotate:
#                 spin_rad()
#                 x +=10
#                 if (RotatingTime - x <= 0):
#                     RotatingTime = 100000
#                     Rotate = False
                               
def spin_rad():
    global number
    number = randint(1,2)


def rad_button():
    global activeTab
    if activeTab == '2':
        fill(255,255,255)
        draw_buttons(60,60,200,40)
        fill(0,0,0)
        draw_textbox("Rol het Rad!", 0, 0, 0, 28, (CENTER, CENTER), 60, 60, 200, 40)
        noFill()
            
def draw():
    global number
    global activeTab
    rad_button()
         
    if number != 0:
        image(rad[number],300,300)
    if mousePressed:
        if mouseButton == LEFT and ((mouseX < 260) and (mouseX > 60) and (mouseY < 140) and (mouseY > 60)):
                x = 0
                RotatingTime = 10000
                Rotate = True 
                while Rotate:
                    spin_rad()
                    x +=10
                    if (RotatingTime - x <= 0):
                        RotatingTime = 100000
                        Rotate = False
        
                
