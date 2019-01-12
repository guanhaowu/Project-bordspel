import init_settings as s
import sub_Lib as lib
import sub_Overzicht as gegevens
import sub_Names as name
import sub_Duelleren as Duel
import sub_Rad as Rad
import sub_KaartRegels as Kaart

inputFieldWidth = 308

# Initial Data for GegevensOverzicht
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

#OverzichtGegevens: amount columns next to Names
OverzichtColumn = 8
OverzichtRows = 4

#TEST
# screen_xSize, screen_ySize  = s.getScreenSize()

spelerNamen, selected_field = s.init('TabNamen')
inputFieldNum = len(spelerNamen)


screen_xSize, screen_ySize = s.getScreenSize()
def setup():
    global bgImg, plus, minus
    global radNum, activeTab, tabNames, textsize1, textsize2, textsize3
    global resetBtnStartX, resetBtnEndX, resetReeksBtnStartX, resetReeksBtnEndX
    
    tabNames = s.getMenuList()

    size(screen_xSize, screen_ySize)
    #load background image into memory.
    bgImg = s.loadBG()
    s.getBgImg(bgImg, screen_xSize, screen_ySize)
    
    activeTab = s.getTab()
    
    textsize1, textsize2, textsize3 = s.getTextSize(1), s.getTextSize(2), s.getTextSize(3)
    Rad.setup()
    # Rad data
    radNum = 0
    
    Kaart.setup()
    Duel.setup()
    
    plus = loadImage("Pluse.jpg")
    minus = loadImage("min.jpg")

    #Reset alles BTN setting
    resetBtnStartX = screen_xSize/100*8
    resetBtnEndX = 200 #button width
    
    #Reset Reeks BTN setting
    resetReeksBtnStartX = screen_xSize/100*70
    resetReeksBtnEndX = 150

#Menu buttons Grey
def menuButton():
    for x in range(len(tabNames)):
        lib.button(screen_xSize/100*2+(x*200), 10, 180, textsize1*2, 10, 150, 150, 150) 
    
    #Menu Light-Grey Bar
    lib.button(0, 70, screen_xSize, 30,0,200,200,200)

def menuText():
    lib.fonts("Arial Bold Italic", textsize1, True)
    textAlign(CENTER,CENTER)
    for x in range(len(tabNames)):   
        fill(0,0,0)
        text(tabNames[x], screen_xSize/100*2+(x*(200)), 10, 180, textsize1*2)
        noFill()

def active(type):
    if type == 'diceChoiceBtn':
        return fill(255,200,0)
    
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
    
    
def mousePressed():
    global Rood_tegen_Groen,Rood_tegen_Blauw, Rood_tegen_Geel
    global Groen_tegen_Rood, Groen_tegen_Blauw,Groen_tegen_Geel
    global Blauw_tegen_Rood,Blauw_tegen_Groen,Blauw_tegen_Geel
    global Geel_tegen_Rood,Geel_tegen_Groen,Geel_tegen_Blauw
    global Rood_Gevangenis,Groen_Gevangenis,Blauw_Gevangenis,Geel_Gevangenis
    global Rood_Boer,Groen_Boer,Blauw_Boer,Geel_Boer 
    global Rood_Reeks, Groen_Reeks, Blauw_Reeks,Geel_Reeks
    global diceCount, radNum
    
    global activeTab
    global selected_field
    
    debug = s.debug('mouse')
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
            pass
            #kolom 1
            # if mouseX > 250 and mouseX < 268  and mouseY > 201 and mouseY < 219:
            #     if Groen_tegen_Rood > 0:
            #         Groen_tegen_Rood = Groen_tegen_Rood - 1    
            # elif mouseX > 330 and mouseX < 348  and mouseY > 201 and mouseY < 219:
            #     Groen_tegen_Rood = Groen_tegen_Rood + 1
            # elif mouseX > 250 and mouseX < 268  and mouseY > 222 and mouseY < 240:
            #     if Blauw_tegen_Rood > 0:
            #         Blauw_tegen_Rood = Blauw_tegen_Rood - 1
            # elif mouseX > 330 and mouseX < 348  and mouseY > 222 and mouseY < 240:
            #     Blauw_tegen_Rood = Blauw_tegen_Rood + 1
            # elif mouseX > 250 and mouseX < 268  and mouseY > 242 and mouseY < 260:
            #     if Geel_tegen_Rood > 0:
            #         Geel_tegen_Rood = Geel_tegen_Rood - 1
            # elif mouseX > 330 and mouseX < 348  and mouseY > 242 and mouseY < 260:
            #     Geel_tegen_Rood = Geel_tegen_Rood + 1
            # #kolom 2
            # elif mouseX > 350 and mouseX < 368  and mouseY > 182 and mouseY < 200:
            #     if Rood_tegen_Groen > 0:
            #         Rood_tegen_Groen = Rood_tegen_Groen - 1
            # elif mouseX > 430 and mouseX < 448  and mouseY > 182 and mouseY < 200:
            #     Rood_tegen_Groen = Rood_tegen_Groen + 1
            # elif mouseX > 350 and mouseX < 368  and mouseY > 222 and mouseY < 240:
            #     if Blauw_tegen_Groen > 0:
            #         Blauw_tegen_Groen = Blauw_tegen_Groen - 1
            # elif mouseX > 430 and mouseX < 448  and mouseY > 222 and mouseY < 240:
            #     Blauw_tegen_Groen = Blauw_tegen_Groen + 1
            # elif mouseX > 350 and mouseX < 368  and mouseY > 242 and mouseY < 260:
            #     if Geel_tegen_Groen > 0:
            #         Geel_tegen_Groen = Geel_tegen_Groen - 1
            # elif mouseX > 430 and mouseX < 448  and mouseY > 242 and mouseY < 260:
            #     Geel_tegen_Groen = Geel_tegen_Groen + 1
            # #kolom 3
            # elif mouseX > 450 and mouseX < 468  and mouseY > 181 and mouseY < 199:
            #     if Rood_tegen_Blauw > 0:
            #         Rood_tegen_Blauw = Rood_tegen_Blauw - 1
            # elif mouseX > 530 and mouseX < 548  and mouseY > 181 and mouseY < 191:
            #     Rood_tegen_Blauw = Rood_tegen_Blauw + 1
            # elif mouseX > 450 and mouseX < 468  and mouseY > 202 and mouseY < 220:
            #     if Groen_tegen_Blauw > 0:
            #         Groen_tegen_Blauw = Groen_tegen_Blauw - 1
            # elif mouseX > 530 and mouseX < 548  and mouseY > 202 and mouseY < 220:
            #     Groen_tegen_Blauw = Groen_tegen_Blauw + 1
            # elif mouseX > 450 and mouseX < 468  and mouseY > 242 and mouseY < 260:
            #     if Geel_tegen_Blauw > 0:
            #         Geel_tegen_Blauw = Geel_tegen_Blauw - 1
            # elif mouseX > 530 and mouseX < 548  and mouseY > 242 and mouseY < 260:
            #     Geel_tegen_Blauw = Geel_tegen_Blauw + 1
            # #kolom 4
            # elif mouseX > 550 and mouseX < 568  and mouseY > 181 and mouseY < 199:
            #     if Rood_tegen_Geel > 0:
            #         Rood_tegen_Geel = Rood_tegen_Geel - 1
            # elif mouseX > 630 and mouseX < 648  and mouseY > 181 and mouseY < 199:
            #     Rood_tegen_Geel = Rood_tegen_Geel + 1
            # elif mouseX > 550 and mouseX < 568  and mouseY > 202 and mouseY < 220:
            #     if Groen_tegen_Geel > 0:
            #         Groen_tegen_Geel = Groen_tegen_Geel - 1
            # elif mouseX > 630 and mouseX < 648  and mouseY > 202 and mouseY < 220:
            #     Groen_tegen_Geel = Groen_tegen_Geel + 1
            # elif mouseX > 550 and mouseX < 568  and mouseY > 222 and mouseY < 240:
            #     if Blauw_tegen_Geel > 0:
            #         Blauw_tegen_Geel = Blauw_tegen_Geel - 1
            # elif mouseX > 630 and mouseX < 648  and mouseY > 222 and mouseY < 240:
            #     Blauw_tegen_Geel = Blauw_tegen_Geel + 1
            # #kolom 5
            # elif mouseX > 650 and mouseX < 668  and mouseY > 181 and mouseY < 199:
            #     if Rood_Gevangenis > 0:
            #         Rood_Gevangenis = Rood_Gevangenis - 1
            # elif mouseX > 730 and mouseX < 748  and mouseY > 181 and mouseY < 199:
            #     Rood_Gevangenis = Rood_Gevangenis + 1
            # elif mouseX > 650 and mouseX < 668  and mouseY > 202 and mouseY < 220:
            #     if Groen_Gevangenis > 0:
            #         Groen_Gevangenis = Groen_Gevangenis - 1
            # elif mouseX > 730 and mouseX < 748  and mouseY > 202 and mouseY < 220:
            #     Groen_Gevangenis = Groen_Gevangenis + 1
            # elif mouseX > 650 and mouseX < 668  and mouseY > 222 and mouseY < 240:
            #     if Blauw_Gevangenis > 0:
            #         Blauw_Gevangenis = Blauw_Gevangenis - 1
            # elif mouseX > 730 and mouseX < 748  and mouseY > 222 and mouseY < 240:
            #     Blauw_Gevangenis = Blauw_Gevangenis + 1
            # elif mouseX > 650 and mouseX < 668  and mouseY > 242 and mouseY < 260:
            #     if Geel_Gevangenis > 0:
            #         Geel_Gevangenis = Geel_Gevangenis - 1
            # elif mouseX > 730 and mouseX < 748  and mouseY > 242 and mouseY < 260:
            #     Geel_Gevangenis = Geel_Gevangenis + 1
            # #kolom 6
            # elif mouseX > 750 and mouseX < 768  and mouseY > 181 and mouseY < 199:
            #     if Rood_Boer > 0:
            #         Rood_Boer = Rood_Boer - 1
            # elif mouseX > 830 and mouseX < 848  and mouseY > 181 and mouseY < 199:
            #     Rood_Boer = Rood_Boer + 1
            # elif mouseX > 750 and mouseX < 768  and mouseY > 202 and mouseY < 220:
            #     if Groen_Boer > 0:
            #         Groen_Boer = Groen_Boer - 1
            # elif mouseX > 830 and mouseX < 848  and mouseY > 202 and mouseY < 220:
            #     Groen_Boer = Groen_Boer + 1
            # elif mouseX > 750 and mouseX < 768  and mouseY > 222 and mouseY < 240:
            #     if Blauw_Boer > 0:
            #         Blauw_Boer = Blauw_Boer - 1
            # elif mouseX > 830 and mouseX < 848  and mouseY > 222 and mouseY < 240:
            #     Blauw_Boer = Blauw_Boer + 1
            # elif mouseX > 750 and mouseX < 768  and mouseY > 242 and mouseY < 260:
            #     if Geel_Boer > 0:
            #         Geel_Boer = Geel_Boer - 1
            # elif mouseX > 830 and mouseX < 848  and mouseY > 242 and mouseY < 260:
            #     Geel_Boer = Geel_Boer + 1
            # #kolom 7
            # elif mouseX > 850 and mouseX < 868  and mouseY > 181 and mouseY < 199:
            #     if Rood_Reeks > 0:
            #         Rood_Reeks = Rood_Reeks - 1
            # elif mouseX > 930 and mouseX < 948  and mouseY > 181 and mouseY < 199:
            #     Rood_Reeks = Rood_Reeks + 1
            # elif mouseX > 850 and mouseX < 868  and mouseY > 202 and mouseY < 220:
            #     if Groen_Reeks > 0:
            #         Groen_Reeks = Groen_Reeks - 1
            # elif mouseX > 930 and mouseX < 948  and mouseY > 202 and mouseY < 220:
            #     Groen_Reeks = Groen_Reeks + 1
            # elif mouseX > 850 and mouseX < 868  and mouseY > 222 and mouseY < 240:
            #     if Blauw_Reeks > 0:
            #         Blauw_Reeks = Blauw_Reeks - 1
            # elif mouseX > 930 and mouseX < 948  and mouseY > 222 and mouseY < 240:
            #     Blauw_Reeks = Blauw_Reeks + 1
            # elif mouseX > 850 and mouseX < 868  and mouseY > 242 and mouseY < 260:
            #     if Geel_Reeks > 0:
            #         Geel_Reeks = Geel_Reeks - 1
            # elif mouseX > 930 and mouseX < 948  and mouseY > 242 and mouseY < 260:
            #     Geel_Reeks = Geel_Reeks + 1
            # #resetBtnStartX, resetBtnEndX
            # elif mouseX > resetBtnStartX and mouseX < resetBtnStartX + resetBtnEndX and mouseY > screen_ySize/100*35 and mouseY < screen_ySize/100*35 +35 :
            #     Reset('OverzichtGegevens')
            # elif mouseX >resetReeksBtnStartX and mouseX < resetReeksBtnStartX + resetReeksBtnEndX and mouseY > screen_ySize/100*35 and mouseY < screen_ySize/100*35 +35 :
            #     Reset('ResetReeks')
        
        #Shortcut Tab        
        if activeTab == 2:
            if mousePressed and mouseButton == LEFT and (mouseX > 400) and (mouseX <600) and (mouseY >250) and (mouseY < 290):
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
                if mouseX >(screen_xSize/100*5)+100 and mouseX < (screen_xSize/100*5)+100+inputFieldWidth and mouseY >(120+(textsize1*1.5))+(x*(textsize2*1.5)) and mouseY < (120+(textsize1*1.5))+(x*(textsize2*1.5))+(textsize2*1.5):
                    selected_field = x+1
                    return selected_field
                else:
                    selected_field = None
        

                            
def keyPressed():
    global spelerNamen, selected_field, activeTab
    
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
            if len(spelerNamen["speler"+str(selected_field)]) > 0:
                spelerNamen["speler"+str(selected_field)] = spelerNamen["speler"+str(selected_field)][:len(spelerNamen["speler"+str(selected_field)])-1]
        elif key==ENTER or key==RETURN:
            # Enter new line, not used in this program.
            # spelerNamen["speler"+str(selected_field)] = spelerNamen["speler"+str(selected_field)] + "\n"
            selected_field = None
        elif (key >= 'A' and key <='Z') or (key >='a' and key <= 'z') or keyCode == 32 or key == SHIFT:
            if len(spelerNamen["speler"+str(selected_field)]) < 10:
                spelerNamen["speler"+str(selected_field)] = spelerNamen["speler"+str(selected_field)] + str(key)
        
                                    
def draw():
    s.getBgImg(bgImg, screen_xSize, screen_ySize)
    menuButton()
    lib.button(screen_xSize/100*2+(activeTab*200), 10, 180, textsize1*2, 10, 255, 255, 0)
    menuText()

    if activeTab == 0:
        gegevens.OverzichtGegevens()
    elif activeTab == 1:
        Duel.ShowDuelleren()
    elif activeTab == 2:
        Rad.ShowRad(radNum)
        mousePressed()
    elif activeTab == 3:
        Kaart.Kaartregels()
    elif activeTab == 4:
        name.ShowNames(spelerNamen,selected_field)
