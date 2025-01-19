'''
Criado por : Gui Castro

18/01/2025

Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar a velocidade de 80kh mostre uma mensagem de multa, e calcule a multa de 7 R$ por km a mais.
'''
print('=====Radar=====')

velocidade = float(input('Velocidade do veiculo:'))

if velocidade > 80 :

    multa = velocidade - 80

    print(f'Você excedeu o limite de 80km/h da pista. Você estava {multa}km acima da velocidade permitida. Você vai receber uma multa de 7,00R$ por km a mais.')

    print(f'Multa ;{multa * 7 :.2f}')

print(f'Você esta dentro do limite de velocidade. parabens!!!!')
