'''
Criado por : Gui Castro

15/01/2025

crie um programa que que receba o numero de um produto e acresenter um preço com desconto de 5 %


desconto = preco - (preco * 5 / 100) conta que exibe o valor ja com desconto sem ter que cirar outra variavel para realizar a subtração do valor original - valor com desconto
'''
print('=====Desconto=====')

#Recebe o valor que recebera o desconto
preco = float(input('Digite o valor da peça para receber o desconto de 5 % R$:'))

#Faz o calculo de 5% de desconto
desconto = preco - (preco * 5  / 100)

#Exibe o preço com e sem desconto
print(f'Sua roupa com o valor de:{preco:.2f} sairá por;{desconto:.2f} com o cumpom de 5%')


#Isso ta """errado"""
# print(f'O valor de dasconto da sua roupa é de: {desconto:.2f} reais')
# print(f'Sendo assim ela saira por {preco - desconto:.2f}')
