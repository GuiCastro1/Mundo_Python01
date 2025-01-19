'''
Criado por : Gui Castro

18/01/2025

Escreva um programa que faça o computador escolher um numero inteiro entre 1 & 5 E peça para o usuario descobrir o numero escolhido pelo com putador. E exiba se ele ganhou ou perdeu
'''
from random import randint
from time import sleep

print('=====Jogo Da Adivinhação=====')

user = str(input('Vamos jogar 😈😈😈? (Y/N)')).strip().upper()

if user == 'Y':

    valor = int(input('Qual número eu estou pensando entre 1 e  10?'))

    num1 = randint(1,10)

    if valor == num1:
        print(f'PROCESSANDO.....')
        sleep(3)
        print(f'Você acertou, era: {num1}  🙄🙄🙄')
    else:
        print(f'PROCESSANDO.....')
        sleep(3)
        print(f'Você perdeu, era: {num1}  😈😈😈')

else:

    print(f'O jogo acabou 😤😤😤')
