# 18 anos ou mais: Pode entrar na festa.
# 16 ou 17 anos: Pode entrar com responsável.
# Menos de 16 anos: Não pode entrar na festa.

# Entrada de dados
idade = int(input("Digite sua idade: "))

# Verificação 
if idade >= 18:
    print("Pode entrar na festa.")
elif idade < 16:
    print("Não pode entrar na festa.")
else:
    print("Pode entrar com responsável.")