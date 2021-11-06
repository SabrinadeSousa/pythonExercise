'''
Crie um programa que receba (input) um valor e se esse valor for inferior
a um salário mínimo informe que o salárioestá incorreto (ou fora da legislação)
Exemplo:
Se informar 500 então mostrar:  Salário: False
(Fora da legislação)
Se informar 1500 então mostrar: Salário: True
(Dentro da legislação)
'''


#Declaração de Variaveis/Entrada de Dados.
salarioMinimo = float(input("Informe o seu salário: "))

#processamento de Dados.
if salarioMinimo >= 1100:
   print ("Seu salario está dentro da legislação: R$ {:.2f}".format(salarioMinimo))
else:
   print("Seu salário não esta dentro da legislação: ")

