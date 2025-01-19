'''
Criado por : Gui Castro

17/01/2025

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados 

EX:1980

unidade 0
dezena 8
centena 9
milhar 1
'''

numero = (input('Digite um número de 0 a 9999:'))
n = int(input('Digite um número de 0 a 9999:'))

print(f'Unidade:{str(numero[3])}')
print(f'Dezena:{str(numero[2])}')
print(f'Centena:{str(numero[1])}')
print(f'Milhar:{str(numero[0])}')
print("-" * 35)
print(f'Unidade:{n % 10}')
print(f'Dezena:{(n // 10) % 10}')
print(f'Centena:{(n // 100) % 10}')
print(f'Milhar:{n // 1000}')
