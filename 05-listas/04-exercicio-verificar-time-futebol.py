# Crie um programa em Python que tenha uma lista com alguns times de futebol.
times = ["Corinthians", "Palmeiras", "Santos", "São Paulo"]

# Peça para o usuário digitar o nome de um time.
time = input("Digite o nome de um time: ")

# Verifique se o time digitado está na lista.

# Se estiver, mostre:
# "Esse time está na lista!"

# Caso contrário, mostre:
# "Esse time não está na lista!"

if time in times:
    print(f"{time} está na lista!")
else:
    print(f"{time} não está na lista!")