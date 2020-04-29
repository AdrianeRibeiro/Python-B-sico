print ("OLÁ, BEM VINDO AO SISTEMA DE VENDAS DE PASSAGENS!")
print ("Preço da Passagem = R$ 5.00")
print ("Crianças menores que cinco anos e idosos maiores que 65 pagam meia.")
print ()

n = 4
janela1 = [0] * n
corredor1 = [0] * n
janela2 = [0] * n
corredor2 = [0] * n
total_poltronas = (len(janela1) + len(corredor1) + len(janela2) + len(corredor2))

print ("O ônibus possui",total_poltronas, "poltronas:")
print ("JANELA1 = ", janela1)
print ("CORREDOR1 = ", corredor1)
print ("JANELA2 = ", janela2)
print ("CORREDOR2 = ", corredor2)


i = 0
contador_meia = 0 # conta as meias passagens
contador_inteiro = 0 # conta as passagens inteiras
condicao = 0
while (condicao != 1):
    i = i + 1
    print ()
    print (i,"ª VENDA!", total_poltronas, "POLTRONAS")
    total_poltronas = total_poltronas - 1
        
    print ()
    idade = int(input("Escolha: 1-MEIA PASSAGEM ou 2-PASSAGEM NORMAL "))
    if (idade == 1):
        contador_meia = contador_meia + 1
    else:
        contador_inteiro = contador_inteiro + 1

    fileira = int(input ("Escolha uma Fileira: 1-JANELA1 2-CORREDOR1 3-JANELA2 4-CORREDOR2 ")) 
    escolha = int(input("Escolha uma POLTRONA: "))

    cond = 0
    while (cond == 0):
        if (fileira == 1):
            if (janela1[escolha] == 0):
                janela1[escolha] = 1
                cond = 1
            elif (janela1[escolha] == 1):
                print ("Escolha inválida. Poltrona OCUPADA.")
                escolha = int(input("Escolha OUTRA Poltrona: "))
        elif (fileira == 2):
            if (corredor1[escolha] == 0):
                corredor1[escolha] = 1
                cond = 1
            elif (corredor1[escolha] == 1):
                print ("Escolha inválida. Poltrona OCUPADA.")
                escolha = int(input("Escolha OUTRA Poltrona: "))
        elif (fileira == 3):
            if (janela2[escolha] == 0):
                janela2[escolha] = 1
                cond = 1
            elif (janela2[escolha] == 1):
                print ("Escolha inválida. Poltrona OCUPADA.")
                escolha = int(input("Escolha OUTRA Poltrona: "))
        elif (fileira == 4):
            if (corredor2[escolha] == 0):
                corredor2[escolha] = 1
                cond = 1
            elif (corredor2[escolha] == 1):
                print ("Escolha inválida. Poltrona OCUPADA.")
                escolha = int(input("Escolha OUTRA Poltrona: "))    

    if (total_poltronas > 0):
        condicao = int(input("Deseja continuar a vender? 0-SIM ou 1-NÃO "))
    else:
        print ()
        print ("TODAS AS POLTRONAS FORAM VENDIDAS!")
        condicao = 1

preco = 5.00
passagens_vendidas = contador_meia + contador_inteiro
faturamento = ((contador_meia * (preco/ 2)) + (contador_inteiro * preco))

print ()
print ("JANELA1 = ", janela1)
print ("CORREDOR1 = ", corredor1)
print ("JANELA2 = ", janela2)
print ("CORREDOR2 = ", corredor2)

total_poltronas = (len(janela1) + len(corredor1) + len(janela2) + len(corredor2))

print ()
if ((passagens_vendidas) < (total_poltronas/ 2)):
    print ("Número de passagens vendidas = ", passagens_vendidas)
    print ("A viagem foi CANCELADA! Poucos passageiros.")
else:
    print ("Viagem CONFIRMADA! ")
    print ("Número de passagens vendidas = ", passagens_vendidas)
    print ("Faturamento = R$ ", faturamento)