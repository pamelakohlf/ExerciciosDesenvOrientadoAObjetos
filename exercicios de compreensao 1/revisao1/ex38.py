def calcular_raizes(a, b, c):
    if a == 0:  
        return "Não é equação de segundo grau"
    
    delta = b**2 - 4*a*c  
    
    if delta < 0:
        return "Não existe raiz"  
    elif delta == 0:
        raiz = -b / (2*a)  
        return f"Raiz única: {raiz}"
    else:
        raiz1 = (-b + delta**0.5) / (2*a)  
        raiz2 = (-b - delta**0.5) / (2*a)  
        return f"As raízes reais são: {raiz1} e {raiz2}"
    
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

resultado = calcular_raizes(a, b, c)
print(resultado)
