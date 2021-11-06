'''
Crie uma variação do programa anterior, porém com os seguintes requisitos adicionais:
Calcule uma média ponderada: Peso da Nota 1 é 1, Peso da Nota 2 é 1.5 e Peso da Nota 3 é 2.
Ao invés de mostrar se o aluno foi aprovado ou não com base na média ponderada mostre uma
menção de SR, II, MI, MM, MS ou SS, conforme a média ponderada e usando a escala:
'''

#ENTRADA DE DADOS.
nota1 = float(input("Primeira Nota: "))
nota2 = float(input("Segunda Nota: "))
nota3 = float(input("terceira Nota: "))

#Declaração do valores dos pesos.
pn1 = 1
pn2 = 1.5
pn3 = 2

#PROCESSAMENTO DE DADOS.
mediaTotal = (pn1 * nota1 + pn2 * nota2 + pn3 * nota3)/4.5

print("-"*18)
#SAIDA DE DADOS.
print("Sua média é: {:.1f}".format(mediaTotal))

while mediaTotal:
   if mediaTotal == 0:
       print("SR")
   elif mediaTotal < 2:
       print("II")
   elif mediaTotal < 5:
       print("MI")
   elif mediaTotal < 7:
       print("MM")
   elif mediaTotal < 9:
       print("MS")
   else:
       print("SS")
   break
print("-"*18)


