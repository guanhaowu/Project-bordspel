import init_settings as s
import sub_Lib as lib
import sub_Overzicht as OG
import sub_Names as name
import sub_Duelleren as Duel
import sub_Rad as Rad
import sub_KaartRegels as Kaart

screen_xSize, screen_ySize = s.getScreenSize()
def setup():
    global xSize, ySize, bgImg
    global radNum, activeTab, tabNames, textsize1, textsize2, textsize3
    global spelerData, inputFieldNum
    global resetBtnStartX, resetBtnEndX, resetBtnStartY, resetBtnEndY # ResetAll Btn
    global resetReeksBtnStartX, resetReeksBtnEndX, resetReeksBtnStartY, resetReeksBtnEndY # ResetReeks Btn
    global inputFieldWidth, inputFieldHeight, OGfieldH, OGfieldW
    
    xSize, ySize = s.getIconSize()
    tabNames = s.getMenuList()
    spelerData = s.OverzichtData('data')
    inputFieldNum = len(spelerData)
    
    size(screen_xSize, screen_ySize)
    
    #load background image into memory.
    bgImg = s.loadBG()
    s.getBgImg(bgImg, screen_xSize, screen_ySize)
    
    activeTab = s.getTab()
    
    textsize1, textsize2, textsize3 = s.getTextSize(1), s.getTextSize(2), s.getTextSize(3)
    
    inputFieldWidth = s.getInputField('name','width')
    inputFieldHeight = s.getInputField('name','height')
    OGfieldH, OGfieldW = s.getInputField('overzicht','height'), s.getInputField('overzicht','width')
    
    #Reset alles BTN setting
    resetBtnStartX, resetBtnEndX, resetBtnStartY, resetBtnEndY = s.getResetKnop('ResetAll',screen_xSize, screen_ySize)
    
    #Reset Reeks BTN setting
    resetReeksBtnStartX, resetReeksBtnEndX, resetReeksBtnStartY, resetReeksBtnEndY = s.getResetKnop('ResetReeks',screen_xSize, screen_ySize)
    
    OG.setup()
    Duel.setup()
    Rad.setup()
    # Rad data
    radNum = 0
    Kaart.setup()
    name.setup()
    
#Menu buttons Grey
def menuButton():
    stroke(150,150,150)
    for x in range(len(tabNames)):
        lib.button((screen_xSize*0.02)+(x*200), 10, 180, textsize1*2, 10, 150, 150, 150) 
    
    #Menu Light-Grey Bar
    lib.button(0, 80, screen_xSize, 20,0,200,200,200)
    noStroke()
    
def menuText():
    lib.fonts("Arial Bold Italic", textsize1, False)
    textAlign(CENTER,CENTER)
    for x in range(len(tabNames)):   
        fill(0,0,0)
        text(tabNames[x], screen_xSize/100*2+(x*(200)), 10, 180, textsize1*2)
        noFill()
    
def mousePressed():
    global diceCount, radNum
    global spelerData
    global activeTab
    global selected_field
    
    debug = s.debug('mouse', 0)
    lib.getMouseClickLoc(debug)
    
    if mouseButton == LEFT:
        if mouseX > 20 and mouseX < 200 and mouseY > 10 and mouseY < 60:
            activeTab = 0
        if mouseX > 220 and mouseX < 400 and mouseY > 10 and mouseY < 60:
            activeTab = 1
        if mouseX > 420 and mouseX < 600 and mouseY > 10 and mouseY < 60:
            activeTab = 2
        if mouseX > 620 and mouseX < 800 and mouseY > 10 and mouseY < 60:   
            activeTab = 3
        if mouseX > 820 and mouseX < 1000 and mouseY > 10 and mouseY < 60: 
            activeTab = 4
        
        #OverzichtGegevens page
        if activeTab == 0:
            # First Half
            for y in range (3):
                # Row 1 1-3 elem min
                if mouseX >(((screen_xSize*0.05)+205)+((y+1)*OGfieldW)) and mouseX < (((screen_xSize*0.05)+205)+((y+1)*OGfieldW)) + xSize:
                    if mouseY > (120+(textsize1*1.7)+(2*(textsize1*1.5))) and mouseY < (120+(textsize1*1.7)+(2*(textsize1*1.5)))+ ySize:
                        if spelerData['speler1']['data'][y] > 0:
                            spelerData['speler1']['data'][y] -= 1
                
                # Row 1 1-3 elem min            
                if mouseX >(((screen_xSize*0.05)+205)+((y+1)*OGfieldW)+(OGfieldW*0.65)) and mouseX < (((screen_xSize*0.05)+205)+((y+1)*OGfieldW)+(OGfieldW*0.65)) + xSize:
                    if mouseY > (120+(textsize1*1.7)+(2*(textsize1*1.5))) and mouseY < (120+(textsize1*1.7)+(2*(textsize1*1.5)))+ ySize:
                        spelerData['speler1']['data'][y] += 1
                
                #Row 4 0-3 elem min
                if mouseX > (((screen_xSize*0.05)+205)+((y)*OGfieldW)) and mouseX < (((screen_xSize*0.05)+205)+((y)*OGfieldW)) + xSize:
                    if mouseY >(120+(textsize1*1.7)+(5*(textsize1*1.5))) and mouseY < (120+(textsize1*1.7)+(5*(textsize1*1.5)))+ySize:
                        if spelerData['speler4']['data'][y] > 0:
                            spelerData['speler4']['data'][y] -= 1
                
                #Row 4 0-3 elem plus
                if mouseX >(((screen_xSize*0.05)+205)+((y)*OGfieldW)+(OGfieldW*0.65)) and mouseX < (((screen_xSize*0.05)+205)+((y)*OGfieldW)+(OGfieldW*0.65)) + xSize:
                    if mouseY > (120+(textsize1*1.7)+(5*(textsize1*1.5))) and mouseY < (120+(textsize1*1.7)+(5*(textsize1*1.5)))+ ySize:
                        spelerData['speler4']['data'][y] += 1
                
                if y > 1:
                    # Row 2 First elem min
                    if mouseX > (((screen_xSize*0.05)+205)+((y-2)*OGfieldW)) and mouseX < (((screen_xSize*0.05)+205)+((y-2)*OGfieldW)) + xSize :
                        if mouseY > (120+(textsize1*1.7)+(3*(textsize1*1.5))) and mouseY < (120+(textsize1*1.7)+(3*(textsize1*1.5))) + ySize :
                            if spelerData['speler2']['data'][y-2] > 0:
                                spelerData['speler2']['data'][y-2] -= 1
                    
                    # Row 2 First elem plus
                    if mouseX >(((screen_xSize*0.05)+205)+((y-2)*OGfieldW)+(OGfieldW*0.65)) and mouseX < (((screen_xSize*0.05)+205)+((y-2)*OGfieldW)+(OGfieldW*0.65)) + xSize :
                        if mouseY > (120+(textsize1*1.7)+(3*(textsize1*1.5))) and mouseY < (120+(textsize1*1.7)+(3*(textsize1*1.5))) + ySize :
                            spelerData['speler2']['data'][y-2] += 1
                    
                    # Row 3 Column 4 min
                    if mouseX > (((screen_xSize*0.05)+205)+((y+1)*OGfieldW)) and mouseX < (((screen_xSize*0.05)+205)+((y+1)*OGfieldW)) + xSize:
                        if mouseY > (120+(textsize1*1.7)+(4*(textsize1*1.5))) and mouseY < (120+(textsize1*1.7)+(4*(textsize1*1.5))) + ySize:
                            if spelerData['speler3']['data'][y] > 0:
                                spelerData['speler3']['data'][y] -= 1
                    
                    # Row 3 Column 4 plus
                    if mouseX > (((screen_xSize*0.05)+205)+((y+1)*OGfieldW)+(OGfieldW*0.65)) and mouseX < (((screen_xSize*0.05)+205)+((y+1)*OGfieldW)+(OGfieldW*0.65)) + xSize:
                        if mouseY > (120+(textsize1*1.7)+(4*(textsize1*1.5))) and mouseY < (120+(textsize1*1.7)+(4*(textsize1*1.5))) + ySize:
                            spelerData['speler3']['data'][y] += 1
                    
                    for x in range(2):
                        # Row 2 Column 3-4 min
                        if mouseX > (((screen_xSize*0.05)+205)+((x+2)*OGfieldW)) and mouseX < (((screen_xSize*0.05)+205)+((x+2)*OGfieldW)) + xSize:
                            if mouseY > (120+(textsize1*1.7)+(3*(textsize1*1.5))) and mouseY < (120+(textsize1*1.7)+(3*(textsize1*1.5))) + ySize:
                               if spelerData['speler2']['data'][x+1] > 0:
                                spelerData['speler2']['data'][x+1] -= 1 
                        
                        # Row 2 Column 3-4 plus        
                        if mouseX > (((screen_xSize*0.05)+205)+((x+2)*OGfieldW)+(OGfieldW*0.65)) and mouseX < (((screen_xSize*0.05)+205)+((x+2)*OGfieldW)+(OGfieldW*0.65)) + xSize:
                            if mouseY > (120+(textsize1*1.7)+(3*(textsize1*1.5))) and mouseY < (120+(textsize1*1.7)+(3*(textsize1*1.5))) + ySize:
                                spelerData['speler2']['data'][x+1] += 1 
                        
                        # Row 3 Column 1-2min
                        if mouseX > (((screen_xSize*0.05)+205)+((x)*OGfieldW)) and mouseX < (((screen_xSize*0.05)+205)+((x)*OGfieldW)) + xSize:
                            if mouseY > (120+(textsize1*1.7)+(4*(textsize1*1.5))) and mouseY < (120+(textsize1*1.7)+(4*(textsize1*1.5))) + ySize:
                               if spelerData['speler3']['data'][x] > 0:
                                spelerData['speler3']['data'][x] -= 1 
                        
                        # Row 3 Column 1-2min  
                        if mouseX > (((screen_xSize*0.05)+205)+((x)*OGfieldW)+(OGfieldW*0.65)) and mouseX < (((screen_xSize*0.05)+205)+((x)*OGfieldW)+(OGfieldW*0.65)) + xSize:
                            if mouseY > (120+(textsize1*1.7)+(4*(textsize1*1.5))) and mouseY < (120+(textsize1*1.7)+(4*(textsize1*1.5))) + ySize:
                                spelerData['speler3']['data'][x] += 1                                
            
            # Right half table
            #Col then Row
            for y in range(len(spelerData)):
                for x in range(len(spelerData)-1):
                    # minus
                    if mouseX > (((screen_xSize*0.05)+205)+((x+5)*OGfieldW)) and mouseX < (((screen_xSize*0.05)+205)+((x+5)*OGfieldW)) + xSize:
                        if mouseY > (120+(textsize1*1.7)+((y+2)*(textsize1*1.5))) and mouseY < (120+(textsize1*1.7)+((y+2)*(textsize1*1.5))) + ySize:
                            if spelerData['speler'+str(y+1)]['data'][x+3] > 0:
                                spelerData['speler'+str(y+1)]['data'][x+3] -= 1
                                
                    # plus
                    if mouseX > (((screen_xSize*0.05)+205)+((x+5)*OGfieldW)+(OGfieldW*0.65)) and mouseX < (((screen_xSize*0.05)+205)+((x+5)*OGfieldW)+(OGfieldW*0.65)) + xSize:
                        if mouseY > (120+(textsize1*1.7)+((y+2)*(textsize1*1.5))) and mouseY < (120+(textsize1*1.7)+((y+2)*(textsize1*1.5))) + ySize:                  
                            spelerData['speler'+str(y+1)]['data'][x+3] += 1

            # Reset all Overzicht data
            if mouseX > resetBtnStartX and mouseX < resetBtnStartX + resetBtnEndX and mouseY > resetBtnStartY and mouseY < resetBtnStartY + resetBtnEndY :
                OG.Reset(spelerData, 'ResetAll')
            # Reset Reeks data
            if mouseX > resetReeksBtnStartX and mouseX < resetReeksBtnStartX + resetReeksBtnEndX and mouseY > resetReeksBtnStartY and mouseY < resetReeksBtnStartY + resetReeksBtnEndY :
                OG.Reset(spelerData, 'ResetReeks')
        
        #Shortcut Tab        
        if activeTab == 2: #screen_xSize*0.125, screen_ySize*0.72, 200, textsize1*1.5, 10,255,255,255
            if mousePressed and mouseButton == LEFT and (mouseX > (screen_xSize*0.125)) and (mouseX < (screen_xSize*0.125)+200) and (mouseY > screen_ySize*0.72) and (mouseY < (screen_ySize*0.72)+(textsize1*1.5)):
                radNum = Rad.SpinRad()
                return radNum
        
        #Dueleren Tab
        if activeTab == 1:
            if mouseX > 300 and mouseX < 500 and mouseY > 110 and mouseY < 160:
                Duel.Reset() 
                Duel.setDiceCounter(3)   
                
            if mouseX > 550 and mouseX < 750 and mouseY > 110 and mouseY < 160:
                Duel.Reset() 
                Duel.setDiceCounter(4) 
            
            if mouseX > 300 and mouseX < 430 and mouseY > 175 and mouseY < 225:
                Duel.Reset() 
                Duel.rollDice()
                Duel.win()
            #reset button click area
            if mouseX > 800 and mouseX < 930 and mouseY > 175 and mouseY < 225:
                Duel.Reset() 
        
        #Namen Tab        
        if activeTab == 4:
            for x in range(inputFieldNum):
                if mouseX >(screen_xSize/100*5)+100 and mouseX < ((screen_xSize/100*5)+100+inputFieldWidth) and mouseY >(120+(textsize1*1.5))+(x*(textsize2*1.5)) and mouseY < (120+(textsize1*1.5))+(x*(textsize2*1.5))+(textsize2*1.5):
                    selected_field = x+1
                    return selected_field
                else:
                    selected_field = None
        

                            
def keyPressed():
    global spelerData, selected_field, activeTab
    
    if activeTab == 4 and selected_field != None:
        # SHIFT keyCode = 16;
        # keyCode 17 = CONTROL, 18 = ALT pressed
        # keyCode 9 = TAB
        if key == TAB:
            if selected_field >= inputFieldNum:
                selected_field = 1
            else:
                selected_field = selected_field +1
        elif key==BACKSPACE:
            if len(spelerData["speler"+str(selected_field)]['name']) > 0:
                spelerData["speler"+str(selected_field)]['name'] = spelerData["speler"+str(selected_field)]['name'][:len(spelerData["speler"+str(selected_field)]['name'])-1]
        elif key==ENTER or key==RETURN:
            selected_field = None
        elif (key >= 'A' and key <='Z') or (key >='a' and key <= 'z') or keyCode == 32 or key == SHIFT:
            if len(spelerData["speler"+str(selected_field)]['name']) < 10:
                spelerData["speler"+str(selected_field)]['name'] = spelerData["speler"+str(selected_field)]['name'] + str(key)
                return spelerData["speler"+str(selected_field)]['name']
                                    
def draw():
    s.getBgImg(bgImg, screen_xSize, screen_ySize)
    menuButton()
    lib.button(screen_xSize/100*2+(activeTab*200), 10, 180, textsize1*2, 10, 255, 255, 0)
    menuText()

    if activeTab == 0:
        frameRate(10)
        OG.OverzichtGegevens(spelerData)
    elif activeTab == 1:
        frameRate(60)
        Duel.ShowDuelleren()
    elif activeTab == 2:
        frameRate(60)
        Rad.ShowRad(radNum)
        mousePressed()
    elif activeTab == 3:
        frameRate(10)
        Kaart.Kaartregels()
    elif activeTab == 4:
        frameRate(30)
        name.ShowNames(spelerData,selected_field)
