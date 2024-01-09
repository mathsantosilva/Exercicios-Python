"""
Seção 3 - Aula 12
Comandos input

-- Receber dados do usuario
Input -> Recebe uma entrada de dados vinda do console inserida pelo usuario
OBS: os dados por padrão vem como o tipo string
Exemplo: print(**texto ou variavel desejada**)

    Cenario 1: Coletando o nome do usuario usando print como mensagem
    EX:
    print("Qual seu nome ?")
    nome = input()
    Result: Ira escrever no console o texto que foi inserido e ficar aguardando a entrada de dados

    Cenario 1: Coletando o nome do usuario usando input como mensagem
    EX:
    nome = input("Qual seu nome ?")
    Result: Ira escrever no console o texto que foi inserido e ficar aguardando a entrada de dados
"""

# Primeira entrada de dados
# Usando print
print("Qual é seu nome ? ")
nome = input()
print(f"Seja bem vindo(a) {nome}")

print("Qual é sua idade ? ")
idade = input()
print(f"Então o {nome} tem {idade} anos de idade !")

# Segunda entrada de dados
# Sem usar print
nome = input("Qual é seu nome ? ")
print(f"Seja bem vindo(a) {nome}")

idade = input("Qual é sua idade ? ")
print(f"Então o {nome} tem {idade} anos de idade !")