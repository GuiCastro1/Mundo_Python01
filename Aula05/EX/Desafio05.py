'''
Criado por : Gui Castro

17/01/2025

Faça um programa que leia uma frase pelo teclado e mostre;

Quantas vezes aparece a letra "A"

Em que posição ela aparace a primeira e ultima vez
'''

frase = str(input('Digite uma frase:')).strip().strip()

frase= frase.upper()

quantidade = frase.count('A')

posicao_um = frase.find('A') + 1

posicao_dois = frase.rfind('A')


print(f'Você digitou a letra "a":{quantidade}')
print(f'A primeira se encontra no indice:{posicao_um}')
print(f'A ultima vez se encontra no indice:{posicao_dois}')

