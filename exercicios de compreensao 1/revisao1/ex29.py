'''9. Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um
percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:
CONSUMO (Km/l) MENSAGEM
menor que 8 ---Venda o carro!
entre 8 e 14 --Econômico!
maior que 12 --Super econômico! '''

km = float(input('Digite a distância em KM: '))

gas = float(input('Digite os L de gasolina consumidos: '))

cons = km / gas

if cons < 8:
    print(f'Venda o carro! KM/L: {cons}')
elif 8 <= cons <= 14:
    print(f'Econômico! KM/L: {cons}')
else:
    print(f'Super econômico! KM/L: {cons}')