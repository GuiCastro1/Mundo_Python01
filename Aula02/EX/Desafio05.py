'''
Criado por : Gui Castro
15/01/2025

crie um programa que leia algo do teclado e informe seu tipo primitivo e todas as informações possiveis sobre ele 
'''
# Solicita ao usuário que digite um valor e armazena na variável 'valor'
valor = input('Digite Algo')

# Verifica se todos os caracteres do valor estão em maiúsculas
print(f"O valor digitado está em maiúsculas? {valor.isupper()}")

# Verifica se todos os caracteres do valor estão em minúsculas
print(f"O valor digitado está em minúsculas? {valor.islower()}")

# Verifica se o valor contém apenas números (sem pontos ou sinais)
print(f"O valor digitado é numérico? {valor.isnumeric()}")

# Verifica se o valor contém apenas letras do alfabeto (sem espaços ou números)
print(f"O valor digitado é alfabético (somente letras)? {valor.isalpha()}")

# Verifica se o valor contém apenas letras e/ou números (sem espaços ou caracteres especiais)
print(f"O valor digitado é alfanumérico (letras ou números)? {valor.isalnum()}")

# Verifica se o valor contém apenas caracteres ASCII (compatível com inglês e símbolos comuns)
print(f"O valor digitado contém apenas caracteres ASCII? {valor.isascii()}")

# Verifica se o valor pode ser impresso (ou seja, não contém caracteres de controle como tabulação ou nova linha)
print(f"O valor digitado é imprimível (não contém caracteres de controle)? {valor.isprintable()}")

# Verifica se o valor representa um número decimal válido (sem letras ou símbolos)
print(f"O valor digitado é um número decimal? {valor.isdecimal()}")

# Verifica se o valor contém apenas espaços em branco (sem letras ou números)
print(f"O valor digitado contém apenas espaços? {valor.isspace()}")

# Verifica se o valor está capitalizado (ou seja, começa com letra maiúscula e o restante em minúsculas)
print(f"O valor digitado está capitalizado (primeira letra maiúscula, resto minúsculo)? {valor.istitle()}")

# Verifica se o valor contém apenas dígitos (sem letras, símbolos ou espaços)
print(f"O valor digitado contém apenas dígitos? {valor.isdigit()}")

# Verifica se o valor pode ser usado como um nome de variável válido em Python
print(f"O valor digitado é um identificador válido em Python? {valor.isidentifier()}")