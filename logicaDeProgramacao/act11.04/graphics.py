from graphics import *

janela = GraphWin("Fazer uma GRID ...", 300, 300)

for col in range(0, 300, 1):
   for lin in range(0, 300, 10):
       janela.plot(col, lin, 'green')

for lin in range(0, 300, 1):
   for col in range(0, 300, 10):
       janela.plot(col, lin, 'green')


janela.getMouse()
janela.close()


