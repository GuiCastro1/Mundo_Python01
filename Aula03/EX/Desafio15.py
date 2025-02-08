'''
Criado por : Gui Castro

16/01/2025

crie um programa que convertea de Celcius em Fahrenheit e Fahrenheit em Celcius

'''
#Recebe o valor em celcius
celcius = float(input("Digite a temperatura em Celcius para converter em Fahrenheit: Cº"))

#Faz a conversão de celcius para fahrenheit direto no print. Era melhor ter feito uma variável com o calculo
print(f'A temperatura digitada em Celcius corresponde a : {(celcius *1.8) + 32 } Graus Fahrenheit ! ! !')

#Recebe o valor em fahrenheit
fahrenheit = float(input('Digite a te,peratura em Farenheit para converter em Celcius: Fº'))

#Faz a conversão de fahrenheit para celcius direto no print. Era melhor ter feito uma variável com o calculo
print(f'A temperatura digitada em Fahrenheit corresponde a : {(fahrenheit - 32) * 5/9} Graus Celcius')