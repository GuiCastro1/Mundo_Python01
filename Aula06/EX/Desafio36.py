'''
Criado por : Gui Castro

18/01/2025

desenvolva um programa que leia três retas  e diga ao usuario de elas podem formar um triângulo.
'''

print('=====Pode ser um triângulo?=====')

l1 = float(input('Digite o valor da prmeira reta:'))
l2 = float(input('Digite o valor da segunda reta:'))
l3  = float(input('Digite o valor da terceira reta'))

if l1 + l2 > l3 and l3 + l1 > l2 and l2 + l3 > l1:

    print(f'As retas {l1},{l2} e {l3} PODEM formar um triângulo')
else:
    print(f'As retas {l1},{l2} e {l3} NÃO PODEM formar um triângulo')