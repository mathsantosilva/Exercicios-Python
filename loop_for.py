"""
Loop for
Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //bloco de codigo
}

Python

for item in interavel:
    //Bloco de codigo


Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis

Exemplos valores iteraveis
- String:
    nome = 'Geek University'
- Lista:
    list = [1, 2, 3, 4, 5]
- Range:
    numeros = range(1, 10)

Range(valor_inicial, valor_final)
OBS: O valor final não e incluso então (igual a n) e não (Maior igual a n)
Range(1, 5)
1
2
3
4
5 - Não itera

Enumerate:
nome = 'Geek'
enumerate(nome)
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')...)

Tabela de emoji, unicode
"""
nome = "Geek University"
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10) # Temos que transformar em uma lista

"""
# Exemplo de for 1 (Iterando sobre uma string)
for letra in nome:
    print(letra)
"""

"""
# exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)
"""

"""
# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1, 10):
    print(numero)
"""

"""
for i, v in enumerate(nome):
    print(nome[i])
"""

"""
# Formas de lidar com retorno de dois valores
# Guardar cada valor em uma variavel diferente (indice, letra)
for indice, letra in enumerate(nome):
    print(indice) # acessa o indice 0
    print(letra) # acessa a letra G

# Ignorar o valor que deseja descartar (_)
# A linguagem python entende o underline como um simbolo para ignorar as coisas
for _, letra in enumerate(nome):
    # O valor do indice foi ignorado
    print(letra) # Acessa a letra G
    
# guardar os dois valores em uma variavel, mas somente acessar o valor desejado([1...])
for letra in enumerate(nome):
    # O valor do indice não esta sendo acessado
    print(letra[1]) # Esta acessando a letra G, utilizando o valor de indice dela, sendo dois itens então ((0)[0] ('G')[1])
    
"""

"""
qtd = int(input('Quantas vezes esse loop deve rodar ?'))

for n in range(1, qtd+1):
    print(f"Imprimindo {n}")
"""
"""
nome = 'Geek University'
for letra in nome:
    print(letra, end="")
"""

# Original: U+1F60D
# Modificado: U0001F60D
emoji = '\U0001F60D'

for num in range(1, 11):
    print(f'{emoji * num}')
