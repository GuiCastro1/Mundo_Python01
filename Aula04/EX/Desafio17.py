'''
Criado por : Gui Castro

16/01/2025

Crie um programa que leia um numero real qualquer pelo teclado e mostre na  tela sua porção inteira
'''

from math import trunc , ceil , floor

num = float(input('Digite um número '))

print(f'O número sem casas decimais é : {trunc(num)}')

print(f'O número sem casas decimais é: {int(num)}')

print(f'O número sem casas decimais é : {floor(num)}')

# print(f'O número sem casas decimais é : {ceil(num)}')  ele arredonda para cima 