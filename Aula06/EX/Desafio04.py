'''
Criado por : Gui Castro

18/01/2025

Desenvolva um programa que pergunte a disde uma viagem em km.
Calcule o preço da passagem , cobrendo 0,50 cent por km para viagens de até 200km e 0,45 para viagens mais longas.
'''
print('=====Preço Da Passagem=====')

km = float(input('Digite quantos km deseja viajar:'))

km = km *0.50 if km <=200 else km * 0.45

print(f'O preço da sua passagem vai custar:{km}R$')
'''
if km <= 200:

    print(f'Sua passagem sairá;{km * 0.50 :.2f} para percorrer {km} km')

else: 

    print(f'Sua passagem sairá;{km * 0.45:.2f} para percorrer {km} km')

'''