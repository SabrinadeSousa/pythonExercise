from graphics import GraphWin, Oval, Point, Circle

win = GraphWin("Um oval", 300,300)

c = Oval(Point(100,10),Point(200,110))
c.setOutline("red")
c.setFill("orange")
c.draw(win)

o = Oval(Point(100, 120), Point(200,180))
o.setOutline("red")
o.setFill("orange")
o.draw(win)

win.getMouse()
win.close()