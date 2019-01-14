
import init_settings as s
import sub_Lib as lib

def setup():
    global screen_xSize, screen_ySize, textsize0, textsize1, textsize2
    global diceCount, dice, diceRes, diceResV, choices, resetknop
    diceCount= s.getDiceCounter()
    screen_xSize, screen_ySize = s.getScreenSize()
    textsize0, textsize1, textsize2 = s.getTextSize(0), s.getTextSize(1), s.getTextSize(2)
    #Dice images
    dice = []
    
    #2 seperate List of Dice Result
    diceRes= []
    diceResV=[]
    
    #Dice BTN names
    choices = ['3 dobbelstenen','4 dobbelstenen']
    
    resetknop =  loadImage('resetknop.png')
    resetknop.resize(40,40)
    
    # Default empty dice
    dice.append(loadImage( "dice_wit.jpg"))
    
    # Dice photo into dice variable
    for i in range(1,7):
       dice.append(loadImage("dice_"+str(i)+".png")) 

def ShowDuelleren():   
    lib.button(0, 250, (screen_xSize*0.8), 50, 0, 255,255,240)# White Bar 1 
    lib.button(0, 550, (screen_xSize*0.8), 50, 0, 255,255,240)# White Bar 2 
    
    lib.fonts("Ariel" , textsize0, True)
    textAlign(LEFT,CENTER)
    fill(50,50,50)
    text('Aanvaller',((screen_xSize*0.0)+20), 250, 200, 50)
    text('Verdediger',((screen_xSize*0.0)+20), 550,200, 50)
    noFill()
    
    lib.fonts("Ariel" , textsize0, True)
    textAlign(CENTER,CENTER)
    # Dice 3 and 4 buttons
    noStroke()
    lib.button(300,110,200,textsize1*2, 50, 255, 0, 0)
    lib.button(550,110,200,textsize1*2, 50, 255, 0, 0)
    
    if diceCount == 3:
        lib.button(300,110,200,textsize1*2, 50,255,200,0)
    elif diceCount == 4:
        lib.button(550,110,200,textsize1*2, 50,255,200,0)
    
    lib.fonts("Ariel", textsize1, False)
    for x in range(2):
        fill(0,0,0)
        text(choices[x],300+(x*250), 110, 200, textsize1*2)
        noFill()

    #Roll & Reset buttons
    for i in range (2):
        stroke(255,0,0)
        lib.button(300+(i*500),(110+(textsize0*1.5)+20),130,textsize0*1.5, 150,255,0,0)
        noStroke()
        
    lib.fonts("Ariel", textsize1, False)
    textAlign(CENTER,CENTER)
    fill(255,255,255)
    text('Rollen!',300,175,130,textsize1*1.5)
    noFill()
    image(resetknop,845,175)
    
    textAlign(CENTER, CENTER)
    lib.fonts("Ariel Bold", textsize2, True)
    fill(255,0,0,170)
    rect(10,110,250,130,25) #red bubble instructions
    fill(255,255,255)
    text('Kies het aantal dobbelsten en rol daarna de dobbelstenen.',10,110,250,130)    
    
    win()
    
    if sumA  == 0:
        for x in range(diceCount):
            image(dice[0], 20+(x*200), 320)
    else:   
        y1 = 0   
        for a in diceRes:
            image(dice[a], 20+(y1*200),320)
            y1 += 1
    
    if sumB == 0:
        for x in range(3):
            image(dice[0], 20+(x*200),620)
    else:
        y2 = 0       
        for a in diceResV:
            image(dice[a],20+(y2*200),620)
            y2 += 1

def rollDice():
    
    global diceCount
    global diceRes, diceResV
    try:
        from random import randint
        x = 0
        y = 0
        while x < diceCount:
            diceRes.append(randint(1,6))
            x+=1
        
        while y < 3:
            diceResV.append(randint(1,6))
            y+=1
    except ExecutionError:
        print("check rollDice function!")
        
def win():
    global diceRes, diceResV
    global sumA,sumB
    sumA = sum(diceRes)
    sumB = sum(diceResV)
    
    # show total points by default
    fill(255,0,0)
    textAlign(LEFT,CENTER)
    lib.fonts("Ariel Bold", textsize0, True)
    text('Totaal: '+str(sumA),(screen_xSize*0.65),250,200,textsize0*1.5)
    text('Totaal: '+str(sumB),(screen_xSize*0.65),550,200,textsize0*1.5)
    
    textAlign(LEFT,CENTER)
    if sumA >= 3 and sumB >= 3:
        if  sumA > sumB:
            text('Wint!', ((screen_xSize*0)+20)+200,250,700,textsize0*1.5) # display text in the White Bar 1
        elif sumA < sumB:
            text('Wint!', ((screen_xSize*0)+20)+200,550,700,textsize0*1.5) # display text in the White Bar 2
        elif sumA == sumB:
            text('Gelijkspel, gooi nog een keer!', (((screen_xSize*0.0)+20)+200),250,500,textsize0*1.5) # display text in the input field box
    noFill()

def setDiceCounter(amount):
    global diceCount 
    diceCount = amount
        
def Reset():
    global diceRes, diceResV
    try:
        diceRes= []
        diceResV=[]
    except ResetError:
        print("Unable to reset diceRes & diceResV")
