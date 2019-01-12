from buttons import Knop
from names import Names

def setup():
    global knop, names
    size(800,400)
    knop = Knop()
    names= Names()
    

def draw():
    for i in range(3):
        knop.button(100+(i*200),10,40,40)
        names.name("Everknown", 100+(i*200), 50,200,20)
    noLoop()
