kaart = []
def kaart_uitleggen():
    fill(140,0,0)
    #textSize(13.5)
    #loadFont("TimesNewRomanPSMT-48.vlw")
    # global Font
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
def setup():
    global kaart
    size(800,800)
    for i in range (1,14):
        kaart.append(loadImage(str(i)+".jpg"))
    
    
def draw():
        
    background(loadImage("backgroundd.jpg"))
    j = 0
    for heigh in range(4):
            for wed in range(5):
                if j < 13:
                    image(kaart[j],wed*150,100+(heigh*200))
                    j+=1
    kaart_uitleggen()
    
