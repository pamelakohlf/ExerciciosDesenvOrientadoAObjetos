print("Cálculo de resistência equivalente em paralelo (digite 0 para encerrar)")

while True:
    R1 = float(input("\nDigite o valor de R1 (Ω): "))
    R2 = float(input("Digite o valor de R2 (Ω): "))

    if R1 == 0 or R2 == 0:
        print("Encerrando o programa...")
        break

    Req = (R1 * R2) / (R1 + R2)
    print(f"Resistência equivalente: {Req:.2f} Ω")
