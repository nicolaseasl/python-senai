# Faça um programa em Python que peça o peso (kg) 
# e a altura (m) de um indivíduo. Calcule o IMC
# mostre a sua classificação:

# Menor que 18,5: abaixo do peso
# De 18,5 a 24,9: peso normal
# 25 ou mais: acima do peso

# Entrada de dados
kg = float(input("Digite seu peso: "))
m = float(input("Digite sua altura: "))

# Cálculo 
imc = kg / (m * m)

# Saída de informações
print(f"Seu imc é: {imc:.2f}")

if imc >= 25:
    print("Acima do peso")
elif imc < 18.5:
    print("Abaixo do peso")
else:
    print("Peso normal")