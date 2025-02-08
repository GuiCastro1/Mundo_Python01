'''
Criado por : Gui Castro

16/01/2025

Faça um programa que leia um angulo qualquer e mostre na tela o seu Seno Cosseno & Tangente desse angulo
'''

from math import cos, sin, tan, trunc,radians, floor, ceil

angulo = float(input('Digite um angulo:')) 

#O exercicio estava errad pois para usar os modulos COS, SIN, TAN  é  necessario converter o valor para radiando e para fazer isso é só usar a lib radians
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))

#Exibe a seno e usa com os metodos usando os médotos que manipulam os decimais
print(f'O Seno de {angulo}º é : {seno :.2f}')
print(f'{trunc(seno * 100) / 100}')
print(f'{floor(seno * 100) / 100}')
print(f'{ceil(seno * 100) / 100 :.2f}')

#Exibe a cosseno e usa com os metodos usando os médotos que manipulam os decimais
print(f'O Cosseno de {angulo}º é : {cosseno :.2f}')
print(f'{trunc(cosseno * 100) / 100}')
print(f'{floor(cosseno * 100) / 100}')
print(f'{ceil(cosseno * 100) / 100 :.2f}')

#Exibe a tangente e usa com os metodos usando os médotos que manipulam os decimais
print(f'A Tangente de {angulo}º é : {tangente :.2f}')
print(f'{trunc(tangente * 100) / 100}')
print(f'{floor(tangente * 100) / 100}')
print(f'{ceil(tangente * 100) / 100 :.2f}')
