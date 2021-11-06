#Faça um programa que receba um número de 1 até 99 e
#depois mostre esse número no console escrito por extenso.

num = int(input('Informe um numero de 1 a 99: '))

unidades = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze','dezesseis', 'dezessete', 'dezoito', 'dezenove']

dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

if 0< num < 20:
   print(num, '-', unidades[num-1])
elif 19 < num < 100:
   if(num% 10)==0:
       print(num, '-', dezenas[(num // 10) - 1])
   else:
       print(num,'-', dezenas[(num // 10) -2], 'e', unidades[(num % 10) -1])
else:
       print('Numero Invalido')


