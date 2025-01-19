# Condicionais no Python

As condicionais no Python são estruturas fundamentais que permitem a execução de códigos diferentes com base em condições lógicas. Aqui estão os principais tipos de condicionais:

---

## Condicional Sequencial

- A execução do código segue uma sequência lógica, linha por linha.

---

## Condicional Simples

- Utiliza apenas o `if`.
- Executa um bloco de código se a condição for verdadeira.

```python
if tempo <= 3:
    print("Carro novo")
```

---

## Condicional Composta

- Combina o `if` com o `else`.
- Permite que um bloco seja executado caso a condição seja verdadeira e outro bloco caso seja falsa.

```python
if tempo <= 3:
    print("Carro novo")
else:
    print("Carro velho")
```

---

## Condicional Simplificada

- Uma única linha que substitui o `if` e o `else` para condições simples.

```python
print("Carro novo" if tempo <= 3 else "Carro velho")
```

---

Essas estruturas permitem criar lógicas mais dinâmicas e eficientes em seus programas. É importante usá-las de forma organizada e clara para garantir legibilidade e manutenção do código.

