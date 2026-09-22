# Crie uma lista com algumas comidas e seus respectivos tipos.

# Percorra a lista usando um for.

# Se o tipo da comida for "Doce", mostre o nome da comida.

# Resultado:

# Comida doce: Brigadeiro
# Comida doce: Pudim

comidas = [
    ["Pudim", "Doce"],
    ["Nuggets", "Salgada"],
    ["Limão", "Azeda"],
    ["Pizza", "Salgada"],
    ["Juju", "Doce"]
]

for comida in comidas:
    if comida[1] == "Doce":
        print("Comida doce: ", comida[0])