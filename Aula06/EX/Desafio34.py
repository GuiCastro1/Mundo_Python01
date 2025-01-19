'''
Criado por : Gui Castro

18/01/2025

faça um programa que leia 3 numeros e exiba qual e o maior e o menor.
'''

print('=====Maior & Menor=====')

numero_um = float(input('Digite o primeiro número:'))
numero_dois = float(input('Digite o segundo número:'))
numero_tres = float(input('Digite o terceiro número:'))

lista = [numero_um, numero_dois, numero_tres]

lista.sort()

print(f'Menor:{lista[0]}')
print(f'Maior:{lista[-1]}')

print('#'*30)

n_um = int(input('Primeiro valor'))
n_dois = int(input('Segundo valor'))
n_tres = int(input('terceiro valor'))

menor = n_um

if n_dois < n_um and n_dois < n_tres:

    menor = n_dois

if n_tres < n_um and n_tres < n_dois:

    menor = n_tres

maior = n_um

if n_dois > n_um and n_dois > n_tres:

    maior = n_dois

if n_tres > n_um and n_tres > n_dois:

    maior = n_tres

print(f'Menor:{menor}')

print(f'Maior:{maior}')
