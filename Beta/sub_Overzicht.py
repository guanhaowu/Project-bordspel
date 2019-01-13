import init_settings as s
import sub_Lib as lib


screen_xSize, screen_ySize = s.getScreenSize()
spelerNamen = s.OverzichtData('name')
player1, player2, player3, player4 = s.OverzichtData('data')
textsize0, textsize1, textsize2, textsize3 = s.getTextSize(0), s.getTextSize(1), s.getTextSize(2), s.getTextSize(3)
col, row = s.OvTable()
OGfieldH, OGfieldW = s.getInputField('overzicht','height'), s.getInputField('overzicht','width')


def setup():
    global plus, minus
    global resetBtnStartX, resetBtnEndX, resetBtnStartY, resetBtnEndY, resetReeksBtnStartX, resetReeksBtnEndX
    
    try:
        plus = loadImage("plus.jpg")
        minus = loadImage("min.jpg")
    except ImgLoadError:
        print('Unable to load image. Check sub_Overzicht.py .Function: setup().')

    #Reset alles BTN setting
    resetBtnStartX = screen_xSize*0.08
    resetBtnEndX = 200 #button width
    resetBtnStartY = screen_ySize*0.4 #button height from top
    resetBtnEndY = 35 #height from resetBtnStartY
    
    #Reset Reeks BTN setting
    resetReeksBtnStartX = screen_xSize*0.7
    resetReeksBtnEndX = 150 #button width

def OverzichtGegevens(spelerNamen):
    #Table layout of columns and rows 
    stroke(0,0,0)
    strokeWeight(1)
    for y in range(row+2):
        for x in range(col):
            if y > 1:
                lib.button(((screen_xSize/100*5)+200)+(x*OGfieldW), (120)+(y*textsize1*1.5), OGfieldW,textsize1*1.5,0,255,255,255)
                line(((screen_xSize/100*5)+200)+(x*OGfieldW),(120)+(y*textsize1*1.5), ((screen_xSize/100*5)+200)+(x*OGfieldW),(120+(textsize1*1.5))+(y*textsize1*1.5))
            else:
                lib.button(((screen_xSize/100*5)+200)+(x*OGfieldW), (120)+(y*textsize1*1.5), OGfieldW,textsize1*1.5,0,0,0,0)
    
    '''Color column RGBY horizontal.'''
    for x in range(len(spelerNamen)):
        lib.field_colors(x+1)
        rect(((screen_xSize/100*5)+200)+(x*OGfieldW), 120+(textsize1*2), OGfieldW,textsize1)
    noFill()
    noStroke()
    
    '''Color column RGBY vertical.'''
    #Names column background
    fill(0,0,0)
    rect(screen_xSize/100*5, 120, 200,textsize1*1.5)
    noFill()
    for x in range(len(spelerNamen)+2):
        if x > 1:
            lib.field_colors(x-1)
            rect(screen_xSize*0.05, (120)+(x*(textsize1*1.5)), 200, textsize1*1.5)  #column 1
            noFill()
        else:
            noStroke()
            lib.button((screen_xSize*0.05), (120)+(x*(textsize1*1.5)),200,(textsize1*1.5), 0,0,0,0)
    
    lib.fonts("Arial", textsize1, True)
    
    #Table name text
    textAlign(CENTER,CENTER)
    lib.fonts("Arial Bold", textsize0, True)
    fill(255,255,255)
    text("Gegevens overzicht van het spel", (screen_xSize*0.05), 120, (col+2)*OGfieldW ,textsize0*1.5)
    noFill()
    
    

            
    # #Greybox
    # for x in range(4):
    #     fill(155,155,155)
    #     stroke(0)
    #     rect(248+(x*100), 180+(x*20), 100, 20)
    #     noStroke()
    #     noFill()
    

    #Top row names
    # lib.fonts("Arial Bold", textsize2, True)
    # fill(255,255,255)
    # textAlign(CENTER)
    # text('Verslagen kleur', screen_xSize/100*5, 120+(textsize1*1.5), 200*5, textsize2*1.5)
    
    # fill(255,0,0)
    # text('Gevangenis', 650, 160, 100, 180)
    # text('Boer', 750, 160, 100, 180)
    # text('Reeks', 850, 160, 100, 180)
    # noFill()
    # noStroke()
    
    lib.fonts("Ariel", textsize1, True)
    # #Names text in column 1   
    for x in range(len(spelerNamen)):
        fill(0,0,0)
        textAlign(LEFT,CENTER)
        if len(spelerNamen["speler"+str(x+1)]) > 0:
            text(str(spelerNamen["speler"+str(x+1)]), (screen_xSize/100*5)+5, (120+(textsize1*1.5))+((x+1)*(textsize1*1.5)),200,(textsize1*1.5))
        else:
            text("Speler"+str(x+1), (screen_xSize/100*5)+5, (120+(textsize1*1.5))+((x+1)*(textsize1*1.5)), 200, (textsize1*1.5))
        noFill()
        
    # for x in range(3):#tabel2
    #     stroke(255,255,255)
    #     line(648+(x*100), 160, 648+(x*100), 180)
    #     stroke(0,0,0)
    #     line(648+(x*100), 180, 648+(x*100), 260)
    #     noStroke()
    
    
    # fill(0,0,0)    
    #kolom 1
    # image(minus,250,201,18,18)
    # image(minus,250,222,18,18)
    # image(minus,250,242,18,18)
    # image(minus,250,242,18,18)
    
    # image(plus,330,201,18,18)
    # image(plus,330,222,18,18)
    # image(plus,330,242,18,18)
    
    # text(str(player2['GroenvRood']),295,201,313,219)
    # text(str(player3['BlauwvRood']),295,222,313,219)
    # text(str(player4['GeelvRood']) ,295,242,313,219)
    
    # #kolom 2
    # image(minus,350,181,18,18)
    # image(minus,350,222,18,18)    
    # image(minus,350,242,18,18)
    
    # image(plus,430,181,18,18)
    # image(plus,430,222,18,18)
    # image(plus,430,242,18,18)
    
    # text(str(Rood_tegen_Groen),395,181,413,219)
    # text(str(Blauw_tegen_Groen),395,222,413,219)
    # text(str(Geel_tegen_Groen),395,242,413,219)
    
    # #kolom 3
    # image(minus,450,181,18,18)
    # image(minus,450,202,18,18)
    # image(minus,450,242,18,18)
    
    # image(plus,530,181,18,18)
    # image(plus,530,202,18,18)
    # image(plus,530,242,18,18)
    
    # text(str(Rood_tegen_Blauw),495,181,413,219)
    # text(str(Groen_tegen_Blauw),495,202,413,219)
    # text(str(Geel_tegen_Blauw),495,242,413,219)
    
    # #kolom 4
    # image(minus,550,181,18,18)
    # image(minus,550,202,18,18)
    # image(minus,550,222,18,18)
    
    # image(plus,630,181,18,18)
    # image(plus,630,202,18,18)
    # image(plus,630,222,18,18)
    
    # text(str(Rood_tegen_Geel),595,181,413,219)
    # text(str(Groen_tegen_Geel),595,202,413,219)
    # text(str(Blauw_tegen_Geel),595,222,413,219)
    
    # #kolom 5
    # image(minus,650,181,18,18)
    # image(minus,650,202,18,18)
    # image(minus,650,222,18,18)
    # image(minus,650,242,18,18)
    
    # image(plus,730,181,18,18)
    # image(plus,730,202,18,18)
    # image(plus,730,222,18,18)
    # image(plus,730,242,18,18)
    
    # text(str(Rood_Gevangenis),695,181,413,219)
    # text(str(Groen_Gevangenis),695,202,413,219)
    # text(str(Blauw_Gevangenis),695,222,413,219)
    # text(str(Geel_Gevangenis),695,242,413,219)
    
    # #kolom 6
    # image(minus,750,181,18,18)
    # image(minus,750,202,18,18)
    # image(minus,750,222,18,18)
    # image(minus,750,242,18,18)
    
    # image(plus,830,181,18,18)
    # image(plus,830,202,18,18)
    # image(plus,830,222,18,18)
    # image(plus,830,242,18,18)
    
    # text(str(Rood_Boer),795,181,413,219)
    # text(str(Groen_Boer),795,202,413,219)
    # text(str(Blauw_Boer),795,222,413,219)
    # text(str(Geel_Boer),795,242,413,219)
    
    # #kolom 7
    # image(minus,850,181,18,18)
    # image(minus,850,202,18,18)
    # image(minus,850,222,18,18)
    # image(minus,850,242,18,18)
    
    # image(plus,930,181,18,18)
    # image(plus,930,202,18,18)
    # image(plus,930,222,18,18)
    # image(plus,930,242,18,18)
    
    # text(str(Rood_Reeks),895,181,413,219)
    # text(str(Groen_Reeks),895,202,413,219)
    # text(str(Blauw_Reeks),895,222,413,219)
    # text(str(Geel_Reeks),895,242,413,219)    
    # noFill()
    
    # #Reset alles button
    # lib.button(resetBtnStartX, resetBtnStartY, resetBtnEndX, resetBtnEndY, 15,200,200,200)
    # fill(0,0,0)
    # textAlign(CENTER,CENTER)
    # text('Reset alles',resetBtnStartX, resetBtnStartY, resetBtnEndX, resetBtnEndY)
    # noFill()
    
    # #Reset reeks button
    # lib.button(resetReeksBtnStartX, screen_ySize/100*35, resetReeksBtnEndX, 35, 15,200,200,200)
    # textAlign(CENTER,CENTER)
    # fill(0,0,0)
    # text('Reset Reeks',resetReeksBtnStartX, screen_ySize/100*35, resetReeksBtnEndX, 35)
    # noFill()
    
    ## Instruction, height, box radius.
    firstLine = 400
    endLine = 400
    radius = 25
    
    # ## Instruction box bg color
    # lib.button(screen_xSize/100*5, 390, screen_xSize/100*90, endLine, radius, 200,200,200,150)
    # ## Instruction text
    # fill(100,0,100)
    # textAlign(LEFT)
    # lib.fonts("Ariel", textsize2, False)
    # text('Instructies:', screen_xSize/100*5+10, firstLine, screen_xSize/100*90,textsize2*2)
    # lib.fonts("Ariel", textsize3, False)
    # margin = textsize3*1.5
    # text("Vul eerst uw naam in bij de tab \"Namen\".", screen_xSize/100*5+10, firstLine+(textsize2*2), screen_xSize/100*90,textsize3*1.5)
    # text("Gebruik dit overzicht om alles bij te houden gedurende spelronde.", screen_xSize/100*5+10, firstLine+(margin*2), screen_xSize/100*80,textsize3*1.5)
    # text("Wanneer een winnaar bekend is van het spel, druk op de \"RESET\" knop om alles terug te zetten naar 0.", screen_xSize/100*5+10, firstLine+(margin*3), screen_xSize/100*90,textsize3*1.5)
    # text('Gebruik de tab \"Dueleren\" wanneer je iemand aanvalt.', screen_xSize/100*5+10, firstLine+(margin*4), screen_xSize/100*90,textsize1*1.5)
    # text('Gebruik de tab \"Shortcut\" wanneer je op het kruisingspunt zit voor de shortcut.', screen_xSize/100*5+10, firstLine+(margin*5), screen_xSize/100*90,textsize3*1.5)
    # text('Gebruik de tab \"Kaartregels\" als je de regels wilt weten van elke kaart.', screen_xSize/100*5+10, firstLine+(margin*6), screen_xSize/100*90,textsize3*1.5)
    # noFill()
    
def Reset(What2Reset):
    global Rood_tegen_Groen,Rood_tegen_Blauw, Rood_tegen_Geel
    global Groen_tegen_Rood, Groen_tegen_Blauw,Groen_tegen_Geel
    global Blauw_tegen_Rood,Blauw_tegen_Groen,Blauw_tegen_Geel
    global Geel_tegen_Rood,Geel_tegen_Groen,Geel_tegen_Blauw
    global Rood_Gevangenis,Groen_Gevangenis,Blauw_Gevangenis,Geel_Gevangenis
    global Rood_Boer,Groen_Boer,Blauw_Boer,Geel_Boer
    global Rood_Reeks, Groen_Reeks, Blauw_Reeks,Geel_Reeks
    if What2Reset == 'OverzichtGegevens':
        Rood_tegen_Groen = 0
        Rood_tegen_Blauw = 0
        Rood_tegen_Geel = 0
        Groen_tegen_Rood = 0
        Groen_tegen_Blauw = 0
        Groen_tegen_Geel = 0
        Blauw_tegen_Rood = 0
        Blauw_tegen_Groen = 0
        Blauw_tegen_Geel = 0
        Geel_tegen_Rood = 0
        Geel_tegen_Groen = 0
        Geel_tegen_Blauw = 0
        Rood_Gevangenis = 0
        Groen_Gevangenis = 0
        Blauw_Gevangenis = 0
        Geel_Gevangenis = 0
        Rood_Boer = 0
        Groen_Boer = 0
        Blauw_Boer = 0
        Geel_Boer = 0
        Rood_Reeks = 0
        Groen_Reeks = 0
        Blauw_Reeks = 0
        Geel_Reeks = 0
        Reset('ResetReeks')
        
    if What2Reset == 'ResetReeks':
        Rood_Reeks = 0
        Groen_Reeks = 0
        Blauw_Reeks = 0
        Geel_Reeks = 0
