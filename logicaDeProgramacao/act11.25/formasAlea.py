'''
Exercício: (Para entrega): Crie um programa que de forma aleatória crie polígonos na tela a cada
vez que o usuário teclar alguma coisa, caso o usuário tecle ESC o programa deve fechar a janela.
Os polígonos devem ter vértices e posições aleatórias, assim como as cores que também devem ser sorteadas.
'''
import time

from graphics import *
import random
import time

janela = GraphWin("Outros...", 600, 600)
ficar = True

while ficar:
    tecla = janela.getKey()
    if tecla == "Escape":
        ficar = False
        continue
    else:
        poligono = Polygon(Point(random.randrange(0, 600), random.randrange(0, 600)),
                           Point(random.randrange(0, 600), random.randrange(0, 600)),
                           Point(random.randrange(0, 600), random.randrange(0, 600)),
                           Point(random.randrange(0, 600), random.randrange(0, 600)))

    for i in range(0, random.randrange(0, 18)):
        poligono.points.append(Point(random.randrange(0, 600), random.randrange(0, 600)))
        poligono.setOutline(color_rgb(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        poligono.setFill(color_rgb(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        poligono.draw(janela)

janela.close()


