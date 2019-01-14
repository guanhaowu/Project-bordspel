from random import randint
import init_settings as s
import sub_Lib as lib

def setup():
    global radImg, textsize1,textsize2, screen_xSize, screen_ySize
    screen_xSize, screen_ySize = s.getScreenSize()
    textsize1,textsize2 = s.getTextSize(1), s.getTextSize(2)
    
    radImg = []
    try:
        radImg.append(loadImage("rad_default.jpg"))
        # Rad photo's save to rad list.
        for i in range(1, 3):
            radImg.append(loadImage("rad"+str(i)+".jpg"))
    except ImgLoadError:
        print('Unable to load image. Check sub_Rad.py .Function: setup().')
        
    
def ShowRad(num):
    lib.button(screen_xSize*0.125, screen_ySize*0.72, 200, textsize1*1.5, 10,255,255,255)
    textAlign(CENTER, CENTER)
    lib.fonts('Ariel',textsize1, True)
    fill(0,0,0)
    text("Rol het rad!", screen_xSize*0.125, screen_ySize*0.72, 200, textsize1*1.5) 
    noFill()
    image(radImg[num], screen_xSize*0.05, screen_ySize*0.2)
        
def SpinRad():
    radNumber = randint(1,2)
    return radNumber
