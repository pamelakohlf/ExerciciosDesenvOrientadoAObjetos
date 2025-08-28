#Crie um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
#utilizando as seguintes formulas (onde h corresponde à altura):
#• Homens: (72.7∗ h)−58
#• Mulheres: (62,1∗ h)−44,7

alt = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo (H ou M): ")

if sexo == 'H':
    alt_ideal = (72.7 * alt) - 58
    print(f'Sua altura ideal é de: {alt_ideal}')
elif sexo == 'M':
    alt_ideal = (62.1 * alt) - 44.7
    print(f'Sua altura ideal é de: {alt_ideal}')