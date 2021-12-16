'''
Crie um programa que faça uma GRID na janela de pequenos quadrados, onde o lado varie de 3 à 9 pixels,
 a sua escolha, e que sejam pintados um de Azul e outro Vermelho, preenchendo toda a extensão da tela.
'''

from graphics import *

janela = GraphWin("GRID ...", 400, 400)
janela.setBackground(color_rgb(240, 240, 255))

azul = True
for col in range(0, 400, 9):
   for lin in range(0, 400, 9):
       quadrado = Rectangle(Point(col, lin), Point(col+10, lin+10))

       if azul:
           quadrado.setFill("blue")
           azul = False
       else:
           quadrado.setFill("red")
           azul = True
       quadrado.draw(janela)

janela.getMouse()




