'''33. Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao
vendedor. Para calcular a comissão, considere a tabela abaixo:
Venda mensal Comissão
Maior ou igual a R$100.000,00 R$700,00 + 16% das vendas
Menor que R$100.000,00 e maior ou igual a R$80.000,00 R$650,00 +14% das vendas
Menor que R$80.000,00 e maior ou igual a R$60.000,00 R$600,00 +14% das vendas
Menor que R$60.000,00 e maior ou igual a R$40.000,00 R$550,00 +14% das vendas
Menor que R$40.000,00 e maior ou igual a R$20.000,00 R$500,00 +14% das vendas
Menor que R$20.000,00 R$400,00 +14% das vendas '''

vendas = float(input('Digite o valor das vendas totais: '))

if vendas >= 100000:
    comis = 700 + (0.16 * vendas) 
    print(f'Comissão: {comis:.2f}')
elif vendas < 100000 and vendas >= 80000:
    comis = 650 + (0.14 * vendas)
    print(f'Comissão: {comis:.2f}')
elif vendas < 80000 and vendas >= 60000:
    comis = 600 + (0.14 * vendas)
    print(f'Comissão: {comis:.2f}')
elif vendas < 60000 and vendas >= 40000:
    comis = 550 + (0.14 * vendas)
    print(f'Comissão: {comis:.2f}')
elif vendas < 40000 and vendas >= 20000:
    comis = 500 + (0.14 * vendas)
    print(f'Comissão: {comis:.2f}')
else:
    comis= 400 + (0.14 * vendas)
    print(f'Comissão: {comis:.2f}')