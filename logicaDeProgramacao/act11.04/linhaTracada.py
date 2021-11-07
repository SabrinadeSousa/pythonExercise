'''
Faça um programa que mostre duas linhas. Estas linhas devem fazer o traço de duas diagonais:
a principal e a secundária na extensão máxima visível da janela em questão.
(Enfim, é o mesmo de fazer um X na janela).
A janela deve ser “quadrada”, Utilize: 600 x 600 pixels(colunas x linhas).
'''

from graphics import *

janela = GraphWin("Linhas x Coluna...", 600, 600)

# Desenhando linhas
linha = Line(Point(0, 600), Point(600, 0))
linha.setFill("black")
linha.draw(janela)

coluna = Line(Point(600, 600), Point(0, 0))
coluna.setFill("black")
coluna.draw(janela)

# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()









