#Faça um programa que receba três números (inteiros) e depois imprima uma saída com os números em ordem crescente.

n1= int(input("Digite um numero: "))
n2= int(input("Digite outro numero: "))
n3= int(input("Outro numero: "))

num = n1+n2+n3

listN = [n1, n2, n3]
listN.sort()
print(listN)
