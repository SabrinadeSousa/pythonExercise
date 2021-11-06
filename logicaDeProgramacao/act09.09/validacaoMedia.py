'''
Crie um programa que receba três notas de 0 até 10 (faça as validações para aceitar apenas esse intervalo)
depois faça o cálculo da média aritmética e então mostre a média calculada e também se o aluno passou ou não.
A escola aceita notas 7 (sete) acima para aprovação.
Atenção para a indentação do código (inclusive na entrega dos exercícios)
'''

#Declaração de Variaveis.
#Entrada de Dados com verificação de valores apenas de 0 há 10.
nota1 = float(input("Digite a primeira nota: "))
while nota1:
   if nota1 < 0 or nota1 > 10:
       print("Digite apenas valores de 0 há 10!")
       nota1 = float(input("Digite a primeira nota: "))
   else:
       break

nota2 = float(input("Digite a segunda nota: "))
while nota2:
   if nota2 < 0 or nota2 > 10:
       print("Digite apenas valores de 0 há 10!")
       nota2 = float(input("Digite a segunda nota: "))
   else:
       break

nota3 = float(input("Digite a terceira nota: "))
while nota3:
   if nota3 < 0 or nota3 > 10:
       print("Digite apenas valores de 0 há 10!")
       nota3 = float(input("Digite a terceira nota: "))
   else:
       break

#Processamento de Dados.
media = (nota1 + nota2 + nota3)/ 3
decisao = media >= 5

#Saida de Dados.
if media >= 5:
   print("Parabéns aprovado!: {:.1f}".format(media), decisao)
else:
   print("Aluno(a): reprovado ficou abaixo da média, sua média foi"
         " {:.1f} mas não desanime estude um pouco mais!".format(media))
