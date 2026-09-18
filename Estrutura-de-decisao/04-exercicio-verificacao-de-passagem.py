# Programa: Verificação de passagem

# Faça um programa em Python que peça a idade de uma pessoa
# e verifique se ela paga passagem inteira ou meia passagem.

# Idade menor ou igual a 12 → Meia passagem
# Idade maior que 12 → Passagem inteira

# Solicita idade 
idade = int(input("Digite sua idade: "))

# Verifica se paga 
if idade < 12 or idade >= 60:
    print("Meia Passagem")
else:
    print("Passagem Inteira")