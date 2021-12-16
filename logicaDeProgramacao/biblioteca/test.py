from graphics import *
from logicaDeProgramacao.biblioteca.desenhos import Formas

jan = GraphWin("Formas", 600, 400)

fig = Formas()
fig.triangulo(Point(250, 50), Point(350, 150), "red", "blue", jan)
fig.losango(Point(250, 250), Point(350, 350), "red", "pink", jan)


jan.getMouse()
jan.close()


