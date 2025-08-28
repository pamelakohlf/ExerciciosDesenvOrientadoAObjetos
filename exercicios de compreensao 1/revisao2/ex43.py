
nome = input('Digite seu nome: ')
i = 1
notas = []

for cont in range(7):
    nota = float(input(f'Digite a nota {i}: '))
    notas.append(nota)
    i += 1



min = min(notas)
max = max(notas)

notas.remove(min)
notas.remove(max)      

media = sum(notas) / len(notas)

print(f'\nResultado final:\nAtleta: {nome}\nMelhor nota: {max}\nPior nota: {min}\nMédia: {media}')