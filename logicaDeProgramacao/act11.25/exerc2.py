#Função para criar losango:


from graphics import *
import time
import random

def losango(pse, pid, corLinha, corPreenche, jan):
   p1 = Point((pid.getX()+pse.getX())/2, pse.getY())
   p2 = Point(pid.getX(), (pid.getY()+pse.getY())/2)
   p3 = Point((pid.getX()+pse.getX())/2, pid.getY())
   p4 = Point(pse.getX(), (pid.getY()+pse.getY())/2)
   p = Polygon(p1, p2, p3, p4)
   p.setOutline(corLinha)
   p.setFill(corPreenche)
   p.draw(jan)


win = GraphWin("Vários losangos", 600, 600)
for i in range(500):
   col1 = random.randrange(0, 300)
   lin1 = random.randrange(0, 300)
   col2 = random.randrange(300, 600)
   lin2 = random.randrange(300, 600)
   cLinha = color_rgb(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
   cPreenche = color_rgb(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
   losango(Point(col1, lin1), Point(col2, lin2), cLinha, cPreenche, win)
   time.sleep(.2)

win.getMouse()
win.close()




