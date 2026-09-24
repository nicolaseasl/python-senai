# Crie uma lista vazia para armazenar nomes.
nomes = []

# Use um for para pedir 3 nomes ao usuário.
for nome in range(3) :
    nome = input("Digite um nome: ")

# A cada nome digitado, adicione o nome na lista usando append().
    nomes.append(nome)

# Separe as linhas (isso fui eu q add só pra ficar bonito)
print(f"\n")

# No final, mostre todos os nomes cadastrados.
print("Nomes cadastrados: ", nomes)

print(f"\n")

for nome in nomes:
    print("-", nome)