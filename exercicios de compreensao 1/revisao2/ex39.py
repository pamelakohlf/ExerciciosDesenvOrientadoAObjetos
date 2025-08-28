import random

numero = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input("Tente adivinhar o número (entre 1 e 100): "))
    tentativas += 1

    if chute < numero:
        print("É maior.")
    elif chute > numero:
        print("É menor.")
    else:
        print(f"Acertou! O número era {numero}. Você tentou {tentativas} vez(es).")
        break