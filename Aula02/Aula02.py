"""
Criado por : Gui Castro
15/01/2025

"""
a = int(input('Digite Algo'))
b = float(input('Digite Algo'))
c = str(input('Digite Algo'))
d = bool(input('Digite Algo'))

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("=====Calculadora=====")

num = int(input("Digite um numero"))

ndois = int(input("digite outro"))

r = num + ndois

print(f"soma de {num} + {ndois} é: {num + ndois}")

print('soma de {} + {} é: {}'.format(num, ndois, r))


n = input('Digite Algo')

print(n.isalpha())
print(n.isnumeric())
