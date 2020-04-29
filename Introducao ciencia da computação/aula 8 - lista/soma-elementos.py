def soma_elementos():

    n = int(input("Digite o número de termos da lista: "))

    lista = []
    i = 1
    
    while i <= n:
        x = int(input("Digite o número: "))
        lista.append(x)
        i = i + 1
        
    soma = 0
    for elemento in lista:
        soma = soma + elemento
    return soma

