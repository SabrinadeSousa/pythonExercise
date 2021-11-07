from graphics import *

janela = GraphWin("Pontos ...", 600, 400)

# Desenhando pontos método-1 (quatro pixels)
ponto = Point(100, 100)
ponto.setFill("Blue")
ponto.draw(janela)

# Desenhando pontos método-2 (um pixel)

janela.plot(200,200,"black")

# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()
