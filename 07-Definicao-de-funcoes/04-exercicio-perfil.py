# Crie uma função exibir_perfil() que receba o nome, a idade e o tipo de conta de um utilizador. 
# O tipo de conta deve ter "Gratuito" como valor padrão. 
# Teste a função com e sem informar o tipo de conta.

# Utilizador: Ana Silva | Idade: 28 | Plano: Gratuito
# Utilizador: João Santos | Idade: 35 | Plano: Premium

inputNome = input("Digite seu nome: ")
inputIdade = input("Digite sua idade: ")


def exibir_perfil(nome, idade, plano = "Gratuito"):
    perfil = f"Utilizador: {nome} | Idade: {idade} | Plano: {plano}"
    print(perfil)

exibir_perfil(inputNome, inputIdade)
exibir_perfil("Nicolas", 17, "Premium")
