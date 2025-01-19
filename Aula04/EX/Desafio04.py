'''
Criado por : Gui Castro

16/01/2025

Um professor quer sortear um de seus alunos para receber uma bala, faça um programa que ajude ele, a ler o nome deles e escrevendo o nome do escolhido.
'''
from random import choice

aluno_um = str(input('Digite o nome do primeiro aluno'))

aluno_dois = str(input('Digite o nome do sengundo aluno'))

aluno_tres = str(input('Digite o nome do terceiro aluno'))

aluno_quatro = str(input('Digite o nime do quarto aluno'))

lista = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]

# O metodo choice escolhe um item da lista 
aluno = choice(lista)

print(f'O aluno sorteado foi : {aluno}')
