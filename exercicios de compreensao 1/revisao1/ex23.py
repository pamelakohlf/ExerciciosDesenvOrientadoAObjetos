print("=== Mini Calculadora ===")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")


opcao = int(input("Escolha uma opção (1 a 4): "))

if opcao in [1, 2, 3, 4]:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = num1 + num2
        operacao = "+"
    elif opcao == 2:
        resultado = num1 - num2
        operacao = "-"
    elif opcao == 3:
        resultado = num1 * num2
        operacao = "*"
    elif opcao == 4:
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            exit()
        resultado = num1 / num2
        operacao = "/"

    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
else:
    print("Opção inválida. Programa encerrado.")
