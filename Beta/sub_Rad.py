from random import randint
import init_settings as s
import sub_Lib as lib

def setup():
    global radImg, textsize1,textsize2
    
    radImg = []
    radImg.append(loadImage("rad_default.jpg"))
    # Rad photo's save to rad list.
    for i in range(1, 3):
        radImg.append(loadImage("rad"+str(i)+".jpg"))

    textsize1,textsize2 = s.getTextSize(1), s.getTextSize(2)
    
def ShowRad(num):
    lib.button(400, 250, 200, textsize1*1.5, 50,255,255,255)
    
    fill(0,0,0)
    textAlign(CENTER, CENTER)
    lib.fonts('Ariel',textsize1, True)
    text("Rol het rad!", 400, 250, 200, textsize1*1.5) 
    noFill()
    image(radImg[num], 300, 300)
        
def SpinRad():
    radNumber = randint(1,2)
    return radNumber
