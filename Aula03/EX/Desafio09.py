'''
Criado por : Gui Castro

15/01/2025

faça um programa que converta de metro para cm e de cm para mm

'''
print('=====Conversor de Metros=====')

metro = float(input('digite um valor em METROS para converter em DM, CM, & MM'))

print(f"{metro} Metros em Km são :{ metro / 1000}Km")

print(f"{metro} Metros em Hm são :{ metro / 100}Hm")

print(f"{metro} Metros em Dam são  :{ metro / 10}Dam")

print(f"{metro} Metros em Dm são :{ metro * 10}Dm")

print(f"{metro} Metros em Cm são :{ metro * 100}Cm")

print(f"{metro} Metros em Mm são  :{ metro * 1000}Mm")