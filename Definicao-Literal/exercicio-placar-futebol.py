# Objetivo:
# Praticar variáveis, números inteiros, operações matemáticas e f-strings.

# Descrição:
# Crie um programa que represente o resultado de uma partida de futebol.
#  O programa deve armazenar o nome de dois times 
#  e a quantidade de golos marcados por cada equipa.

time1 = "Brasil"
time2 = "Alemanha"

gols1 = 1
gols2 = 7

total_gols = gols1 + gols2

# Depois, apresente o placar e calcule o total de golos da partida.

print("================================")
print("       RESULTADO DO JOGO        ")
print("================================")
print(f"{time2} {gols2} x {gols1} {time1}")
print(f"Total de gols: {total_gols}")
print("================================")

# Resultado no terminal
# ================================
#         RESULTADO DO JOGO
# ================================
# França 3 x 2 Espanha
# Total de gols: 5
# ================================