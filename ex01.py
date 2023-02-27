import json

with open("dados.json", encoding='utf-8') as exercicio_json:
    dados = json.load(exercicio_json)

indice = 13
soma = 0

for i, dic in enumerate(dados):
    if (i < indice):
        soma += dic['valor']

print(f'A soma é igual a: {soma:.4f}')
