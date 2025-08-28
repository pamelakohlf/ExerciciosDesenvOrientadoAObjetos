ano_inicial = 2019
salario = 4000.00
aumento = 1.5 / 100  
ano_atual = 2025
for ano in range(2020, ano_atual + 1):
    salario += salario * aumento  
    aumento *= 2 
print(f"O salário atual do funcionário em {ano_atual} é R$ {salario:.2f}")
