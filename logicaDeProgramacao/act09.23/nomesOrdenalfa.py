#Faça um programa que receba “n” nomes via console e depois imprima esses nomes em ordem alfabética,
#independente de maiúsculas e minúsculas.

nomes = []
quantidade = int(input('Quantos nomes? '))

for indice in range(quantidade):
   nomes.append(input('Informe o nome-{}: '.format(indice+1)))
for primeiro in range (quantidade-1):
   for segundo in range(primeiro+1, quantidade):
       if nomes[primeiro] > nomes [segundo]:
           aux = nomes[primeiro]
           nomes[primeiro] = nomes[segundo]
           nomes[segundo] = aux
for indice in range (quantidade):
   print(indice+1, '-', nomes[indice])

