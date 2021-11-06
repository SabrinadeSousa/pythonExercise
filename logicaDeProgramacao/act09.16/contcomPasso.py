'''
Faça um programa que receba int(input()) três números positivos
(faça as validações): número inicial, número final e passo.
O número final deve ser maior que o número inicial (if), pois deve ser uma contagem crescente.
Após receber estes números o programa deve imprimir a contagem do número inicial até o número
final e a cada iteração deve acrescentar o passo.
Usar int(input(“Mensagem?”)) para fazer as entradas de dados.
'''

#Criando função para validar se é um número inteiro.
def leiaInt(msg):
   ok = False
   valor = 0
   while True:
       n = str(input(msg))
       if n.isnumeric():
           valor = int(n)
           ok = True
       else:
           print("\033[0;31mERRO! Digite apenas números inteiros.\033[m")
       if ok:
           break
   return valor

#Programa principal

nI = leiaInt("Digite número inicial: ")
nF = leiaInt("Digite número final: ")
nP = leiaInt("Digite número para o passo: ")

#Saida de Dados.
num = (list(range(nI, nF, nP)))
for conte in num:
   print(conte)
