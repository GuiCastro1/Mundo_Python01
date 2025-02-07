'''
Criado por : Gui Castro
15/01/2025

crie um progama que leia dois numeros e retorne uma operação deles

'''
# As variáveis (num, ndois) recebem um número e guardam na memória no tipo str.

num = input('Digite um Número')

ndois = input('Digite Outro Número')

# A função Print usa o Fstring para interpolar os dados e para mostrar os resultados temos que converter o tipo da variável chamando o int() e passando a variável como parâmetro.abs

print (f'A soma de {num} + {ndois} é: {int(num) + int(ndois)}')

print (f'A subtração de {num} - {ndois} é: {int(num) - int(ndois)}')

print (f'A divisão {num} / {ndois} é: {int(num) / int(ndois)}')

print (f'A multiplicação {num} * {ndois} é: {int(num) * int(ndois)}')
    