# Pedir os números para o usuario
inputNumero1 = int(input("Digite um numero: "))
inputNumero2 = int(input("Digite outro numero: "))

# Função que apresenta calculo
def somar(numero1, numero2):
    soma = numero1 + numero2
    print(soma)

def subtrair(numero1, numero2):
    sub = numero1 - numero2
    print(sub)

def multiplicar(numero1, numero2):
    mult = numero1 * numero2
    print(mult)

def dividir(numero1, numero2):
    div = numero1 / numero2
    print(div)

# Soma
somar(inputNumero1, inputNumero2)
subtrair(inputNumero1, inputNumero2)
multiplicar(inputNumero1, inputNumero2)
dividir(inputNumero1, inputNumero2)
