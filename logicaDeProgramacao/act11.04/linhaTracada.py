'''
Faça um programa que mostre duas linhas. Estas linhas devem fazer o traço de duas diagonais:
a principal e a secundária na extensão máxima visível da janela em questão.
(Enfim, é o mesmo de fazer um X na janela).
A janela deve ser “quadrada”, Utilize: 600 x 600 pixels(colunas x linhas).
'''
import time


from graphics import *
import time

janela = GraphWin("Fazer um X na tela ...", 600, 600)
# Diagonal principal
for linhas in range(600):
   ponto = Line(Point(0, 600), Point(600, 0))
   ponto.setFill("black")
   ponto.draw(janela)
   time.sleep(0.01)

# Diagonal secundaria
for colunas in range(600):
   ponto = Point(colunas, colunas)
   ponto.setFill("red")
   ponto.draw(janela)
   time.sleep(0.01)

# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()


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









