'''
Faça um programa que desenhe um túnel fictício (da mesma forma que foi feito para o túnel de círculos),
porém que seja feito de quadrados em uma janela.
'''

from graphics import *

janela = GraphWin("Túnel Quadrado...", 400, 400)

for posicao in range(50, 325, 3):
   quadrado = Rectangle(Point(posicao -40, posicao -40), Point(posicao +40, posicao +40))
   quadrado.setOutline(color_rgb(0, 50, 255))
   quadrado.draw(janela)

janela.getMouse()
janela.close()












