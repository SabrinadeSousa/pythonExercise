'''
Faça um programa que receba o valor do litro da gasolina e valor do litro do álcool na
bomba e informe se é mais vantajoso abastecer com um ou outro combustível.
Utilize a proporção de 70% do valor para o álcool.
'''

# Entrada de dados.
gasolina = float(input("Informe o valor da gasolina: "))
alcool = float(input("Informe o valor do alcool: "))

# processamento de dados.
valor = gasolina * 0.7

# Saida de dados.
if valor > alcool:
    print("A gasolina é mais vantajosa!")
elif valor < alcool:
    print("O alcool é mais vantajoso!")
else:
    print("Não tem diferença! vai qualquer um mesmo")

