'''
Criado por : Gui Castro

15/01/2025

Crie um programa que cualcule seu dobro seu triplo e sua raiz quadrada

✔✔✔
'''
print('=====Dobro Triplo & Raiz²=====')

#A variável (n)  recebe um numero e ja converte para o tipo int, e guada na memória.

n = int(input('Digiter um Número'))

#Para realizar esse desafio fiz por meio da interpolação usando Fstring para não criar uma variável já que as contas são um formula contante

#Calcula o dobro 
print(f'O Dobro do número {n} é : {n *2}')
#Calcula o triplo
print(f'O triplo do número {n} é : {n*3}')
# o Jeito certo de calcular a raiz quadrada.
print(f'A raiz quadrada do número {n} é : {n ** (1/2)}')

#Esse calculo esta errado ?
print(f'A raiz quadrada do número {n} é : {n *n}')