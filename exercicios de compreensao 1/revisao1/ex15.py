
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))


valor_hora = 40.50
salario_bruto = horas_trabalhadas * valor_hora


if salario_bruto > 2500:
    imposto_renda = salario_bruto * 0.11
else:
    imposto_renda = 0


salario_liquido = salario_bruto - imposto_renda


print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Imposto de renda: R$ {imposto_renda:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")