n = 100
soma_dos_quadrados = sum(i**2 for i in range(1, n+1))
quadrado_da_soma = sum(range(1, n+1)) ** 2
diferenca = quadrado_da_soma - soma_dos_quadrados
print(f"A diferença entre a soma dos quadrados e o quadrado da soma dos primeiros {n} números naturais é {diferenca}")