frs = input('Digite uma frase: ')
metade = len(frs) // 2
ultimo = len(frs) - 1
for ini in range(0, metade, 1):
   fim = ultimo - ini
   print(frs[fim] + frs[ini], end='')

if (len(frs) % 2) == 1:
   print(frs[metade])
