'''
Criado por : Gui Castro

16/01/2025

Faça um programa que leia comprimento  do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
'''
#Importa a math que é uma lib nativa de matemática do python
import math

adjacente = float(input('Digite o valor do cateto adjacente do seu triangulo:'))

oposto = float(input('digite o valor do cateto oposto do seu triangulo'))

#desse modo o python faz o calculo dos catetos e usa o sqrt para descobrir a raiz quadrada

hipotenusa = math.sqrt(oposto **2 + adjacente**2)

# Aqui não utilizamos o modulo fazemos as somas dos catetos elevados e resolvemos a raiz elevendo ela a 1/2

hipo = (adjacente ** 2 + oposto ** 2) ** (1/2)

# O hypot e uma lib dedicada a essse calculo 
h = math.hypot(adjacente , oposto)


# math.floor ou math.trunc para manipular números de forma precisa e controlada.
print(math.trunc(hipotenusa * 100) / 100)

print(math.trunc(hipo * 100) / 100)

print(math.trunc(h * 100) / 100)

print(math.floor(hipotenusa * 100) /100)

print(math.floor(hipo * 100) / 100)

print(math.floor(h * 100) / 100)

print(f'{hipotenusa :.2f}')

print(f'{hipo :.2f}')

print(f'{h:.2f}')
