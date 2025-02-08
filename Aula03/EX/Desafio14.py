'''
Criado por : Gui Castro

15/01/2025

Faça um programa que acresente 15% ao salario de um funcionario

'''
#Recebe o salário 
salario = float(input('digite o valor do seu salario para receber um acrescimo de 15% R$:'))

#Faz o calculo do salário com o aumento de 15% do salário, na variável aumento
aumento = salario + (salario * 15 / 100)

#Exibe o salário reajustado com a variável aumento
print(f'Seu salario reajustado é de R$:{aumento:.2f}')
