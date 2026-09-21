# Cria um programa que percorra os números de 1 a 10 
# e mostre se cada número é par ou ímpar.
# % 2 == 0
numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in range(1, 11): 
    if numero % 2 == 0:
        print(numero, "é par!")
    else:
        print(numero, "é ímpar!")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")

for numero in numeros: 
    if numero % 2 == 0:
        print(numero, "é par!")
    else:
        print(numero, "é ímpar!")