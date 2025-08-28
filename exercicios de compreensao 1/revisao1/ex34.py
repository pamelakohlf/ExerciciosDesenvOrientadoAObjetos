salario = float(input("Digite o salário atual do funcionário: "))
tempo_servico = int(input("Digite o tempo de serviço (em anos): "))

reajuste = 0
bonus = 0

if salario <= 500:
    reajuste = 0.25
elif salario <= 1000:
    reajuste = 0.20
elif salario <= 1500:
    reajuste = 0.15
elif salario <= 2000:
    reajuste = 0.10
else:
    reajuste = 0  

if tempo_servico < 1:
    bonus = 0
elif 1 <= tempo_servico <= 3:
    bonus = 100
elif 4 <= tempo_servico <= 6:
    bonus = 200
elif 7 <= tempo_servico <= 10:
    bonus = 300
elif tempo_servico > 10:
    bonus = 500

if reajuste == 0 and bonus == 0:
    print("O funcionário não tem direito a nenhum aumento.")
else:
    salario_reajustado = salario + (salario * reajuste)
    salario_final = salario_reajustado + bonus
    print("Salário reajustado: R$", round(salario_reajustado, 2))
    print("Bônus: R$", bonus)
    print("Salário final: R$", round(salario_final, 2))
