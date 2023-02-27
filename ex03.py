import json

with open("dados.json", encoding='utf-8') as exercicio_json:
    dados = json.load(exercicio_json)

valor = []

for i in range(0, len(dados)):
    valor.append(dados[i]["valor"])

menor = valor[0]
maior = valor[0]
media = 0
cont = 0

for i, dados in enumerate(valor):
    if dados > 0:
        media += dados
        cont += 1
        if dados < menor:
            menor = dados
        if dados > maior:
            maior = dados

media /= cont

numDias_superiorMedia = 0

for dados in valor:
    if dados > media:
        numDias_superiorMedia += 1

print(f'O menor valor encontrado é: {menor}')
print(f'O maior valor encontrado é: {maior}')
print(
    f'O número de dias com faturamento acima da média é: {numDias_superiorMedia}')
