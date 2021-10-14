

#Assim ela fica um triangulo mais perfeito.
for num in range(65, 91):
      numEsp = (26 * 3) - ((num - 64) * 3)
      numEsp //= 2
      print((' ' * numEsp), ((' ' + chr(num) + ' ')*(num - 64)))


