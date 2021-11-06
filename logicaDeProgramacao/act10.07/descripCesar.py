'''
Faça um programa para descriptografar uma frase criptografada com a cifra de César
com deslocamento de 2 (duas) casas, ou seja, um programa que faça a decodificação
daquilo gerado pelo exemplo do tutorial.
'''
print("A seguir iremos aplicar a Cifra de César sobre um texto com deslocamento de 2 casas")
print("Informe uma frase:")
frase = input()
if (len(frase)==0):
   print ("Informe uma frase por favor")
else:
   cesar=""
   for ind in range(0, len(frase)):
       codigo=ord(frase[ind])
       codigo+=-2
       novoCaracter=chr(codigo)
       cesar+=novoCaracter
   print("A frase decifrada é")
   print(cesar)