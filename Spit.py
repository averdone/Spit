##/*  Spit
##Spit.java
##Anthony Verdone 
##amverdon
##Your section (2) */

from random import randrange
from Graphics import*
import time


#PLACEMENTS FOR CARDS/KEYS
## Z CARD
zCard = Point(9,20)
## X CARD
xCard = Point(19,20)
xCard2 = Point(19,23)
## C CARD
cCard = Point(29,20)
cCard2 = Point(29,23)
cCard3 = Point(29,26)

## M CARD
mCard = Point(91,20)
## N CARD
nCard = Point(81,20)
nCard2 = Point(81,23)
## B CARD
bCard = Point(71,20)
bCard2 = Point(71,23)
bCard3 = Point(71,26)

## G CARD
gCard = Point(30,70)
## H CARD
hCard = Point(70,70)

##SPIT PILE 1
spitCard1 = Point(45,70)
##SPIT PILE 2
spitCard2 = Point(55,70)
#PLACEMENT FOR KEYS
#key = Image(Point(X VALUE OF CARD,4.5),"NAME.gif").draw(win)



def setUpWindow():
    #sets up window, opens new window
    window = GraphWin("SPIT", 1200,700)
    window.setCoords(0,0,100,100)
    window.setBackground('lightgreen')
    return window

def newBackdrop(win):
    #removes every item drawn in a window
    newBackdrop = Rectangle(Point(0,0),Point(100,100))
    newBackdrop.setFill('lightgreen')
    newBackdrop.draw(win)
    
def displayInstructions(fname,win):
    #displays instructions
    title = Text(Point(50,75), "INSTRUCTIONS")
    title.setFace("arial")
    title.setSize(25)
    title.setStyle("bold")
    title.draw(win)
    infile = open(fname, 'r')
    #y value for the text
    y = 65
    for line in infile:
        display = Text(Point(50,y), line)
        display.setFace("arial")
        display.setSize(20)
        display.draw(win)
        y -= 5
    win.getMouse()
    newBackdrop(win)

def processClick(x1,x2,y1,y2,win):
    #checks for mouse click
    point=win.checkMouse()
    #keeps checking
    while point == None:
        point = win.getMouse()
    #returns the values
    x = point.getX()
    y = point.getY()
    coords = [x,y]
    #checks to see if values matched to the button
    if (coords[0] >=x1 and coords[0] <=x2) and (coords[1]>=y1 and coords[1]<=y2):
        validClick = True
    else:
        validClick = False
        
    return validClick
    #values returned from the function

def processKey(b1,b2,spit1,spit2,t1,t2,win):
##    This funtion is a little over 50 lines but there was no way
##    to add an additional funtion without makeing the program confusing
##    b1 is the list of cards from player 1
##    b2 is the list of cards from player 1
##    spit1 is the card drawn from the G pile
##    spit2 is the card drawn from the H pile
##    DrawList is only there to be used when undrawing and moving objects
##    index is a variable used to assist undrawing and moving


##   checks to see if the list carrd list is empty
##    then checks to see if the card values add up 
    validity = False
    card = None
    pile = ''
    key = win.checkKey()
    while key == '':
        key = win.checkKey()
    
    if key == 'z':
    
       if b1[0] == []:
           validity == False
       else:
           validity,pile = checkValid(b1[0][0].value,spit1[0].value, spit2[0].value)
       if validity == True:
           #return the list, so that the spit funtion will take the card from the top of the pile
           card = b1[0]
           
    if key == 'x':
        if b1[1] == []:
           validity == False          
        else:
            validity,pile = checkValid(b1[1][0].value,spit1[0].value, spit2[0].value)
        if validity == True:
           
           card = b1[1]           
    if key == 'c':
        if b1[2] == []:
           validity == False
        else:
            validity,pile = checkValid(b1[2][0].value,spit1[0].value, spit2[0].value)
        if validity == True:
           card = b1[2]
           
    if key == 'b':
        if b2[2] == []:
           validity == False
        else:
            validity,pile = checkValid(b2[2][0].value,spit1[0].value, spit2[0].value)
        if validity == True:
           
           card = b2[2]
    if key == 'n':
        if b2[1] == []:
           validity == False
        else:
            validity,pile = checkValid(b2[1][0].value,spit1[0].value, spit2[0].value)
        if validity == True:
           
           card = b2[1]
    if key == 'm':
        if b2[0] == []:
           validity == False
        else:
            validity,pile = checkValid(b2[0][0].value,spit1[0].value, spit2[0].value)
        if validity == True:
           
           card = b2[0]
           
    if key == 'space':
        if (len(t1) > 0) and ((len(t2))>0):
            spit1.insert(0,t1[0])
            t1.remove(t1[0])
            spit1card = Image(spitCard1,spit1[0].img).draw(win)
        
            spit2.insert(0,t2[0])
            t2.remove(t2[0])
            spit2card = Image(spitCard2,spit2[0].img).draw(win)
            validity == True

    return validity, card, pile
    

def gameSetUp(win):
    #draws all the objects
    title = Text(Point(50,70),"SPIT")
    title.setFace("courier")
    title.setSize(36)
    title.setStyle("bold")
    title.draw(win)
    plyr1nametxt = Text(Point(25,55),"Player 1:").draw(win)
    plyr1box = Entry(Point(25, 50),10).draw(win)
    plyr2nametxt = Text(Point(75,55),"Player 2:").draw(win)
    plyr2box = Entry(Point(75,50),10).draw(win)
    startButton = Rectangle(Point(30,40),Point(70,60,))
    startButton.setFill('red')
    startButton.draw(win)
    startText = Text(Point(50,50),"START")
    startText.setFace("arial")
    startText.setSize(25)
    startText.setStyle("bold")
    startText.draw(win)
    
    #checks for a click
    startButtonClick = processClick(30,70,40,60,win)
    
    #keeps checking for click
    while startButtonClick == False:
        startButtonClick = processClick(30,70,40,60,win)
    while startButtonClick == True:
        #gets player names
        player1name = plyr1box.getText()
        player2name = plyr2box.getText()
        
        #if no input was given, sets default
        if player1name.replace(' ','') == "":
            player1name = "Player 1"
        if player2name.replace(' ','') == "":
            player2name = "Player 2"
        
        #undraws all the items
        plyr1nametxt.undraw()
        plyr1box.undraw()
        plyr2nametxt.undraw()
        plyr2box.undraw()
        startButton.undraw()
        startText.undraw()
        title.undraw()
        #breaks the loop
        break
    return player1name, player2name



def readyUp(win):
    #load Images
    plyr1status,plyr2status = "notready","notready"
    backdrop = Image(Point(50,50),"eh.gif").draw(win)
    plyr1img = Image(Point(25.94166,50),"notReady.gif").draw(win)
    plyr2img = Image(Point(77.18333,50),"notReady.gif").draw(win)
    ready = win.checkKey()
    while ready == '':
        ready = win.checkKey()
        
        #checks to see if the players have readied up or not
        if ready == 'q':
            plyr1img.undraw()
            time.sleep(.05)
            plyr1img = Image(Point(25.94166,50),"ready.gif").draw(win)
            plyr1status = "ready"
        if ready == 'p':
            plyr2img.undraw()
            time.sleep(.05)
            plyr2img = Image(Point(77.18333,50),"ready.gif").draw(win)
            plyr2status = "ready"
##        checks key input again
        ready = win.checkKey()
        
        if plyr1status == "ready" and plyr2status == "ready":
            break
    
    startText = Text(Point(50,25),"Starting In...").draw(win)
##    coutdown by 3
    three = Text(Point(50,23),"3").draw(win)
    time.sleep(1)
    three.undraw()
    two = Text(Point(50,23),"2").draw(win)
    time.sleep(1)
    two.undraw()
    one = Text(Point(50,23),"1").draw(win)
    time.sleep(1)
    #undraws everything 
    one.undraw()
    startText.undraw()
    backdrop.undraw()
    plyr1img.undraw()
    plyr2img.undraw()
    
    
                

class Player:
    
        self.name = name
        self.deck = deck
        
        def getName(self):
            name = self.name
            return name

class Cards:
    
    def __init__(self,suit,value,img,position=None):
        self.suit= suit
        self.value = value
        self.img = img
        #self. position is the image of the card being drawnn
        self.pos = position
        
    def getPos(self):
        #returns the string of the position
        #to be used when searching the glossary when moving cards
        position = (self.pos)
        return position
        
    def display(self):

        print("{0:} of {1:}".format(self.value,self.suit))
        
def changePos(self,newPos):
##        changes the image being drawn
        self.pos = newPos
        return self

def establishDeck():
    #makes the deck and assigns each outside imaege to an objeect
    deck=[]
    megaList = []
    
    heartlist = ["Aheart.gif","2heart.gif","3heart.gif","4heart.gif","5heart.gif","6heart.gif","7heart.gif"]
    diamondlist = ["Admd.gif","2dmd.gif","3dmd.gif","4dmd.gif","5dmd.gif","6dmd.gif","7dmd.gif"]
    clublist = ["Aclub.gif","2club.gif","3club.gif","4club.gif","5club.gif","6club.gif","7club.gif"]
    spadelist = ["Aspade.gif","2spade.gif","3spade.gif","4spade.gif","5spade.gif","6spade.gif","7spade.gif"]
    
    megaList.append(heartlist)
    megaList.append(diamondlist)
    megaList.append(clublist)
    megaList.append(spadelist)
    
    
    suitIndex = 0
    for i in ("Hearts","Diamonds","Clubs","Spades"):
        for j in range(0,7):
            card = Cards(i,(j+1),megaList[suitIndex][j])
            deck.append(card)
        suitIndex += 1

    return deck
        
def shuffle(deck):
    #shuffles the deck
    for i in range(27,0,-1):
#        right here ^ is the # of cards - 1
       r = randrange(0,28)
       deck[i],deck[r] = deck[r],deck[i]
       s = randrange(0,28)
       deck[r],deck[s] = deck[s],deck[r]
    return deck
       
def deal(deck):
    player1deck = []
    player2deck = []
    #this takes every other card and gives it to each player
    for i in range (0,28,2):
        player1deck.append(deck[i])
    for i in range (1,28,2):
        player2deck.append(deck[i])       
    return player1deck, player2deck

def seperate(one,two):
    #the first letter signifies the placement, the first digit signifies player#
    #the second digit signifies which deck
    B1 = []
    b11 = []
    b12 = []
    b13 = []
    
    B2 = []
    b21 = []
    b22 = []
    b23 = []
    
    #appends the correct numebr of cards to each deck
    for i in range(len(one)):
        if i == 0:
            b11.append(one[i])
        elif i == 1 or i == 2:
            b12.append(one[i])
        elif i > 2 and i < 6:
            b13.append(one[i])
    for i in range(len(two)):
        if i == 0:
            b21.append(two[i])
        elif i == 1 or i == 2:
            b22.append(two[i])
        elif i > 2 and i < 6:
            b23.append(two[i])
            
    B1 = [b11,b12,b13]
    B2 = [b21,b22,b23]
    return B1,B2

def setUpStacks(one, two):
    bottomOne = []
    bottomTwo = []
    lenOne = len(one)
    lenTwo = len(two)
    #Takes the first 6 cards from the player decks and stores them in a seperate pile
    #this is the bottom deck: the playable cards
    #removes the cards that were taken from the deck immediatley after
    i = 0
    if lenOne > 6:
        for i in range(0,6):
            
            bottomOne.append(one[0])
            one.remove(one[0])
            
    else:
        for i in range(0,lenOne):
            bottomOne.append(one[0])
            one.remove(one[0])
    i = 0
    if lenTwo > 6:
        for i in range(0,6):
            bottomTwo.append(two[0])
            two.remove(two[0])
    else:
        for i in range(0,lenTwo):
            bottomTwo.append(two[0])
            two.remove(two[0])
    #Stores the rest of the cards in a different pile
    #this is the spit pile for each player
    pileOne = one
    pileTwo = two
    #-------------------------
#sets up the key piles
    #Lists for key Piles
    bottomOne, bottomTwo = seperate(bottomOne,bottomTwo)
    
    return bottomOne, bottomTwo, pileOne, pileTwo

def showCard1(bottom,t1,win):
    #bottom Cards
    #draws each card on the player 1 side
    drawList = []
    length = len(bottom[0])
    if length != 0:
        Z = Image(Point(9,4.5),"ZKey.gif").draw(win)
        b11 = Image(zCard,bottom[0][0].img)
        drawList.append(b11)
        bottom[0][0] = changePos(bottom[0][0],b11)
        
        
    length = len(bottom[1])
    if length != 0:
        X = Image(Point(19,4.5), "XKey.gif").draw(win)
        b121 = Image(xCard,bottom[1][0].img)
        drawList.append(b121)
        bottom[1][0] = changePos(bottom[1][0],b121)
        length -= 1
        
    if length != 0:
        b122 = Image(xCard2,bottom[1][1].img)
        drawList.append(b122)
        bottom[1][1] = changePos(bottom[1][1],b122)
               
    length = len(bottom[2])
    if length != 0:
        C = Image(Point(29,4.5), "CKey.gif").draw(win)
        b131 = Image(cCard,bottom[2][0].img)
        drawList.append(b131)
        bottom[2][0] = changePos(bottom[2][0],b131)
        length -= 1
    if length != 0:
        b132 = Image(cCard2,bottom[2][1].img)
        drawList.append(b132)
        bottom[2][1] = changePos(bottom[2][1],b132)
        length -= 1
    if length != 0:
        b133 = Image(cCard3,bottom[2][2].img)
        bottom[2][2] = changePos(bottom[2][2],b133)
        drawList.append(b133)

    drawCards(drawList,win)

    #top cards
    #if there is no cards in the pile, they dont draw
    if not (len(t1) == 0):
        G = Image(Point(30,54.5),"GKey.gif").draw(win)
        gPile = Image(gCard,"backSide.gif").draw(win)
    
    
    return drawList

def showCard2(bottom,top,win):
    #bottom Cards
    #draws each card on the player 2 side 
    drawList = []
    length = len(bottom[0])
    if length != 0:
        Z = Image(Point(91,4.5),"MKey.gif").draw(win)
        b11 = Image(mCard,bottom[0][0].img)
        drawList.append(b11)
        bottom[0][0] = changePos(bottom[0][0],b11)
        
        
    length = len(bottom[1])
    if length != 0:
        X = Image(Point(81,4.5), "NKey.gif").draw(win)
        b121 = Image(nCard,bottom[1][0].img)
        drawList.append(b121)
        bottom[1][0] = changePos(bottom[1][0],b121)
        length -= 1
        
    if length != 0:
        b122 = Image(nCard2,bottom[1][1].img)
        drawList.append(b122)
        bottom[1][1] = changePos(bottom[1][1],b122)
               
    length = len(bottom[2])
    if length != 0:
        C = Image(Point(71,4.5), "BKey.gif").draw(win)
        b131 = Image(bCard,bottom[2][0].img)
        drawList.append(b131)
        bottom[2][0] = changePos(bottom[2][0],b131)
        length -= 1
    if length != 0:
        b132 = Image(bCard2,bottom[2][1].img)
        drawList.append(b132)
        bottom[2][1] = changePos(bottom[2][1],b132)
        length -= 1
    if length != 0:
        b133 = Image(bCard3,bottom[2][2].img)
        bottom[2][2] = changePos(bottom[2][2],b133)
        drawList.append(b133)

    drawCards(drawList,win)

    #top cards
    #if there is no cards in the pile, they dont draw
    
    if not (len(top) == 0):
        H = Image(Point(70,54.5),"HKey.gif").draw(win)
        hPile = Image(hCard,"backSide.gif").draw(win)
        
    return drawList
        
def drawCards(drawList, win):
    #draws the cards in the window
    length = len(drawList)
    for i in range(length-1,-1,-1):
        drawList[i].draw(win)
        

    
def begin(t1,t2,win):
    #establishes spit piles
    spit1 = []
    spit2 = []
    
    #takes card from top of pile and puts it into spit pile
    spit1.insert(0,t1[0])
    t1.remove(t1[0])
    spit1card = Image(spitCard1,spit1[0].img).draw(win)
    
    spit2.insert(0,t2[0])
    t2.remove(t2[0])
    spit2card = Image(spitCard2,spit2[0].img).draw(win)
    
    return spit1, spit2
    
def checkValid(bottomVal,valG, valH):
    #checks to see if the move is valid
    validity = False
    returnPile = ''
    #checks to see if the card is a 7 or Ace
    #if so, it checks to see if the move is valid
    if bottomVal == 7:
        if valG == 6 or valG == 1:
            validity = True
            returnPile = 'G'
        if valH == 6 or valH == 1:
            validity = True
            returnPile = 'H'
    if bottomVal == 1:
        if valG == 7 or valG == 2:
            validity = True
            returnPile = 'G'
        if valH == 7 or valH == 2:
            validity = True
            returnPile = 'H'
    #disregarding the specifity of the number
    #checks to see if the move was valiid
    else:
        if bottomVal == (valG + 1) or bottomVal == (valG - 1):
            validity = True
            returnPile = 'G'
        if bottomVal == (valH + 1)  or bottomVal == (valH - 1):
            validity = True
            returnPile = 'H'
        
    return validity, returnPile
                        

def spit(card, s1, s2, pile,win):
    #moves the card frrom the bottom pile to the middle
    #also moves the image on the window
    
    if pile == 'G':
        s1.insert(0,card[0])
        move(card[0],pile,win)
        card.remove(card[0])
        
        
    if pile == 'H':
        s2.insert(0,card[0])
        move(card[0],pile,win)
        card.remove(card[0])
        
    
        
    return card, s1, s2
        
def move(card, pile,win):
    #moves the image to the correct pile
    if pile == 'G':
        newSpitCard = Image(spitCard1,(card.img)).draw(win)
        
    if pile == 'H':
        newSpitCard = Image(spitCard2,(card.img)).draw(win)
        
def gameStats(Player1,Player2,moves,file):
    #output file info
    outFile= open(file, 'w')
    print("GAME STATS",file=outFile)
    print("\n{0:^20}|{1:^20}|{2:^4}".format("PLAYER 1","PLAYER 2","MOVES"),file=outFile)
    print("\n{0:^20}|{1:^20}|{2:^4}".format(Player1.getName(),Player2.getName(),moves),file=outFile)
    
    
        
def over(Player,win):
    #closes the window
    
    over = Text(Point(50,80), "GAME OVER")
    over.setFace("arial")
    over.setSize(30)
    over.setStyle("bold")
    over.draw(win)
    
    winner = Text(Point(50,60),(Player.getName())+ " WINS!")
    winner.setFace("arial")
    winner.setSize(30)
    winner.setStyle("bold")
    winner.draw(win)
    
    suggest = Text(Point(50,20), "CLICK TO CLOSE WINDOW")
    suggest.setFace("arial")
    suggest.setSize(30)
    suggest.setStyle("bold")
    suggest.draw(win)
    
    win.getMouse()
    win.close()
    
    

def main():
    
    win = setUpWindow()
    player1name, player2name = gameSetUp(win)
    deck = establishDeck() 
    shuffled = shuffle(deck)
    player1deck, player2deck = deal(shuffled)
    
    Player1 = Player(player1name, player1deck)
    Player2 = Player(player2name, player2deck)
    
    #displays the instructions before game
    displayInstructions("instructions.txt",win)          
    totalMoves = 0
    b1,b2,t1,t2 = setUpStacks(player1deck,player2deck)
        
    readyUp(win)
    spit1, spit2 = begin(t1,t2,win)
        
    while (b1 != [[], [], []]) or (b2 != [[], [], []]):
        
        
        showCard1(b1,t1,win)
        showCard2(b2,t2,win)
        
        validity,chosenCard,pile = processKey(b1,b2,spit1,spit2,t1,t2,win)
        #undraws and redraws every keypress
        if validity == True:
            for i in range(3):
                for j in range(len(b1[i])):
                    b1[i][j].getPos().undraw()
                for j in range(len(b2[i])):
                    b2[i][j].getPos().undraw()
            chosenCard,spit1,spit2= spit(chosenCard,spit1,spit2,pile,win)
            totalMoves += 1
        else:
            for i in range(3):
                for j in range(len(b1[i])):
                    b1[i][j].getPos().undraw()
                for j in range(len(b2[i])):
                    b2[i][j].getPos().undraw()
        #double checks to break the loop
        if b1 == [[], [], []] or b2 ==[[], [], []]:
            break
        
   

        
    #finishes up the game
    #writes game stats in a outfile
    #asks user to close window
    newBackdrop(win)
    gameStats(Player1,Player2,totalMoves,"stats.txt")
    if b1 == [[], [], []]:
        over(Player1,win)
    else:
        over(Player2,win)
    
    

    
main()

