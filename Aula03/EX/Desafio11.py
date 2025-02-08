'''
Criado por : Gui Castro

15/01/2025

Crie um programa que  leia quanto de dinheiro uma pessoa tem na carteira e quntos dolares el apode comprar considere a cotação autal

'''
print('=====Converte Doleta=====')

#A variável real armazena um número float 

real = float(input('quanto dinheiro você tem na Carteira ? R$'))

# A variável doleta Armazena o valor do dolar no dia que fiz o codigo

doleta =  6.0377

#A função print com o fString faz o calculo da conversão de real para dolar

print (f'Com esse {real:.2f} você pode comprar {real / doleta:.2f} Dólares')