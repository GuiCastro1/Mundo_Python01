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
'''
('carro novo' if tempo <= 3 else 'carro velho')
operador ternario

ansi?

\033[0;33;44m

style = 0=none 1=bold 4=underline 7=negative
text = 30 a 37 cada um é uma cor (""lembrar de teste"")
back = 40 a 47 mesmas cores do texto só que para background
'''