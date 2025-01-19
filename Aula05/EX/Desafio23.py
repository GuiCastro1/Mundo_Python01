'''
Criado por : Gui Castro

17/01/2025

Crie um programa que leia o nome de uma pessoa e exiba

O nome com todas as letrs maiusculas 
O nome com todas minusculas 
Quantas letras tem sem considerar os espaços em branco
Quantas letras tem o primeiro nome 
'''

nome = str(input('Digite seu nome completo:'))

quantidade = nome.split()

vazio= nome.count(' ')

print(nome.lower())

print(nome.upper())

print(f'Seu nome possui:{len(nome) - vazio} letra sem considerar os espaços')

print(f'Seu nome possui:{len(nome.replace(' ', ''))} letras sem considerar os espaços')

print(f'Seu primeiro nome possui:{len(quantidade[0])} letras')

print(f'Seu nome possui:{nome.find(' ')} letra sem considerar os espaços')

print(f'Você deu :{vazio} espaços para digitar seu nome')

print('-'.join(nome))

