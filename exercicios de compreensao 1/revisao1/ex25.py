'''25. Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida.
Escolha a opção:
1- Soma de 2 números.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero). '''


print('Escolha a opção:\n1- Soma de 2 números.\n2- Diferença entre 2 números (maior pelo menor).\n3- Produto entre 2 números.\n4- Divisão entre 2 números (o denominador não pode ser zero)')

opcao = int(input('Escolha a opção:'))

n1 = float(input("Digite o numero 1: "))
n2 = float(input("Digite o numero 2: "))

if opcao == 1:
    res = n1 + n2
    print(f'Resultado: {res}')
elif opcao == 2:
    if n1 > n2:
        res = n1 - n2
        print(f'Resultado: {res}')
    else:
        res = n2 - n1
        print(f'Resultado: {res}')
elif opcao == 3:
    res = n1 * n2
    print(f'Resultado: {res}')
elif opcao == 4:
    if n2 == 0:
        print('Denominador inválido.')
    else:
        res = n1 / n2
        print(f'Resultado: {res}')
else:
    print("Opção inválida.")