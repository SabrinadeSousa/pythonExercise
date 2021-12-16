'''
Faça um programa que desenhe sempre a partir do centro da janela
66 círculos que tenham raio de 3 até 198 pixels (3, 6, 9, 12, …, 198), pulando de 3 em 3.
 A janela deve ter tamanho 600 x 600.
 '''

from graphics import *

janela = GraphWin("Circulos diversos...", 600,600)
x = 3
y = 198
for i in range(0, 67):
   circle = Circle(Point(300, 300), x)
   circle.draw(janela)
   x+= 3

# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()



