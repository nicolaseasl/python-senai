# Entrada de dados básicos
nome = input("Informe seu nome: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota"))

# Processamento compuacional
media = (n1 + n2) / 2

# Saída de informações
print(f"Aluno: {nome} ")
# Formatação com uma casa decimal 
# f -> significa número de ponto flutuante (decimal)
# .1 -> siginifica mostrar 1 casa decimal 
print(f"Média Final: {media: .1f}")

