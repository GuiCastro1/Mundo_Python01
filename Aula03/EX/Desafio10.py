'''
Criado por : Gui Castro

15/01/2025

crie um programa que calcule toda a da tabuada de um determinado numero

'''
print('=====Exibe Tabuada=====')  

#A variável (tabuada) transforma uma string para um tipo int.

tabuada = int(input('Digite um cumero para exibir a tabuada do mesmo'))
print("-" * 20)

# Com o fString da para interpolar e exibir a tabuada do 1 ao 10 e usei formatação para aparecer tudo alinhado.

print(f'{tabuada :<1} x 1={ tabuada * 1:>2}')
print(f'{tabuada :<1} x 1={ tabuada * 2:>2}')
print(f'{tabuada :<1} x 1={ tabuada * 3:>2}')
print(f'{tabuada :<1} x 1={ tabuada * 4:>2}')
print(f'{tabuada :<1} x 1={ tabuada * 5:>2}')
print(f'{tabuada :<1} x 1={ tabuada * 6:>2}')
print(f'{tabuada :<1} x 1={ tabuada * 7:>2}')
print(f'{tabuada :<1} x 1={ tabuada * 8:>2}')
print(f'{tabuada :<1} x 1={ tabuada * 9:>2}')
print(f'{tabuada :<1} x 1={ tabuada * 10:>2}')

print("-" * 20)

# num = int(input('Digite um cumero para exibir a tabuada do mesmo'))

# for i in range(1,11):

#     print(f'{i :<2} x {num :>2} = {i * num:>3}')


# print("-" * 20)
# ndois = int(input('Digite um cumero para exibir a tabuada do mesmo'))

# i = 1

# while i <= 10:

#     print(f'{i :<2} x {num:>2} = {i * num :>3}')

#     i+=1
# print("-" * 20)