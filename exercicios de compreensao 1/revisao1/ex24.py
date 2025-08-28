def tri(a,b,c):
  if a + b > c and a + c > b and b + c > a:
    print("São lados de um triangulo")
    if a == b and b == c:
      print("Equilátero")
    elif a == b or a == c or b == c:
      print("Isósceles")
    elif a != b and b != c:
      print("Escaleno")
  else:
    print("Não são lados de um triangulo")

tri(1,1,3)  # <- digite os numeros aqui