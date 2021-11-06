#Primeiro padrão:
# ABC -> ABBCCC
# 12345 -> 122333444455555
# PYTHON -> PYYTTTHHHHOOOOONNNNNN
#Entrada de dados.
texto = input('Digite algo: ')
tam = len(texto)
ind = 0
#processamento e saida de dados.
while ind < tam:
   rep = ind + 1
   num = 0
   while num < rep:
       print(texto[ind], end='')
       num += 1
   ind += 1

