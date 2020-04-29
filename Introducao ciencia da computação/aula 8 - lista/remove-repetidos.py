def remove_repetidos ():

    n = int(input("Digite o número de termos da lista: "))

    lista = []
    i = 1
    
    while i <= n:
        x = int(input("Digite o número: "))
        lista.append(x)
        i = i + 1

    nova_lista = list(set(lista))
    nova_lista.sort()
    return nova_lista
