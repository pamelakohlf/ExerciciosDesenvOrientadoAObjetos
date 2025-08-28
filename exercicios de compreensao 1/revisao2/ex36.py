inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))
if inicio > fim:
    print("Intervalo de valores inválido")
else:
    soma = 0
    for numero in range(inicio, fim + 1):
        if numero % 2 != 0:  
            soma += numero
    print("Soma dos ímpares neste intervalo:", soma)
