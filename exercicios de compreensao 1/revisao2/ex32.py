consoantes = []
for i in range(10):
    letra = input("Digite uma letra: ").lower()
    if letra not in ['a', 'e', 'i', 'o', 'u']:
        consoantes.append(letra)
print("Consoantes digitadas:", consoantes)
print("Quantidade de consoantes:", len(consoantes))
