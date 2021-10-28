arquivo = open("tabuada.txt", "w+")
nt = int(input("Digite um número: "))
numeros = range(11)
for num in numeros:
   arquivo.write(str("{} x {} = {}".format(nt, num, nt * num)))
   arquivo.write("\n")
   print("{} x {} = {}".format(nt, num, nt * num))