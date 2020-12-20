from libs import latterByLatter as LatterByLatter, formatarPoliticas
import re

# Contador de Possibilidades positivas
politicas_certas = 0

# Politicas
politicas = formatarPoliticas('politica de senhas.txt')

# Precorrendo os dados
for item in politicas:
    # Formatando a quantidade de digito
    # Tornando elas em listas do tipo: [menor, maior]
    item['quantidade'] = item['quantidade'].split('-')

    latterByLatter = LatterByLatter(item['expressao'])

    if latterByLatter.count(item['caracter']) >= int(item['quantidade'][0]) and latterByLatter.count(item['caracter']) <= int(item['quantidade'][1]):
        politicas_certas += 1

print('Tem: ', politicas_certas)