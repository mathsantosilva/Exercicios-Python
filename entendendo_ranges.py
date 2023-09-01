"""
Ranges

- Precisamos conhecer o loop para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequencias numericas, não de forma aleatoria,
mas sim de maneira especificada

Formas gerais:
# Forma 1
range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, incrementado de 1 em 1)

# Exemplo forma 2
range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, incrementado de 1 em 1)

# Exemplo forma 3
Range(valor_de_inicio, valor_de_parada, valor_passo)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, incrementado de acordo com o valor passo)

# Exemplo forma 4
Range(valor_de_inicio, valor_de_parada, valor_passo)

OBS: valor_de_parada não inclusive (final especificado pelo usuario, decrementando de acordo com o valor passo)

Utilização do range:

lista = range(1, 10, 1) # Não ira gerar a lista de numeros
print(lista) # Saida: range(1, 10)

lista = list(range(1, 10, 1)) # Gera a lista de numeros
print(lista) # Saida: [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
"""
# Exemplo Forma 1
for num in range(11):
    print(num)
"""

"""
# Exemplo forma 2
for num in range (1, 11):
    print(num)
"""
"""
# Exemplo forma 3
for num in range(1, 10, 2):
    print(num)
"""

"""
# Exemplo forma 4
for num in range(10, 0, -1):
    print(num)
"""
