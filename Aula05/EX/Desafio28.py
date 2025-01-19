'''
Criado por : Gui Castro

17/01/2025

Crie um programa que leia o nome de uma pessoa e exiba o primero e o ultimo nome dela.

guilherme castro perreira de araujo

guilherme 
araujo
'''
nome = str(input('Digite seu nome completo:')).lower().strip()

nome= nome.split()

print(f'Seu primero nome é: {nome[0]}')
print(f'Seu ultimo nome é:{nome[-1]}')
