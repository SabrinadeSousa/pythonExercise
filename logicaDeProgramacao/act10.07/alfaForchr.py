#Faça um programa para imprimir um triângulo com as letras do alfabeto.
#Utilize o for e a função chr.

#vai me o alfabeto em forma de triângulo.

for alfa in range(96, 123):
  for repete in range(0, (alfa - 96)):
      print(chr(alfa), end="")

#esse print vazio vai me da o formato de triângulo.
  print()

#ou

#Assim ela fica um triângulo mais perfeito.

for num in range(65, 91):
     numEsp = (26 * 3) - ((num - 64) * 3)
     numEsp //= 2
     print((' ' * numEsp), ((' ' + chr(num) + ' ')*(num -64)))

