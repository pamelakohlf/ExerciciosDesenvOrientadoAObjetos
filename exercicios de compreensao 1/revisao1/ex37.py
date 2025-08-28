'''37. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos
dê:
- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:
IR (11%) INSS (8%) Sindicato (5 %)
- Salário Bruto : R$
- Salário Líquido: R$
Obs.: Salário Bruto - Descontos = Salário Líquido. '''

horavalor = float(input('Digite o valor da sua hora: '))

horatrab = float(input('Quantas horas trabalhou: '))

salariob = horavalor * horatrab

IR = (salariob * 0.11)
INSS = (salariob * 0.08)
sind = (salariob * 0.05)

salarioliq = salariob - (IR + INSS + sind)

print(f'Seu salário bruto: {salariob}\nSalário líquido: {salarioliq}\n - DESCONTOS - \nIR: {IR}\nINSS: {INSS}\nSindicato: {sind}')