# Cria um programa que permita ao utilizador fazer vários pedidos numa lanchonete.
itens = []
quantidade = 0
# O programa deve pedir ao utilizador o nome de um produto.
produto = input("Digite o produto que deseja pedir: ")
# Enquanto o utilizador não escrever sair, o programa deve continuar a pedir novos produtos.
while produto != "sair":
    itens.append(produto)

    produto = input("Digite o produto que deseja pedir: ")
    quantidade = quantidade + 1

# Quando o utilizador escrever sair, o programa deve mostrar:

#   .Quantos produtos foram pedidos;
#   .Uma mensagem a indicar que o pedido foi finalizado.

print("\n")
print("Pedido finalizado!")
print("Você pediu", quantidade, "produtos.")
# Digite o produto que deseja pedir: hambúrguer
# Digite o produto que deseja pedir: batata
# Digite o produto que deseja pedir: refrigerante
# Digite o produto que deseja pedir: sair

# Pedido finalizado!
# Você pediu 3 produtos.
