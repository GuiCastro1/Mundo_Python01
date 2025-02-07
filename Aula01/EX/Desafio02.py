'''
Criado por : Gui Castro
05/01/2025

Crie um scrpit que leia a data de nascimento de uma pessoa e mostre de maneira
formatada
'''
print("=====Desafio02=====")

# As variáveis (dia, mes e ano) recebem um input que guarda as informações da data de nascimento do usúario e armazenam na memória.

dia = input("Digite o dia que você nasceu")
mes = input("Digite o mês")
ano = input("E ano")

#A função print usa o método fString para interpolar a variável (dia, mes, ano) gerando a frase formatada.

print(f"Você nasceu no dia {dia} de {mes} de {ano}. Correto?")
