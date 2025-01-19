'''
Criado por : Gui Castro

17/01/2025

Crie um programa que leia o nome de uma cidade começa com "Santo" ou não.
'''

cidade = str(input('Digite o nome da sua cidade:')).strip()

cidade = cidade.lower()

print(f'{'santo' in cidade}')

print(f'{cidade[:5] == 'santo'}')