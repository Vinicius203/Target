faturamentoEstados = [('SP', 67836.43), ('RJ', 36678.66),
                      ('MG', 29229.88), ('ES', 27165.48), ('Outros', 19849.53)]

faturamentoTotal = 0

for i in range(0, len(faturamentoEstados)):
    faturamentoTotal += faturamentoEstados[i][1]

for i in range(0, len(faturamentoEstados)):
    porcentagem = (faturamentoEstados[i][1] * 100) / faturamentoTotal
    print(
        f'A porcentagem da representação do estado {faturamentoEstados[i][0]} foi de: {porcentagem:.2f}%.')
