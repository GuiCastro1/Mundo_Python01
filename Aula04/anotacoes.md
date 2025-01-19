# Aula 04: Módulos no Python

Nesta aula, aprendemos sobre o uso de módulos (ou bibliotecas) no Python e como eles ajudam a organizar e expandir as funcionalidades de seus programas. Aqui estão as anotações principais e complementares.

---

## O Que São Módulos?

O Python, por padrão, oferece uma base essencial de funcionalidades. Para não sobrecarregar o programa, você pode adicionar bibliotecas (também chamadas de pacotes ou módulos) conforme necessário. Isso torna o programa mais leve e flexível, além de facilitar a personalização.

---

## Como Importar Módulos?

### Importação Generalista:
- Utiliza o comando `import` para carregar toda a biblioteca.
- Ideal para casos onde você precisa de múltiplas funcionalidades do módulo.

Exemplo:
```python
import math

print(math.sqrt(16))  # Retorna a raiz quadrada: 4.0
```

### Importação Específica:
- Utiliza `from` seguido de `import` para carregar apenas funcionalidades específicas do módulo.
- Reduz o uso de memória e torna o código mais legível.

Exemplo:
```python
from math import sqrt

print(sqrt(16))  # Retorna a raiz quadrada: 4.0
```

---

## Módulo `math`

O módulo `math` é amplamente utilizado para realizar operações matemáticas. Aqui estão algumas de suas principais funções:

1. **`ceil`**
   - Arredonda um número para cima.
   - Exemplo:
     ```python
     from math import ceil
     print(ceil(4.3))  # Saída: 5
     ```

2. **`floor`**
   - Arredonda um número para baixo.
   - Exemplo:
     ```python
     from math import floor
     print(floor(4.7))  # Saída: 4
     ```

3. **`trunc`**
   - Elimina a parte decimal, sem arredondar.
   - Exemplo:
     ```python
     from math import trunc
     print(trunc(4.9))  # Saída: 4
     ```

4. **`pow`**
   - Calcula a potência de um número.
   - Equivalente a `base ** expoente`.
   - Exemplo:
     ```python
     from math import pow
     print(pow(2, 3))  # Saída: 8.0
     ```

5. **`sqrt`**
   - Calcula a raiz quadrada.
   - Exemplo:
     ```python
     from math import sqrt
     print(sqrt(25))  # Saída: 5.0
     ```

6. **`factorial`**
   - Calcula o fatorial de um número.
   - Exemplo:
     ```python
     from math import factorial
     print(factorial(5))  # Saída: 120
     ```

---

## Dicas e Boas Práticas

1. Utilize **importações específicas** sempre que possível para melhorar a legibilidade e desempenho.
2. Nomeie suas funções e variáveis de forma que não entrem em conflito com os nomes das funções dos módulos importados.
3. Consulte a [documentação oficial do Python](https://docs.python.org/3/library/math.html) para descobrir mais métodos e funções do módulo `math` e de outros módulos padrão.

---



