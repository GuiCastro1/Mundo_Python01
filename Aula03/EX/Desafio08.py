'''
Criado por : Gui Castro

15/01/2025

Crie um programa que leia a nota de um aluno e calcule sua media
'''

print('=====Média=====')
#As variaáveis (nota1 nota2 nota3 nota4) rebem valores do tipo str e convertem para float(Números com casas decimais) e armazena em mamória.
nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a segunda nota'))
nota3 = float(input('Digite a terceira nota'))
nota4 = float(input('Digite a quarta nota'))
# com o fString fiz a conta de média somando tudo e dividindo pelo numero de notas
print(f'A Média do seu aluno é: {(nota1 + nota2 + nota3 + nota4) / 4}')


# i = 0
# soma = 0
# nota = 4

# while i < nota :

#     num = float(input('digite uma nota'))

#     soma+= num
#     i+=1
   
# print(f'A media do seu aluno é :{soma / nota}')