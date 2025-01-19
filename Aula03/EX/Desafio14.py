'''
Criado por : Gui Castro

15/01/2025

Faça um programa que acresente 15% ao salario de um funcionario

'''

salario = float(input('digite o valor do seu salario para receber um acrescimo de 15% R$:'))

aumento = salario + (salario * 15 / 100)

print(f'Seu salario reajustado é de R$:{aumento:.2f}')
