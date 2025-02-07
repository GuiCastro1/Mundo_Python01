"""
Criado por : Gui Castro
05/01/2025

Crie um scrpit que leia o nome de uma pessoa e retorne uma mensagem de boas vindas
com o valor digitado
"""
print("=====Desafio01=====")

# A variável nome recebe um input com o nome e guarda em formato de string na memória 

nome = input ('Qual e o seu nome?')

#A função print usa o método fString para interpolar a variável nome gerando uma mensagem personalizada.

print (f"Olá, {nome} seja bem-vindo ao mundo do python !!!")
