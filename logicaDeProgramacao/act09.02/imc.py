#Faça um programa que receba os parâmetros necessários para a obtenção e impressão do IMC.

#imc = peso / (alt ** 2).

#Entrada de Dados -> peso e altura.
peso = float(input("Qual o seu peso (KG)? "))
altura = float(input("Qual a sua altura (m)? "))

#Processamento de Dados.
altura **= 2
imc=peso
imc/=altura

#Saida de Dados.
print("O seu IMC é:", "%.2f"% imc)

