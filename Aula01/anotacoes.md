# Aula 01: Sintaxe Básica do Python

Nesta aula, foram abordados os conceitos iniciais sobre a sintaxe básica do Python. Abaixo estão as anotações principais e complementos sobre o tema.

---

## Delimitadores e Aspas

- Strings podem ser delimitadas por:
  - Aspas simples: `'exemplo'`
  - Aspas duplas: `"exemplo"`
  - Aspas triplas (simples ou duplas):
    ```python
    '''exemplo'''
    """exemplo"""
    ```

As aspas triplas são frequentemente usadas para:
- Docstrings (documentação de funções, classes e módulos).
- Strings que ocupam múltiplas linhas.

---

## Funções e Parênteses no Python 3

- No Python 3, **todos os comandos são funções** e requerem parênteses.

Exemplos:
```python
print("Hello, World!")  # Correto no Python 3
```

Erro comum:
```python
print "Hello, World!"  # Incorreto, não funciona no Python 3
```

---

## Convenções de Escrita

- **Nomes de variáveis:** Devem estar em letras minúsculas e usar underscores para separação de palavras.

Exemplo:
```python
minha_variavel = 10
```

- **Nomes de funções:** Devem seguir o mesmo padrão de letras minúsculas com underscores.

Exemplo:
```python
def minha_funcao():
    pass
```

---

## Variáveis no Python

- Em Python, **toda variável é um objeto**.
  - Isso significa que variáveis podem ter métodos associados a elas, dependendo de seu tipo.

Exemplo:
```python
texto = "Hello, World!"
print(texto.upper())  # Converte a string para letras maiúsculas
```

- A declaração de variáveis é feita dinamicamente, sem a necessidade de especificar tipos.

Exemplo:
```python
numero = 42       # Inteiro
texto = "Python"  # String
```

