
soma_dos_quadrados = 0
soma = 0


for i in range(1, 101):
    soma_dos_quadrados += i ** 2
    soma += i

quadrado_da_soma = soma ** 2
diferenca = quadrado_da_soma - soma_dos_quadrados


print(f"Soma dos quadrados: {soma_dos_quadrados}")
print(f"Quadrado da soma: {quadrado_da_soma}")
print(f"Resultado final (diferença): {diferenca}")
