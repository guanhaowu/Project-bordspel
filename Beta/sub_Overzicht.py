import init_settings as s
import sub_Lib as lib


screen_xSize, screen_ySize = s.getScreenSize()
spelerData = s.OverzichtData('data')
textsize0, textsize1, textsize2, textsize3 = s.getTextSize(0), s.getTextSize(1), s.getTextSize(2), s.getTextSize(3)
col, row = s.OvTable()
OGfieldH, OGfieldW = s.getInputField('overzicht','height'), s.getInputField('overzicht','width')


def setup():
    global plus, minus
    global resetBtnStartX, resetBtnEndX, resetBtnStartY, resetBtnEndY, resetReeksBtnStartX, resetReeksBtnEndX
    global colName
    
    try:
        plus = loadImage("plus.jpg")
        minus = loadImage("min.jpg")
    except ImgLoadError:
        print('Unable to load image. Check sub_Overzicht.py .Function: setup().')

    colName = s.OverzichtData('colName')

    #Reset alles BTN setting
    resetBtnStartX = screen_xSize*0.08
    resetBtnEndX = 200 #button width
    resetBtnStartY = screen_ySize*0.4 #button height from top
    resetBtnEndY = 35 #height from resetBtnStartY
    
    #Reset Reeks BTN setting
    resetReeksBtnStartX = screen_xSize*0.7
    resetReeksBtnEndX = 150 #button width

def OverzichtGegevens(spelerData):
    drawTable()
    drawTableText()
    drawTableData(spelerData, row)
    
    # fill(0,0,0)
            
    #kolom 1
    # image(minus,250,201,18,18)
    # image(minus,250,222,18,18)
    # image(minus,250,242,18,18)
    # image(minus,250,242,18,18)
    
    # image(plus,330,201,18,18)
    # image(plus,330,222,18,18)
    # image(plus,330,242,18,18)
    
    # #kolom 2
    # image(minus,350,181,18,18)
    # image(minus,350,222,18,18)    
    # image(minus,350,242,18,18)
    
    # image(plus,430,181,18,18)
    # image(plus,430,222,18,18)
    # image(plus,430,242,18,18)

    
    # #kolom 3
    # image(minus,450,181,18,18)
    # image(minus,450,202,18,18)
    # image(minus,450,242,18,18)
    
    # image(plus,530,181,18,18)
    # image(plus,530,202,18,18)
    # image(plus,530,242,18,18)
    
    # #kolom 4
    # image(minus,550,181,18,18)
    # image(minus,550,202,18,18)
    # image(minus,550,222,18,18)
    
    # image(plus,630,181,18,18)
    # image(plus,630,202,18,18)
    # image(plus,630,222,18,18)
    
    # #kolom 5
    # image(minus,650,181,18,18)
    # image(minus,650,202,18,18)
    # image(minus,650,222,18,18)
    # image(minus,650,242,18,18)
    
    # image(plus,730,181,18,18)
    # image(plus,730,202,18,18)
    # image(plus,730,222,18,18)
    # image(plus,730,242,18,18)
    
    # #kolom 6
    # image(minus,750,181,18,18)
    # image(minus,750,202,18,18)
    # image(minus,750,222,18,18)
    # image(minus,750,242,18,18)
    
    # image(plus,830,181,18,18)
    # image(plus,830,202,18,18)
    # image(plus,830,222,18,18)
    # image(plus,830,242,18,18)
    
    # #kolom 7
    # image(minus,850,181,18,18)
    # image(minus,850,202,18,18)
    # image(minus,850,222,18,18)
    # image(minus,850,242,18,18)
    
    # image(plus,930,181,18,18)
    # image(plus,930,202,18,18)
    # image(plus,930,222,18,18)
    # image(plus,930,242,18,18)
       
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

def drawTableInstructions():    
    ## Instruction box bg color
    lib.button(screen_xSize*0.05, 390, screen_xSize*0.9, endLine, radius, 200,200,200,150)
    ## Instruction text
    fill(100,0,100)
    textAlign(LEFT)
    lib.fonts("Ariel", textsize2, False)
    text('Instructies:', screen_xSize*0.05+10, firstLine, screen_xSize*0.9,textsize2*2)
    lib.fonts("Ariel", textsize3, False)
    margin = textsize3*1.5
    text("Vul eerst uw naam in bij de tab \"Namen\".", ((screen_xSize*0.05)+10), firstLine+(textsize2*2), (screen_xSize*0.9),textsize3*1.5)
    text("Gebruik dit overzicht om alles bij te houden gedurende spelronde.", ((screen_xSize*0.05)+10), firstLine+(margin*2), (screen_xSize*0.80),textsize3*1.5)
    text("Wanneer een winnaar bekend is van het spel, druk op de \"RESET\" knop om alles terug te zetten naar 0.", (screen_xSize*0.05)+10, firstLine+(margin*3), (screen_xSize*0.9),textsize3*1.5)
    text('Gebruik de tab \"Dueleren\" wanneer je iemand aanvalt.', (screen_xSize*0.05)+10, firstLine+(margin*4), (screen_xSize*0.9),textsize1*1.5)
    text('Gebruik de tab \"Shortcut\" wanneer je op het kruisingspunt zit voor de shortcut.', ((screen_xSize*0.05)+10), firstLine+(margin*5), (screen_xSize*0.9),textsize3*1.5)
    text('Gebruik de tab \"Kaartregels\" als je de regels wilt weten van elke kaart.', ((screen_xSize*0.05)+10), firstLine+(margin*6), (screen_xSize*0.9),textsize3*1.5)
    noFill()

### Table layout of columns and rows with colors. 
def drawTableText():
    #Table name text
    textAlign(CENTER,CENTER)
    lib.fonts("Arial Bold", textsize0, True)
    fill(255,255,255)
    text("Gegevens overzicht van het spel", (screen_xSize*0.05), 120, (col+2)*OGfieldW ,textsize0*1.5)
    noFill()
    
    # Text: Names in column 0.   
    
    for x in range(len(spelerData)):
        fill(0,0,0)
        lib.fonts("Ariel", textsize1, True)
        textAlign(LEFT,CENTER)
        try:
            if len(spelerData["speler"+str(x+1)]['name']) > 0:
                text(str(spelerData["speler"+str(x+1)]['name']), (screen_xSize*0.05)+5, (120+(textsize1*1.5))+((x+2)*(textsize1*1.5)),200,(textsize1*1.5))
            else:
                text("Speler"+str(x+1), (screen_xSize*0.05)+5, (120+(textsize1*1.5))+((x+2)*(textsize1*1.5)), 200, (textsize1*1.5))
        except IndexError:
            print("Error at Function: DrawTableText() first part")
        noFill()
        
        fill(255,0,0)
        textAlign(CENTER,CENTER)
        lib.fonts("Ariel", textsize3, True)
        if x < len(colName):
            try:
                text(colName[x], (((screen_xSize*0.05)+200)+((x+4)*OGfieldW)), (120+((textsize1)*3)), OGfieldW, textsize2*1.5)
            except IndexError:
                print("Error at Function: DrawTableText() second part")
        noFill()
    
    ### Third row, column names.
    lib.fonts("Arial Bold", textsize2, True)
    fill(255,255,255)
    textAlign(CENTER, CENTER)
    text('Verslagen kleur', (screen_xSize*0.05)+205, (120+((textsize1)*2)), (len(spelerData))*OGfieldW, textsize2*1.5)
    
### Table Data.    
def drawTableData(spelerData,Row):
    fill(255,0,0)
    textAlign(CENTER,CENTER)
    lib.fonts("Ariel", textsize3, True)
    # Left half table
    try:
        x = 1    
        text(str(spelerData["speler1"]['data'][0]), (((screen_xSize*0.05)+200)+(1*OGfieldW)), (120+(textsize1*1.5)+((2*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(spelerData["speler1"]['data'][1]), (((screen_xSize*0.05)+200)+(2*OGfieldW)), (120+(textsize1*1.5)+((2*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(spelerData["speler1"]['data'][2]), (((screen_xSize*0.05)+200)+(3*OGfieldW)), (120+(textsize1*1.5)+((2*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        x = 2
        text(str(spelerData["speler2"]['data'][0]), (((screen_xSize*0.05)+200)+(0*OGfieldW)), (120+(textsize1*1.5)+((3*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(spelerData["speler2"]['data'][1]), (((screen_xSize*0.05)+200)+(2*OGfieldW)), (120+(textsize1*1.5)+((3*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(spelerData["speler2"]['data'][2]), (((screen_xSize*0.05)+200)+(3*OGfieldW)), (120+(textsize1*1.5)+((3*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        x = 3
        text(str(spelerData["speler3"]['data'][0]), (((screen_xSize*0.05)+200)+(0*OGfieldW)), (120+(textsize1*1.5)+((4*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(spelerData["speler3"]['data'][1]), (((screen_xSize*0.05)+200)+(1*OGfieldW)), (120+(textsize1*1.5)+((4*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(spelerData["speler3"]['data'][2]), (((screen_xSize*0.05)+200)+(3*OGfieldW)), (120+(textsize1*1.5)+((4*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        x = 4
        text(str(spelerData["speler4"]['data'][0]), (((screen_xSize*0.05)+200)+(0*OGfieldW)), (120+(textsize1*1.5)+((5*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(spelerData["speler4"]['data'][1]), (((screen_xSize*0.05)+200)+(1*OGfieldW)), (120+(textsize1*1.5)+((5*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(spelerData["speler4"]['data'][2]), (((screen_xSize*0.05)+200)+(2*OGfieldW)), (120+(textsize1*1.5)+((5*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
    except IndexError:
        print("Error at Function: DrawTableText() first half table part")
    noFill()
    # Right half table
    for x in range(3):
        for y in range(Row):
            try:
                text(str(spelerData["speler"+str(y+1)]['data'][x+3]), (((screen_xSize*0.05)+200)+((x+5)*OGfieldW)), (120+(textsize1*1.5)+((y+2)*(textsize1*1.5))), OGfieldW, textsize1*1.5)
            except IndexError:
                print(x)
                print("Error at Function: DrawTableText() second half table part")
    noFill()
                    
### Table layout of columns and rows with colors. 
def drawTable():
    stroke(0,0,0)
    strokeWeight(1)
    offsetRow = 2
    for y in range(row+offsetRow+1):
        for x in range(col):
            if y > offsetRow:
                lib.field_colors(y-(offsetRow))
                rect(screen_xSize*0.05, (120+(y*(textsize1*1.5))), 200, textsize1*1.5)  #column 1
                noFill()
                if x == 4:
                    fill(0,100,200) # Blue cell for Totaal column
                else:
                    fill(255,255,255) # White cells
            else:
                fill(0,0,0) # Black Cells
                rect(screen_xSize*0.05, (120+(y*(textsize1*1.5))), 200, textsize1*1.5)
            rect(((screen_xSize*0.05)+200)+(x*OGfieldW), (120+(y*(textsize1*1.5))), OGfieldW,textsize1*1.5)
            
            if x < len(spelerData):
                '''Color column RGBY horizontal.'''
                lib.field_colors(x+1)
                rect(((screen_xSize*0.05)+200)+(x*OGfieldW), 120+(textsize1*1.5)+(textsize1*2), OGfieldW,(textsize1))
                
                ### Invalid box (GREY rectangles) on table.
                lib.button(((screen_xSize*0.05)+200)+(x*OGfieldW), (120+(2*(textsize1*1.5)))+((x+1)*textsize1*1.5), OGfieldW,(textsize1*1.5),0,100,100,100)
            elif y > 2:
                line(((screen_xSize*0.05)+200)+(x*OGfieldW),(120)+(y*textsize1*1.5), ((screen_xSize*0.05)+200)+(x*OGfieldW),(120+(textsize1*1.5))+(y*textsize1*1.5))

    '''Color column RGBY vertical.'''
    #Names column background
    for y in range(len(spelerData)+3):
        offset = 2
        
            
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
