# Faça um programa que peça o nome de um time de futebol,
# a quantidade de vitórias e empates.
# Sabendo que cada vitória vale 3 pontos e cada empate vale 1 ponto,
# calcule e mostre a pontuação total do time.

# Entrada de dados
time = input("Digite o nome do seu time: ")
vitorias = int(input("Digite a quantidade de vitórias: "))
empates = int(input("Digite a quantidade de empates: "))

# Processamento computacional
pont_vit = vitorias * 3 
pont_emp = empates * 1
pont_total = pont_vit + pont_emp

# Saída de infotmações
print(f"Seu time é o: {time}")
print(f"Atualmente ele está com: {vitorias} vitorias e {empates} empates")
print(f"No total ele tem {pont_vit} pontos de vitoria , {pont_emp} pontos de empate e {pont_total} ao todo")