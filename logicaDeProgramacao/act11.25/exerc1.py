from graphics import *

win = GraphWin("Um poligono", 300,300)

p= Polygon(Point(150,1), Point(299,150), Point(150,299), Point(1,150))
p.setOutline("blue")
p.setFill("violet")
p.draw(win)

win.getMouse()
win.close()