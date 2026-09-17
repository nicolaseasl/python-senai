# Crie um programa que solicite o nome de um produto, 
# seu preço e a quantidade comprada. Depois, calcule o valor total da compra
# e exiba o nome do produto e o valor total.

# Entrada de dados 
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite quantos serão comprados: "))

#Processamento computacinal
valor_total = preco * quantidade

#Saída de informações
print(f"{produto}: R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total: {valor_total:.2f}")