nome = str(input('Digite seu nome')).strip().upper()

espaços = nome.replace(' ', '')
nome= nome.split()

if len(espaços) > 30:

    print(f'Nome muito grande seu nome possui {len(espaços)} e nosso limite é 30')
    print(f'{'-'.join(nome)}')
    
    print(f'Use seu  primero nome é: {nome[0]}')

    print(f'E seu ultimo nome é:{nome[-1]}')
else:
    print(f'Seu nome esta dentro do limite de digitos ')

#('carro novo' if tempo <= 3 else 'carro velho')
#operador ternario