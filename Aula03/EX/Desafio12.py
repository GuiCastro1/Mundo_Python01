'''
Criado por : Gui Castro

15/01/2025

Faça um programa que leia altura e largura de uma parede em M e calcule quantos litros de tinta são necessarios para pintala considerando que cada litro pinta 2m²

'''
#A variável largura recebe um input da largura da parede

largura = float(input("LARGURA da  Parede"))

#A variável altura recebe um input da altura da parede

altura = float(input("ALTURA da  Parede"))

#Calcura a area da parede

area = largura * altura

#Calcula a quantua de tinta que precisa para pintar a parede

tinta = area / 2 

#Usa o fString para exibir a interpolar e exibir a area e a quantia de tinta

print(f'Sua parede tem uma area de :{area:.2f} m², e precisará de :{tinta:.2f} litros de tinta para cobrila completamente.')
