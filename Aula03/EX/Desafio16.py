'''
Criado por : Gui Castro

16/01/2025

Escreva um programa que pergunte a quntidade de km rodados por um carro alugado e e a quntidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar sabendo que a diaria e de 60 R$ e 0,15 centavos por km
'''
# recebe os valores de dias com o carro e km rodados
dia = int(input('Tempo com o carro?'))
km = float(input('Km rodados  com o carro'))

#Faz o calculo de alugel do carro
rd = (dia * 60) + (km * 0.15)

#Exibe o preço do aluguel
print(f'O preço total do alugel mais os km, são de: {rd :.2f}')