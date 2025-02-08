'''
Criado por : Gui Castro

16/01/2025

O mesmo professor que sorrear e exibir uma ordem de apresentação, faça um programa que leia o nomee dos quatros alunos e mostre a ordem sorteada.
'''

from random import shuffle

#Recebe o nome dos alunos
aluno_um = str(input('Digite o nome do primeiro aluno'))

aluno_dois = str(input('Digite o nome do sengundo aluno'))

aluno_tres = str(input('Digite o nome do terceiro aluno'))

aluno_quatro = str(input('Digite o nime do quarto aluno'))

#Adciona em uma lista
lista = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]

# O metodo shuffle escolhe um item da lista 
shuffle(lista)

print(f'O aluno sorteado foi : {lista}')
