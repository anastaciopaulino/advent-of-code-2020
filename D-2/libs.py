# Aqui estão todas as funções que eu usei nos desafios
# Separei elas por uma questão de organização
import re

# Função para gerar uma lista com as letras da expressão
def latterByLatter(latter):
    count = 0
    latter_list = []

    # Precorrendo cada caracter de uma palavra
    # E adicionando ela em uma lista
    while(count < len(latter)):
        latter_list.append(latter[count])
        count += 1

    return latter_list

# Função para formatar os dados(politicas de senhas)
def formatarPoliticas(filename):

    # Abrindo o arquivo onde estão os dados
    file = open(filename, 'r+')

    politicas = []

    # Precorrendo as linhas desse arquivo
    for line in file.readlines():

        # Usando expressões regulares para encontrar padrões 
        # e depois criar um dicionário

        quantidade = re.search(r'\d*-\d*', line)
        caracter = re.search(r'([a-z]|[A-Z])', line)
        expressao = re.search(r':.*', line)

        politicas.append({'quantidade': quantidade.group(),
                        'caracter': caracter.group(),
                        'expressao': expressao.group()})
        
    return politicas

