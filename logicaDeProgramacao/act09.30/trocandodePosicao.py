'''
 ABCDEF -> FAEBDC
# 1234567890 -> 0192837465
# PYTHON -> NPOYHT
# Carlos -> sCoalr
# 1234567 -> 7162534
# VXYWZ -> ZVWXY
último/primeiro, penúltimo/segundo, antepenúltimo/terceiro, …
Par ou ímpar:
len(s) % 2 == 0 (par)
len(s) % 2 == 1 (ímpar)
'''

frs = input('Digite uma frase: ')
metade = len(frs) // 2
ultimo = len(frs) - 1
for ini in range(0, metade, 1):
  fim = ultimo - ini
  print(frs[fim] + frs[ini], end='')

if (len(frs) % 2) == 1:
  print(frs[metade])



