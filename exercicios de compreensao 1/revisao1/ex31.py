
cardapio = {
    100: ("Hot Dog", 1.20),
    101: ("Bauru", 1.30),
    102: ("X-Salada", 1.50),
    103: ("X-BACON", 1.20),
    104: ("X-Burguer", 17.00),
    105: ("Suco de Laranja", 9.50),
    106: ("Refrigerante", 6.00)
}


print("=== Cardápio ===")
for codigo, (item, preco) in cardapio.items():
    print(f"{codigo} - {item} - R$ {preco:.2f}")


codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade desejada: "))

if codigo in cardapio:
    item, preco = cardapio[codigo]
    total = preco * quantidade
    print(f"Você pediu {quantidade}x {item}(s). Total a pagar: R$ {total:.2f}")
else:
    print("Código inválido. Por favor, tente novamente.")
