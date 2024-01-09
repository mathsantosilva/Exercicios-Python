"""
Seção 3 - Aula 12
Comandos print - cast

-- Enviar dados para o usuario
print -> Envia uma mensagem via console para o usuario
Exemplo: print(**texto ou variavel desejada**)


    Cenario 1: Passando um texto(String) para ser printado
    EX: print("Ola seja bem vindo")
    Result: Ira escrever no console o texto que foi inserido

    Cenario 2: Passando uma variavel do tipo string para ser printada
    EX:
    texto = "Ola seja bem vindo"
    print(texto)
    Result: Ira escrever no console o texto que foi inserido dentro da variavel

-- Tratamento de dado
cast -> Conversão de um tipo de dado em outro
OBS: no caso os inputs vem como string, sendo necessario trocar para um tipo numero para trabalhar com numeros
OBS2: Em todos os cenarios, caso o usuario forneça algo que não seja um numero, o programa ira cair em uma exceção
Exemplo: int(idade)


    Cenario 1: Recebendo a idade em string e convertendo ela no momento do print
    EX:
    print("Diga a sua idade: ")
    idade = input()
    anoatual = 2024
    print(f"então você nasceu em {anoatual - int(idade)}")
    Result: Ira printar o resultado da subtração do ano atual, menos a idade fornecida

    Cenario 2: Tratando a idade diretamente no momento que ela é recebida
    EX:
    print("Diga a sua idade: ")
    idade = int(input())
    anoatual = 2024
    print(f"então você nasceu em {anoatual - idade}")
    Result: Ira printar o resultado da subtração do ano atual, menos a idade fornecida
"""
# Primeira entrada de dados
anoatual = 2024
print("Qual é seu nome ? ")
nome = input()

# Exemplo print versão pithon 2.x
print("Seja bem vindo(a) %s" % nome)
# Exemplo print versão pithon 3.x
print("Seja bem vindo(a) {0}".format(nome))
# Exemplo print versão pithon 3.7
print(f"Seja bem vindo(a) {nome}")

# Segunda entrada de dados
print("Qual é sua idade ? ")
idade = input()

# Exemplo print versão pithon 2.x
print("Então o %s tem %s anos de idade !" % (nome, idade))
# Exemplo print versão pithon 3.x
print("Então o {0} tem {1} anos de idade !".format(nome, idade))
# Exemplo print versão pithon 3.7
print(f"Então o {nome} tem {idade} anos de idade !")

# Exemplo print versão pithon 2.x
print("então você nasceu em %s" % (anoatual - int(idade)))
# Exemplo print versão pithon 3.x
print("então você nasceu em {0}".format(anoatual - int(idade)))
# Exemplo print versão pithon 3.7
print(f"então você nasceu em {anoatual - int(idade)}")

idade = int(idade)
# Exemplo print versão pithon 2.x
print("então você nasceu em %s" % (anoatual - idade))
# Exemplo print versão pithon 3.x
print("então você nasceu em {0}".format(anoatual - idade))
# Exemplo print versão pithon 3.7
print(f"então você nasceu em {anoatual - idade}")