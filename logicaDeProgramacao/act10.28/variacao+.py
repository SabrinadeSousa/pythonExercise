#Utilizando o programa do quadrado faça uma variação do programa para imprimir o caractere “+”
#nas diagonais principal e secundária.

lado=int(input("Quantos caracteres no lado do quadrado [10-100]? "))
if lado<10 or lado>100:
    print ("Informe um número entre 1 e 100!")
else:
  for linha in range(1, lado+1):
      print()
      for coluna in range(1, lado+1):
          if linha == coluna or linha + coluna == lado +1:
              print(" + ", end="")
          else:
              print(" 0 ", end="")

