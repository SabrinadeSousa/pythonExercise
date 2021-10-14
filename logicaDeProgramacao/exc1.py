'''
Faça um programa para imprimir todo o alfabeto uma
letra por linha e em cada linha deve ter 10 letras
repetidas com utilização da repetição (for)
'''

for alfa in range(65, 91):
    for letra in range(65, 91):
        letra = (chr(letra)*10)
        print(letra)
    break



