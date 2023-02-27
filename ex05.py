string = input('Entre com a string desejada: ')
stringInvertida = ''
tamanho = len(string) - 1

for i in range(tamanho, -1, -1):
    stringInvertida += string[i]

print(f'A string "{string}" invertida fica como: "{stringInvertida}"')
