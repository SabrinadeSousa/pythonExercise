'''
Faça um programa que desenhe três quadrados pintados por completo de Verde, Amarelo e Azul
e que sejam perfeitamente distribuídos em uma linha horizontal fictícia no meio da janela (metade).
Cada quadrado deve ter tamanho de 50 pixels de lado.
O tamanho da janela deve ser 600 x 600.
'''

from graphics import *

janela = GraphWin("Quadrados ...", 600, 600)

# Desenhando Quadrados
rect = Rectangle(Point(260, 325), Point(210, 275))
rect.setFill("green")
rect.draw(janela)

rect1 = Rectangle(Point(275, 325), Point(325, 275))
rect1.setFill("yellow")
rect1.draw(janela)
rect2 = Rectangle(Point(340, 325), Point(390, 275))
rect2.setFill("blue")
rect2.draw(janela)

# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()

