import math

def potencias_raiz():
    while True:
        try:
            numero = float(input("Digite o número: "))
        except ValueError:
          print("Entrada inválida. Digite um número inteiro.")
          continue

        if numero <= 0:
            break

        quadrado = numero ** 2
        cubo = numero ** 3
        raiz_quadrada = math.sqrt(numero)

        print(f"Número: {numero}")
        print(f"Quadrado: {quadrado:.2f}")
        print(f"Cubo: {cubo:.2f}")
        print(f"Raiz quadrada: {raiz_quadrada:.2f}")

potencias_raiz()