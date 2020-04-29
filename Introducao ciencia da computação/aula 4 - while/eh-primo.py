numero = int(input("Digite um número inteiro: "))

i = 2

while (i < numero):
    if (not (numero % i == 0)):
    numeroeprimo = numero
    i = i + 1

if (numero == numeroeprimo):
    print ("primo")
else:
    print ("não primo")
