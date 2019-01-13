import init_settings as s
import sub_Lib as lib

screen_xSize, screen_ySize = s.getScreenSize()
inputFieldWidth = s.getInputField('name','width')
inputFieldHeight = s.getInputField('name','height')
textsize1,textsize2 = s.getTextSize(1), s.getTextSize(2)
spelerNamen, selected_field = s.OverzichtData('name'), s.OverzichtData('field')

def setup():
    global blinkTime, blinkOn, blinkLine
    #Switch on/off
    blinkTime = millis()
    blinkOn = True
    blinkLine = ""
                                
def ShowNames(spelerNamen, selected_field):
    global blinkTime, blinkOn, blinkLine

    inputFieldNum = len(spelerNamen)
    
    # Table rect bar    
    fill(0,0,0)
    rect(screen_xSize/100*5, 120, 100+inputFieldWidth, textsize1*1.5)
    noFill()
    
    # Table Text name
    fill(255,255,255)
    lib.fonts("Arial Bold", textsize1, True)
    textAlign(CENTER,CENTER)
    text("Vul uw naam hier onder in:", screen_xSize/100*5, 120, 100+inputFieldWidth, textsize1*1.5)
    noFill()

    # Player Name Column 1 colors
    lib.fonts("Arial", textsize2, True)
    for x in range(inputFieldNum):
        noStroke()
        lib.field_colors(x+1)
        rect(screen_xSize/100*5, (120+(textsize1*1.5))+(x*(textsize2*1.5)), 100, textsize2*1.5)  #column 1
        noFill()
        
        # Player1-4 Text Column 1
        fill(0,0,0)# Text color
        textAlign(LEFT,CENTER) # text alignment
        text("Speler" + str(x+1), (screen_xSize/100*5)+10, (120+(textsize1*1.5))+(x*(textsize2*1.5)), 100, textsize2*1.5) #player1-4 column 1
        noFill()
        
        stroke(6)
        # highlight selected field upon click or Tab.
        if (x+1) == selected_field:
            #Beige text field upon selected
            fill(255,255,160)
            rect((screen_xSize/100*5)+100, (120+(textsize1*1.5))+(x*(textsize2*1.5)), inputFieldWidth, textsize2*1.5) #column 2
            noFill()
            
            #Show input text when typed.
            fill(0,0,0)
            # display text in the input field box
            text(str(spelerNamen["speler"+str(x+1)])+blinkLine,(screen_xSize/100*5)+110, (120+(textsize1*1.5))+(x*(textsize2*1.5)), inputFieldWidth, textsize2*1.5)
            noFill()
        else:
            #Show White Input Text Field
            fill(255,255,255)
            rect((screen_xSize/100*5)+100, (120+(textsize1*1.5))+(x*(textsize2*1.5)), inputFieldWidth, textsize2*1.5) #column 2
            noFill()
            
            #Show text from spelerNamen list.
            fill(0,0,0)
            # display text in the input field box
            text(str(spelerNamen["speler"+str(x+1)]), (screen_xSize/100*5)+110, (120+(textsize1*1.5))+(x*(textsize2*1.5)), inputFieldWidth, textsize2*1.5)
            noFill()
        noStroke()
        
    if blinkOn:
        fill(0,0,0)
        blinkLine = "|"
        noFill()
    else:
        blinkLine = ""
        
    if (millis() - 250 > blinkTime):
        blinkTime = millis()
        blinkOn = not blinkOn
