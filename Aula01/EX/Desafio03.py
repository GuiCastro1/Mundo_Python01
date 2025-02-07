'''
Criado por : Gui Castro
05/01/2025

Cria um script que receba dois numeros e mostra a soma deles
'''
print("=====Desafio03=====")
# as variáveis (num e ndois) recebem um número do tipo str e armazena na memória.
num = input ("digite um numero") # entrada 5
ndois = input ("digite outro numero") # entrada 5
#Podemos realizar a conta direto no print sem a necessidade de criar outra variával e gastar mais memória. Nesse caso quando tentamos usar a operação de soma ocorre um resultado errado da conta pois os dados guardados são do tipo str e o python entende que tem que juntar um texto com outro resuntando em 55 como saida no lugar ade 10.

print("soma e", num + ndois) #saísda 55
print("brincadeirinha ! ! ! ! ! ! ")

#Nesse segundo caso declaramos o tipo de dados que vamos trabalhar, um dados do tipo int, Convertendo o input do tipo texto para a um número inteiro.

num = int(input ("digite um numero"))# Entrada 15
ndois = int(input ("digite outro numero")) # Entrada 15

print(num + ndois)# Saida 30
    