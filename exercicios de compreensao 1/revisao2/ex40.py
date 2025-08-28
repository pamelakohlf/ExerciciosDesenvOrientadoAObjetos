print("Menu de opções:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Sair")

opcao = int(input("Escolha uma opção: "))

if opcao == 5:
    print("Programa encerrado.")
else:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        print("Resultado:", num1 + num2)
    elif opcao == 2:
        print("Resultado:", num1 - num2)
    elif opcao == 3:
        print("Resultado:", num1 * num2)
    elif opcao == 4:
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Não é possível dividir por zero.")
    else:
        print("Opção inválida.")
