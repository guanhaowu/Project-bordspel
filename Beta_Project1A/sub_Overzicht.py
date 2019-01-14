import init_settings as s
import sub_Lib as lib



# spelerData = s.OverzichtData('data')
textsize0, textsize1, textsize2, textsize3 = s.getTextSize(0), s.getTextSize(1), s.getTextSize(2), s.getTextSize(3)
col, row = s.OvTable()
OGfieldH, OGfieldW = s.getInputField('overzicht','height'), s.getInputField('overzicht','width')


def setup():
    global plus, minus, xSize, ySize
    global resetBtnStartX, resetBtnEndX, resetBtnStartY, resetBtnEndY
    global resetReeksBtnStartX, resetReeksBtnEndX, resetReeksBtnStartY, resetReeksBtnEndY
    global screen_xSize, screen_ySize
    global colName
    
    screen_xSize, screen_ySize = s.getScreenSize()
    colName = s.OverzichtData('colName')

    #Reset alles BTN setting
    resetBtnStartX, resetBtnEndX, resetBtnStartY, resetBtnEndY = s.getResetKnop('ResetAll',screen_xSize, screen_ySize)
    
    #Reset Reeks BTN setting
    resetReeksBtnStartX, resetReeksBtnEndX, resetReeksBtnStartY, resetReeksBtnEndY = s.getResetKnop('ResetReeks',screen_xSize, screen_ySize)
    
    xSize, ySize = s.getIconSize()
    try:
        plus = loadImage("plus.jpg")
        minus = loadImage("min.jpg")
    except LoadError:
        print('Unable to load image. Check sub_Overzicht.py .Function: setup().')
    plus.resize(int(xSize), int(ySize))
    minus.resize(int(xSize), int(ySize))
    
    
def OverzichtGegevens(spelerData):
    drawTable(spelerData)
    drawTableText(spelerData)
    drawTableData(spelerData, row)
    drawBtns(plus, minus, xSize, ySize, row)
    
    
    # #Reset alles button
    lib.button(resetBtnStartX, resetBtnStartY, resetBtnEndX, resetBtnEndY, 15,200,200,200)
    fill(0,0,0)
    textAlign(CENTER,CENTER)
    text('Reset alles',resetBtnStartX, resetBtnStartY, resetBtnEndX, resetBtnEndY)
    noFill()
    
    #Reset reeks button
    lib.button(resetReeksBtnStartX, resetReeksBtnStartY, resetReeksBtnEndX, resetReeksBtnEndY, 15,200,200,200)
    fill(0,0,0)
    textAlign(CENTER,CENTER)
    text('Reset Reeks', resetReeksBtnStartX, resetReeksBtnStartY, resetReeksBtnEndX, resetReeksBtnEndY)
    noFill()
    
    drawTableInstructions()

def drawTableInstructions():    
    ## Instruction box bg color
    lib.button(screen_xSize*0.05, screen_ySize*0.6, screen_xSize*0.84, screen_ySize*0.4, 15, 200,200,200,240)
    ## Instruction text
    fill(100,0,100)
    textAlign(LEFT)
    lib.fonts("Ariel", textsize2, False)
    text('Instructies:', (screen_xSize*0.05)+10, (screen_ySize*0.6)+10, screen_xSize*0.9,textsize2*2)
    
    lib.fonts("Ariel", textsize3, False)
    text("Vul eerst uw naam in bij de tab \"Namen\".", ((screen_xSize*0.05)+10),((screen_ySize*0.6)+10)+(textsize2*2), (screen_xSize*0.9),textsize3*1.5)
    text("Gebruik dit overzicht om alles bij te houden gedurende spelronde.", ((screen_xSize*0.05)+10), ((screen_ySize*0.6)+10)+((textsize2*2)*2), (screen_xSize*0.9),textsize3*1.5)
    text("Wanneer een winnaar bekend is van het spel, druk op de \"RESET\" knop om alles terug te zetten naar 0.", (screen_xSize*0.05)+10, ((screen_ySize*0.6)+10)+((textsize2*2)*3), (screen_xSize*0.9),textsize3*1.5)
    text('Gebruik de tab \"Duelleren\" wanneer je iemand aanvalt.', (screen_xSize*0.05)+10, ((screen_ySize*0.6)+10)+((textsize2*2)*4), (screen_xSize*0.9),textsize1*1.5)
    text('Gebruik de tab \"Shortcut\" wanneer je op het kruisingspunt zit voor de shortcut.', ((screen_xSize*0.05)+10), ((screen_ySize*0.6)+10)+((textsize2*2)*5), (screen_xSize*0.9),textsize3*1.5)
    text('Gebruik de tab \"Kaartregels\" als je de regels wilt weten van elke kaart.', ((screen_xSize*0.05)+10), ((screen_ySize*0.6)+10)+((textsize2*2)*6), (screen_xSize*0.9),textsize3*1.5)
    noFill()

### Table layout of columns and rows with colors. 
def drawTableText(spelerData):
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
        if len(spelerData["speler"+str(x+1)]['name']) > 0:
            text(str(spelerData["speler"+str(x+1)]['name']), (screen_xSize*0.05)+5, (120+(textsize1*1.5))+((x+2)*(textsize1*1.5)),200,(textsize1*1.5))
        else:
            text("Speler"+str(x+1), (screen_xSize*0.05)+5, (120+(textsize1*1.5))+((x+2)*(textsize1*1.5)), 200, (textsize1*1.5))
        noFill()
        
        fill(255,255,255)
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
def drawTableData(Data,Row):
    fill(0,0,0)
    textAlign(CENTER,CENTER)
    lib.fonts("Ariel", textsize3, True)
    # Left half table
    try:
        text(str(Data["speler1"]['data'][0]), (((screen_xSize*0.05)+200)+(1*OGfieldW)), (120+(textsize1*1.5)+((2*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(Data["speler1"]['data'][1]), (((screen_xSize*0.05)+200)+(2*OGfieldW)), (120+(textsize1*1.5)+((2*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(Data["speler1"]['data'][2]), (((screen_xSize*0.05)+200)+(3*OGfieldW)), (120+(textsize1*1.5)+((2*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        
        text(str(Data["speler2"]['data'][0]), (((screen_xSize*0.05)+200)+(0*OGfieldW)), (120+(textsize1*1.5)+((3*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(Data["speler2"]['data'][1]), (((screen_xSize*0.05)+200)+(2*OGfieldW)), (120+(textsize1*1.5)+((3*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(Data["speler2"]['data'][2]), (((screen_xSize*0.05)+200)+(3*OGfieldW)), (120+(textsize1*1.5)+((3*(textsize1*1.5)))), OGfieldW, textsize1*1.5)

        text(str(Data["speler3"]['data'][0]), (((screen_xSize*0.05)+200)+(0*OGfieldW)), (120+(textsize1*1.5)+((4*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(Data["speler3"]['data'][1]), (((screen_xSize*0.05)+200)+(1*OGfieldW)), (120+(textsize1*1.5)+((4*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(Data["speler3"]['data'][2]), (((screen_xSize*0.05)+200)+(3*OGfieldW)), (120+(textsize1*1.5)+((4*(textsize1*1.5)))), OGfieldW, textsize1*1.5)

        text(str(Data["speler4"]['data'][0]), (((screen_xSize*0.05)+200)+(0*OGfieldW)), (120+(textsize1*1.5)+((5*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(Data["speler4"]['data'][1]), (((screen_xSize*0.05)+200)+(1*OGfieldW)), (120+(textsize1*1.5)+((5*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
        text(str(Data["speler4"]['data'][2]), (((screen_xSize*0.05)+200)+(2*OGfieldW)), (120+(textsize1*1.5)+((5*(textsize1*1.5)))), OGfieldW, textsize1*1.5)
    except IndexError:
        print("Error at Function: DrawTableText() first half table part")
    noFill()
    # Right half table
    for x in range(3):
        for y in range(Row):
            try:
                fill(255,255,255)
                text(str(Data["speler"+str(y+1)]['data'][0]+Data["speler"+str(y+1)]['data'][1]+Data["speler"+str(y+1)]['data'][2]), (((screen_xSize*0.05)+200)+(4*OGfieldW)), (120+(textsize1*1.5)+((y+2)*(textsize1*1.5))), OGfieldW, textsize1*1.5)
                noFill()
                fill(0,0,0)
                text(str(Data["speler"+str(y+1)]['data'][x+3]), (((screen_xSize*0.05)+200)+((x+5)*OGfieldW)), (120+(textsize1*1.5)+((y+2)*(textsize1*1.5))), OGfieldW, textsize1*1.5)
            except IndexError:
                print("Error at Function: DrawTableText() second half table part")
    noFill()
                    
### Table layout of columns and rows with colors. 
def drawTable(spelerData):
    stroke(0,0,0)
    strokeWeight(1)
    offsetRow = 2
    for y in range(row+offsetRow+1):
        for x in range(col):
            if y > offsetRow:
                '''Color column RGBY vertical.'''
                #Names column background
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

### Plus & Minus buttons.
def drawBtns(plus, minus, xSize, ySize, Row):
    #First half of Table
    for y in range (3):
        # Row 1
        image(minus,(((screen_xSize*0.05)+205)+((y+1)*OGfieldW)),(120+(textsize1*1.7)+(2*(textsize1*1.5))),xSize, ySize)
        image(plus,(((screen_xSize*0.05)+205)+((y+1)*OGfieldW)+(OGfieldW*0.65)),(120+(textsize1*1.7)+(2*(textsize1*1.5))),xSize, ySize)
        
        #Row 4
        image(minus,(((screen_xSize*0.05)+205)+((y)*OGfieldW)),(120+(textsize1*1.7)+(5*(textsize1*1.5))),xSize, ySize)
        image(plus,(((screen_xSize*0.05)+205)+((y)*OGfieldW)+(OGfieldW*0.65)),(120+(textsize1*1.7)+(5*(textsize1*1.5))),xSize, ySize)
        
        if y > 1:
            # Row 2 First elem
            image(minus,(((screen_xSize*0.05)+205)+((y-2)*OGfieldW)),(120+(textsize1*1.7)+(3*(textsize1*1.5))),xSize, ySize)
            image(plus,(((screen_xSize*0.05)+205)+((y-2)*OGfieldW)+(OGfieldW*0.65)),(120+(textsize1*1.7)+(3*(textsize1*1.5))),xSize, ySize)
            
            # Row 3 Column 4
            image(minus,(((screen_xSize*0.05)+205)+((y+1)*OGfieldW)),(120+(textsize1*1.7)+(4*(textsize1*1.5))),xSize, ySize)
            image(plus,(((screen_xSize*0.05)+205)+((y+1)*OGfieldW)+(OGfieldW*0.65)),(120+(textsize1*1.7)+(4*(textsize1*1.5))),xSize, ySize)
            
            for x in range(2):
                # Row 2 Column 3-4
                image(minus,(((screen_xSize*0.05)+205)+((x+2)*OGfieldW)),(120+(textsize1*1.7)+(3*(textsize1*1.5))),xSize, ySize)
                image(plus,(((screen_xSize*0.05)+205)+((x+2)*OGfieldW)+(OGfieldW*0.65)),(120+(textsize1*1.7)+(3*(textsize1*1.5))),xSize, ySize)
                
                # # Row 3 Column 1-2
                image(minus,(((screen_xSize*0.05)+205)+((x)*OGfieldW)),(120+(textsize1*1.7)+(4*(textsize1*1.5))),xSize, ySize)
                image(plus,(((screen_xSize*0.05)+205)+((x)*OGfieldW)+(OGfieldW*0.65)),(120+(textsize1*1.7)+(4*(textsize1*1.5))),xSize, ySize)
    
    # Right half table
    for y in range(Row):
        for x in range(Row-1):
            image(minus,(((screen_xSize*0.05)+205)+((x+5)*OGfieldW)),(120+(textsize1*1.7)+((y+2)*(textsize1*1.5))),xSize, ySize)
            image(plus,(((screen_xSize*0.05)+205)+((x+5)*OGfieldW)+(OGfieldW*0.65)),(120+(textsize1*1.7)+((y+2)*(textsize1*1.5))),xSize, ySize)

def Reset(spelerData, arg):
    if arg == 'ResetAll':
        for x in range (len(spelerData)):
            for y in range(6):
                spelerData['speler'+str(x+1)]['data'][y] = 0
            Reset(spelerData, 'ResetReeks')
        
    if arg == 'ResetReeks':
        for x in range (len(spelerData)):
            spelerData['speler'+str(x+1)]['data'][5] = 0
        return spelerData
