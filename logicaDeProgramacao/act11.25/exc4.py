from graphics import *

win = GraphWin("Calculadora", 400, 300)

tn1 = Text(Point(60, 20), "Número-1:")
tn1.setOutline("blue")
tn1.setSize(14)
tn1.draw(win)

tn2 = Text(Point(60, 60), "Número-2:")
tn2.setOutline("blue")
tn2.setSize(14)
tn2.draw(win)

in1 = Entry(Point(150, 20), 5)
in1.setFill(color_rgb(230, 255, 230))
in1.setSize(16)
in1.draw(win)

in2 = Entry(Point(150, 60), 5)
in2.setFill(color_rgb(230, 255, 230))
in2.setSize(16)
in2.draw(win)

ficar = True
while ficar:
   ponto = win.getMouse()
   if ponto.getX() > 250:
       ficar = False
   else:
       n1 = int(in1.getText())
       n2 = int(in2.getText())
       soma = n1 + n2
       sub = n1 - n2
       mult = n1 * n2
       divi = n1 / n2

       tSoma = Text(Point(200, 120), "{} + {} = {}".format(n1, n2, soma))
       tSoma.setOutline("blue")
       tSoma.setSize(16)
       tSoma.draw(win)

       tSub = Text(Point(200, 160), "{} - {} = {}".format(n1, n2, sub))
       tSub.setOutline("blue")
       tSub.setSize(16)
       tSub.draw(win)

       tMult = Text(Point(200, 200), "{} x {} = {}".format(n1, n2, mult))
       tMult.setOutline("blue")
       tMult.setSize(16)
       tMult.draw(win)

       tDivi = Text(Point(200, 240), "{} / {} = {}".format(n1, n2, divi))
       tDivi.setOutline("blue")
       tDivi.setSize(16)
       tDivi.draw(win)

win.getMouse()
win.close()
