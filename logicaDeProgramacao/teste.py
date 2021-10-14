print("A seguir iremos aplicar a Cifra de César sobre um texto com deslocamento de 2 casas")
print("Informe uma frase:")
frase = input()
if (frase == ''):
    print("Informe uma frase por favor")
else:
    cesar = ""
    for car in frase:
        cesar += chr(ord(car) - 1)

    part1= ""
    part2= ""
    
    metade = len(cesar) // 2
    for ind in range(0, metade):
        sr += cesar[ind] + cesar[len(cesar) - ind - 1]

    if (len(cesar) % 2) == 1:
        sr += cesar[ind + 1]

    print("A frase Descifrada é")
    print(sr)