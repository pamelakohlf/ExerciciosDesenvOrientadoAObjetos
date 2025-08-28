
custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))


if custo_fabrica <= 12000:
    perc_distribuidor = 0.05
    perc_impostos = 0
elif custo_fabrica <= 25000:
    perc_distribuidor = 0.10
    perc_impostos = 0.15
else:
    perc_distribuidor = 0.15
    perc_impostos = 0.20

comissao = custo_fabrica * perc_distribuidor
impostos = custo_fabrica * perc_impostos
custo_consumidor = custo_fabrica + comissao + impostos


print(f"\nResumo do custo:")
print(f"Custo de fábrica: R$ {custo_fabrica:.2f}")
print(f"Comissão do distribuidor: R$ {comissao:.2f}")
print(f"Impostos: R$ {impostos:.2f}")
print(f"Custo ao consumidor: R$ {custo_consumidor:.2f}")
