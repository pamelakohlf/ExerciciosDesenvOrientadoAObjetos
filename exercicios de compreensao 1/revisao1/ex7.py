preco_aquisicao = float(input("Digite o valor de aquisição: "))

if preco_aquisicao <= 50:
    caso_menor = preco_aquisicao + preco_aquisicao * (45/100)
    print(f"O valor de revenda será de R${caso_menor}")

else:
    caso_maior = preco_aquisicao + preco_aquisicao * (30/100)
    print(f"O preço de revenda será de R${caso_maior}")
