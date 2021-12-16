from graphics import *
win = GraphWin("Um polígono", 300, 300)
p = Polygon(Point(100,100), Point(150,120), Point(160,160), Point(190,210))
p.setOutline("blue")
p.setFill("violet")
p.draw(win)

win.getMouse()
win.close()