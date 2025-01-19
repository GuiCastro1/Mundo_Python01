'''
Criado por : Gui Castro

17/01/2025
Crie um programa que leia o nome de uma pessoa e verifique se ela possui o nome "Silva" no nome.
'''

nome = str(input('Digite seu nome:'))

nome = nome.lower()

print(f'{'silva' in nome}')
