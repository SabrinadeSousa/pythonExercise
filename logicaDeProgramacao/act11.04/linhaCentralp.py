'''
Faça um programa que desenhe uma linha reta horizontal no meio da janela,
mas que seja pontilhada,esta deve ir da coluna 0 até a 599.
Sugestão: Utilize o for para isso. Dica: nem toda coluna deve ter um ponto plotado (para ficar pontilhado).
A janela deve ser “quadrada”. Utilize: 600 x 600 pixels (colunas x linhas).
'''

from graphics import *

janela = GraphWin("Pontos ...", 600, 600)

# Desenhando pontos método-2 (um pixel)
for col in range(0, 599, 5):
    janela.plot(col,300,"black")

# Aguardando um clique de mouse para fechar a janela
janela.getMouse()
janela.close()