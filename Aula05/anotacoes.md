Manipulando com Stings:

Fatiamento: pegar pedaços de uma string("Modo de usar - nome da variavel e [o indice] para pegar mais indices usar[o valor : o valor desejado = +1]")

[9: 21 ; 2] vai de nove a vinte e um pulando de 2 em 2 pode ser escrito [9::3]
                                                                                         🔼 
[:5] == [0:5]  ele vai do começo ate o valor dindiciado e o mesmo ao contrario ex [15 : ] vai a partir do 15 ate o final fa que não esta declarado.


Analise:

len- mostra o comprimento 

count('o'(0,13))- conta quantas letras o tem. Pode-se usar parametros de fatiamento 

find('deo') - encontra o indice onde se encontra a frase declarada 'deo'. se declarar uma frase que não exista na retornara -1 que não foi encontra do 

in retorna True e False se houver o item declarado na frase.

Transformação:

replace- substitui uma palavra por outra('python', 'android') trocaria todas as palavras python por android. "não substitui diretamente na string"

upper- transforma em maiuscula 

lower- transforma em minuscula

captalize- deixa todas as letras minusculas exeto a primera

title- Analisa todas as palavras e aplica o captalize na palavra independentes (ola mundo -> Ola Mundo "CamelCase")

strip- remove todos os espaços a mais do inicio e do fim. se colocar um (R) fara so o da direita, e (L)para esquerda

"As duas precisam de () pois são metodos"


Divisão:

Split- cada palavra encontrada recebe seu propio indice. E é locado em "lista"

join- junta os split e adiciona um caracter se desejado ("*".join(frase))
