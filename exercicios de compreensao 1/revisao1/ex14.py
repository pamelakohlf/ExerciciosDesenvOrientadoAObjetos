nota1 = float(input("Digite a primeira nota (entre 0.0 e 10.0): "))

if nota1 < 0.0 or nota1 > 10.0:
    print("Nota 1 inválida.")
else:
    nota2 = float(input("Digite a segunda nota (entre 0.0 e 10.0): "))
    if nota2 < 0.0 or nota2 > 10.0:
        print("Nota 2 inválida.")
    else:
        media = (nota1 + nota2) / 2
        print("A média das notas é:", media)