# Aula 03: Operadores Aritméticos no Python

Nesta aula, aprendemos sobre os operadores aritméticos disponíveis no Python e a ordem de precedência utilizada em expressões matemáticas. Aqui estão as anotações principais e complementos.

---

## Operadores Aritméticos

### Operações Básicas:
1. **Adição** (`+`): Soma dois valores.
   - Exemplo: `2 + 3` resulta em `5`.
2. **Subtração** (`-`): Subtrai o segundo valor do primeiro.
   - Exemplo: `5 - 2` resulta em `3`.
3. **Multiplicação** (`*`): Multiplica dois valores.
   - Exemplo: `4 * 3` resulta em `12`.
4. **Divisão** (`/`): Realiza a divisão comum, retornando um resultado do tipo `float`.
   - Exemplo: `10 / 2` resulta em `5.0`.

### Operações Avançadas:
1. **Potência** (`**`): Calcula a exponenciação.
   - Exemplo: `2 ** 3` resulta em `8`.
2. **Divisão Inteira** (`//`): Retorna o quociente inteiro de uma divisão.
   - Exemplo: `7 // 2` resulta em `3`.
3. **Módulo** (`%`): Retorna o resto da divisão.
   - Exemplo: `7 % 3` resulta em `1`.

### Observação:
- **Operadores binários** requerem dois operandos (valores). Por exemplo: `5 + 3` ou `10 % 2`.

---

## Operadores de Atribuição e Comparação

1. **Atribuição** (`=`): Utilizado para armazenar um valor em uma variável.
   - Exemplo:
     ```python
     x = 10
     print(x)  # Saída: 10
     ```
2. **Comparação** (`==`): Verifica se dois valores são iguais.
   - Exemplo:
     ```python
     print(5 == 5)  # True
     print(5 == 3)  # False
     ```

---

## Ordem de Precedência

Ao realizar cálculos, o Python segue uma ordem de precedência definida. Essa ordem determina quais operações são executadas primeiro em uma expressão.

### Ordem Prioritária:
1. **Parênteses** (`()`): Operações dentro de parênteses são executadas primeiro.
   - Exemplo: `(2 + 3) * 4` resulta em `20`.
2. **Potência** (`**`): Realizada antes de outras operações matemáticas.
   - Exemplo: `2 ** 3 + 1` resulta em `9`.
3. **Multiplicação, Divisão, Divisão Inteira e Módulo** (`*`, `/`, `//`, `%`): Têm a mesma prioridade.
   - Exemplo: `10 / 2 * 3` resulta em `15.0`.
4. **Adição e Subtração** (`+`, `-`): Executadas por último.
   - Exemplo: `5 + 3 - 2` resulta em `6`.

### Exemplo Geral:
```python
resultado = (2 + 3) * 4 ** 2 / 8 % 3
print(resultado)  # Saída: 1.0
```

---

## Dicas e Boas Práticas

- Sempre use parênteses para tornar expressões complexas mais legíveis.
- Lembre-se que operadores de mesma prioridade são executados da esquerda para a direita (com exceção do operador `**`, que é avaliado da direita para a esquerda).
- Teste diferentes combinações para entender melhor o comportamento da ordem de precedência.

---

