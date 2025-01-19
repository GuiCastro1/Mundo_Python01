'''
Criado por : Gui Castro

18/01/2025

Faça um programa que calcule um aumento de salario. para salarios de ate 1250 aumente 10%. para inferiores ou = 15% 
'''

print('=====Aumento=====')

salario = float(input('Informe o valor do seu salário para receber um aumento'))

if salario <= 1.250:

    print(f'Você recebeu um aumento de 15%. Salário atual:{salario} salário com aumento{salario + (salario * 15 / 100)}')

else:
    print(f'Você recebeu um aumento de 10%. Salário atual:{salario} salário com aumento {salario + (salario * 10 / 100)}')
'''
salario = salario+(salario * 15 / 100) if salario <= 1.250 else salario + (salario * 10 / 100)
print(f'Novo salario;{salario :.2f}')

'''
