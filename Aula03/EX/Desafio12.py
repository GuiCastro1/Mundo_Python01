'''
Criado por : Gui Castro

15/01/2025

Faça um programa que leia altura e largura de uma parede em M e calcule quantos litros de tinta são necessarios para pintala considerando que cada litro pinta 2m²

'''

largura = float(input("LARGURA da  Parede"))

altura = float(input("ALTURA da  Parede"))

area = largura * altura

tinta = area / 2 

print(f'Sua parede tem uma area de :{area:.2f} m², e precisará de :{tinta:.2f} litros de tinta para cobrila completamente.')
