# Aula 02: Tipos Primitivos no Python

Nesta aula, aprendemos sobre os **tipos primitivos** do Python e alguns de seus métodos associados. Abaixo estão as anotações principais e complementos sobre o tema.

---

## Tipos Primitivos

1. **int**: Representa números inteiros.
   - Exemplo: `42`, `-10`, `1000`

2. **float**: Representa números decimais (ponto flutuante).
   - Exemplo: `3.14`, `-0.5`, `2.0`

3. **string**: Representa sequências de caracteres (texto).
   - Exemplo: `'Python'`, `"Curso"`

4. **boolean**: Representa valores lógicos, que podem ser:
   - `True` (verdadeiro)
   - `False` (falso)

---

## Métodos Associados a Tipos Primitivos

### 1. **`format`**
- Permite formatar valores em strings.

Exemplo:
```python
idade = 25
mensagem = "Eu tenho {} anos.".format(idade)
print(mensagem)
```
Saída:
```
Eu tenho 25 anos.
```

### 2. **`isnumeric`**
- Verifica se o valor de uma string é composto apenas por números e pode ser convertido para o tipo `int`.

Exemplo:
```python
valor = "12345"
print(valor.isnumeric())  # True
```

### 3. **`isalpha`**
- Verifica se a string contém apenas caracteres alfabéticos (sem espaços ou números).

Exemplo:
```python
texto = "Python"
print(texto.isalpha())  # True
```

### 4. Outros Métodos Importantes
- **`isdigit`**: Similar ao `isnumeric`, mas funciona apenas para caracteres do tipo `digit`.
- **`isdecimal`**: Verifica se todos os caracteres de uma string são decimais.
- **`isupper`**: Verifica se todos os caracteres alfabéticos estão em maiúsculas.
- **`islower`**: Verifica se todos os caracteres alfabéticos estão em minúsculas.

---

## Exemplos Adicionais

### Tipos e Conversões

- **`type()`**: Retorna o tipo do valor.
- Conversões explícitas:

Exemplo:
```python
num_str = "42"
num_int = int(num_str)  # Converte string para inteiro
print(type(num_int))    # <class 'int'>
```

### Verificações com Métodos

Exemplo:
```python
texto = "Python123"
print(texto.isalpha())    # False, pois contém números

numero = "1234"
print(numero.isnumeric())  # True
```

A combinação desses métodos facilita a validação de dados e o trabalho com diferentes tipos no Python.

