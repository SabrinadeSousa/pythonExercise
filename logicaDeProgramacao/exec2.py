#Faça um programa para imprimir todo o alfabeto usando repetição (for)

numRep=1
for num in range(49, 58):
   for repete in range(0, numRep):
       print(chr(num), end="")
   print()
   numRep+=1

