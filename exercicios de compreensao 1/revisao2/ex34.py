def funcao(num):
  if num <= 1:
    print("Número inválido. Digite um número maior que 1.")
  else:
    eh_primo = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            eh_primo = False
            break
        i += 1

    if eh_primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")

num = int(input("Digite um número inteiro maior que 1: "))
funcao(num)