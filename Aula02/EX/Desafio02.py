'''
Criado por : Gui Castro
15/01/2025

crie um programa que leia algo do teclado e informe seu tipo primitivo e todas as informações possiveis sobre ele 
'''
valor = input('Digite Algo')

print(f"O valor digitado está em maiúsculas? {valor.isupper()}")

print(f"O valor digitado está em minúsculas? {valor.islower()}")

print(f"O valor digitado é numérico? {valor.isnumeric()}")

print(f"O valor digitado é alfabético (somente letras)? {valor.isalpha()}")

print(f"O valor digitado é alfanumérico (letras ou números)? {valor.isalnum()}")

print(f"O valor digitado contém apenas caracteres ASCII? {valor.isascii()}")

print(f"O valor digitado é imprimível (não contém caracteres de controle)? {valor.isprintable()}")

print(f"O valor digitado é um número decimal? {valor.isdecimal()}")

print(f"O valor digitado contém apenas espaços? {valor.isspace()}")

print(f"O valor digitado está capitalizado (primeira letra maiúscula, resto minúsculo)? {valor.istitle()}")

print(f"O valor digitado contém apenas dígitos? {valor.isdigit()}")

print(f"O valor digitado é um identificador válido em Python? {valor.isidentifier()}")
