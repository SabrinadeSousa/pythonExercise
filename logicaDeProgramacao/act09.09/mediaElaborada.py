''''
Crie um programa que receba duas notas e informe se a pessoa passou ou não.
Considere que o usuário irá informar uma nota de 0 à 10 e que média a partir de 5 leva o aluno a aprovação
Exemplo:
(5 + 7)  / 2 = 6 Aprovado: True (ou seja está aprovado)
(4 + 3) / 2 = 3.5 Aprovado: False (ou seja está reprovado)
'''

#Declaração de Variaveis.
#Entrada de Dados.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

#Processamento de Dados.
media = (nota1 + nota2)/ 2

#Saida de Dados.
if media >= 5:
   print("Parabéns aprovado!: {:.1f}".format(media))
else:
   print("Aluno(a): reprovado ficou abaixo da média, sua média foi"
         " {:.1f} mas não desanime estude um pouco mais!".format(media))
