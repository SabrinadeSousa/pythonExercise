#Faça um programa que receba um número e gere um arquivo texto
#com a tabuada de multiplicação (0 até 10) do número recebido.

arquivo = open("C:\\temp\\tabuada.txt", "w")
nt = int(input("Digite um número: "))
numeros = range(11)
for num in numeros:
    arquivo.write(str("{} x {} = {}".format(nt, num, nt * num)))
    arquivo.write("\n")
    print("{} x {} = {}".format(nt, num, nt * num))