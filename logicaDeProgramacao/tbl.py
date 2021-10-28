
def escrever(tabuada):

    arquivo = open("tabuada.txt", "w+")
    nt = int(input("Digite um número: "))
    numeros = range(11)
    for num in numeros:
        arquivo.write(str("{} x {} = {}".format(nt, num, nt * num)))
        arquivo.write("\n")
        print("{} x {} = {}".format(nt, num, nt * num))


"""def atualizar():
    arquivo = open('tabuada.txt', 'a')
    arquivo.write()
    arquivo.close()


def ler():
    arquivo = open('tabuada.txt', 'r')
    arquivo.read()
    arquivo.close()


if __name__ == '__main__':
    atualizar()"""