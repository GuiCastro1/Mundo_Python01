'''
Criado por : Gui Castro

15/01/2025

Faça um Programa qie leia um numero E mostra na tela  o seu sucessor e antesessor
 
✔✔✔
'''
print("=====Sucessor & Antecessor=====")

#A variável (numero)  recebe um numero e ja converte para o tipo int, e guada na memória.

numero = int(input('Digite um numero para decobrir seu sucessor e seu antecessor'))

# Para realizar o desafio de mostrar o sucessor e antecessor e so soma e diminuir um do valor original

#Esse print esta feito da maneira errada usando um meio de formatação de python 2

print('Sucessor : {}'.format(numero + 1))

print('Antecessor  : {}' . format(numero -1))

#O correto para o Python 3 é:

print(f'Sucessor: {numero + 1}')
print(f'Antecessor: {numero - 1}')