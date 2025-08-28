idade = int(input("Digite a idade: "))
tempo_servico = int(input("Digite o tempo de serviço (em anos): "))

if idade >= 65:
    print("Pode se aposentar (por idade).")
elif tempo_servico >= 30:
    print("Pode se aposentar (por tempo de serviço).")
elif idade >= 60 and tempo_servico >= 25:
    print("Pode se aposentar (idade + tempo de serviço).")
else:
    print("Não pode se aposentar.")
