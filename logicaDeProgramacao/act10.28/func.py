#Primeira parte.
class Funcoes:

    def recnum(self, msg, numIni, numFim):
        valor = numIni - 1
        while (valor < numIni) or (valor > numFim):
            valor = int(input(msg + ' '))
        return valor

    def texto(self, msg, minimo):
        numCar = minimo - 1
        while numCar < minimo:
            txt = input(msg + ' ')
            numCar = len(txt)
        return txt







