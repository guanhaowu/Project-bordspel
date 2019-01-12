import init_settings as s
import sub_Lib as lib


def setup():
    global screen_xSize, screen_ySize, kaart
    screen_xSize, screen_ySize = s.getScreenSize()
    
    # Loaded images of Kaart into kaart.
    kaart = []
    # Kaart photo saved to kaart list
    for i in range (1,14):
        kaart.append(loadImage(str(i)+".jpg"))    

def Kaartregels():
    card_width =  150 #150 px width card
    card_height = 250 #250 px height card
    cardText_width =  133 #5 px margin from x start x position ,card 133px
    cardText_height = 195 #40 px margin from y position,card 195px
    left_margin= screen_xSize/100*25 #margin from left 25%
    card = 0
    for yRow in range(4):
        for xRow in range(5):
            if card < 13:
                # left_margin/2 = 150px
                image(kaart[card],left_margin/2 + (xRow*card_width), 100 +(card_height*yRow))
                card+=1

    fill(140,0,0)
    lib.fonts("Arial Italic", 15, True)
    textAlign (LEFT)
    # text box with auto wrap (x,y, from x, from y)
    Aas = "Een pion uit het startveld op eigen startpositie (vlag icoontje) zetten of een pion 1 plaats vooruit zetten." 
    text(Aas, left_margin/2 + 5 + (cardText_width*0), 100 + (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Twee = "Bij deze kaart moet je je pion twee stappen vooruit zetten."
    text(Twee, left_margin/2 + 22 + (cardText_width*1), 100 + (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Drie = "Bij deze kaart moet je je pion drie stappen vooruit zetten."
    text(Drie, left_margin/2 + 22 + (cardText_width*2+20), 100 + (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Vier = "Bij deze kaart moet je je pion vier stappen achteruit zetten." 
    text(Vier,left_margin/2 +22+ (cardText_width*3+35),100 + ( cardText_height*0)+40, cardText_width-11,cardText_height-40)
    Vijf = "Bij deze kaart moet je je pion vijf stappen vooruit zetten."
    text(Vijf,left_margin/2 +22+ (cardText_width*4+50),100 + (cardText_height*0)+40, cardText_width-11,cardText_height-40)
    Zes = "Bij deze kaart moet je je pion zes stappen vooruit zetten."
    text(Zes, left_margin/2 + 5 + (cardText_width*0), 350+ (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Zeven = "Bij deze kaart kan je je pion zeven stappen vooruit zetten of splitsen over twee pionnen."
    text(Zeven, left_margin/2 + 22 + (cardText_width*1), 350+ (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Acht = "Bij deze kaart moet je je pion acht stappen vooruit zetten."
    text(Acht, left_margin/2 + 22 + (cardText_width*2+20),350+ (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Negen = "Bij deze kaart moet je je pion negen stappen vooruit zetten."
    text(Negen,left_margin/2 +22+ (cardText_width*3+35),350 + ( cardText_height*0)+40, cardText_width-11,cardText_height-40)
    Tien = "Bij deze kaart moet je je pion tien stappen vooruit zetten."
    text(Tien,left_margin/2 +22+ (cardText_width*4+50),350+ (cardText_height*0)+40, cardText_width-11,cardText_height-40)
    Boer = "Een eigen pion met een pion van een andere speler omruilen."
    text(Boer, left_margin/2 + 5 + (cardText_width*0), 600+ (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Vrouw = "Een pion twaalf plaatsen vooruit zetten."
    text(Vrouw, left_margin/2 + 22 + (cardText_width*1), 600 + (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Heer = "Een pion uit het startveld op eigen startpositie(vlag icoontje) zetten."
    text(Heer, left_margin/2 + 22 + (cardText_width*2+20), 600 + (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    noFill()
