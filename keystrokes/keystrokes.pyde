  
# Run this program to learn how each of these functions
# relate to the others.


def draw():  # Empty draw() needed to keep the program running
    pass


def keyPressed():
    print("pressed %s %d" % (key, keyCode))


def keyTyped():
    print("typed %s %d" % (key, keyCode))


def keyReleased():
    print("released %s %d" % (key, keyCode))
