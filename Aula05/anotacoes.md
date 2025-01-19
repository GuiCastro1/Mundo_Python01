# Manipulação de Strings no Python

As strings no Python são objetos extremamente versáteis, permitindo uma ampla variedade de operações, como fatiamento, análise, transformação e divisão. Aqui estão as principais funcionalidades com exemplos para facilitar a compreensão.

---

## Fatiamento

Fatiar uma string significa obter pedaços dela com base nos índices:

- **Acessando índices**:
  ```python
  frase = "Curso em Video Python"
  print(frase[9])  # Saída: 'V'
  ```

- **Fatiamento com intervalos**:
  ```python
  print(frase[9:21])  # Saída: 'Video Python'
  print(frase[9:21:2])  # Saída: 'VdoPto'
  print(frase[:5])  # Saída: 'Curso'
  print(frase[15:])  # Saída: 'Python'
  print(frase[9::3])  # Saída: 'VePh'
  ```

---

## Análise

### Principais Métodos:

1. **`len()`**:
   - Retorna o comprimento da string.
   ```python
   print(len(frase))  # Saída: 21
   ```

2. **`count()`**:
   - Conta quantas vezes um caractere aparece na string.
   - Aceita parâmetros de fatiamento.
   ```python
   print(frase.count('o'))  # Saída: 3
   print(frase.count('o', 0, 13))  # Saída: 2
   ```

3. **`find()`**:
   - Encontra o índice da primeira ocorrência de uma substring.
   - Retorna `-1` se não for encontrada.
   ```python
   print(frase.find('deo'))  # Saída: 11
   print(frase.find('Java'))  # Saída: -1
   ```

4. **`in`**:
   - Verifica se uma substring está presente na string.
   ```python
   print('Curso' in frase)  # Saída: True
   ```

---

## Transformação

### Principais Métodos:

1. **`replace()`**:
   - Substitui todas as ocorrências de uma substring por outra.
   ```python
   nova_frase = frase.replace('Python', 'Android')
   print(nova_frase)  # Saída: 'Curso em Video Android'
   ```

2. **`upper()`**:
   - Converte todos os caracteres para maiúsculas.
   ```python
   print(frase.upper())  # Saída: 'CURSO EM VIDEO PYTHON'
   ```

3. **`lower()`**:
   - Converte todos os caracteres para minúsculas.
   ```python
   print(frase.lower())  # Saída: 'curso em video python'
   ```

4. **`capitalize()`**:
   - Converte apenas o primeiro caractere para maiúscula.
   ```python
   print(frase.capitalize())  # Saída: 'Curso em video python'
   ```

5. **`title()`**:
   - Converte o primeiro caractere de cada palavra para maiúscula.
   ```python
   print(frase.title())  # Saída: 'Curso Em Video Python'
   ```

6. **`strip()`**:
   - Remove espaços em excesso do início e do fim da string.
   - Variantes:
     - `rstrip()`: Remove apenas espaços à direita.
     - `lstrip()`: Remove apenas espaços à esquerda.
   ```python
   frase = "   Curso em Video Python   "
   print(frase.strip())  # Saída: 'Curso em Video Python'
   print(frase.rstrip())  # Saída: '   Curso em Video Python'
   print(frase.lstrip())  # Saída: 'Curso em Video Python   '
   ```

---

## Divisão

### Principais Métodos:

1. **`split()`**:
   - Divide a string em uma lista de palavras.
   ```python
   palavras = frase.split()
   print(palavras)  # Saída: ['Curso', 'em', 'Video', 'Python']
   ```

2. **`join()`**:
   - Junta os elementos de uma lista em uma única string, com um caractere separador.
   ```python
   frase_junta = '*'.join(palavras)
   print(frase_junta)  # Saída: 'Curso*em*Video*Python'
   ```

---

Essas ferramentas permitem manipular strings de forma poderosa e flexível. Explore cada método para dominar o trabalho com textos no Python!

