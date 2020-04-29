tipo_de_jogo = 0


def computador_escolhe_jogada(n, m):
    
    if n <= m:
        return n
    else:
        peças_restantes = n % (m+1)
        
        if peças_restantes > 0:
            return peças_restantes
        else:
            return m

def usuario_escolhe_jogada(n, m):
       
    jogada = 0
    
    while jogada == 0:
        
        jogada = int(input("Quantas peças você vai tirar? "))

        if (jogada > n or jogada < 1 or jogada > m):
            print("")
            print ("Oops! Jogada inválida! Tente de novo.")
            print("")
            jogada = int(input("Quantas peças você vai tirar? "))
            print("")

    return jogada

def partida():
    print(" ")
    n = int(input("Quantas peças? "))
    m = int (input("Limite de peças por jogada? "))
    print ("")

    vez_do_computador = True

    if (n % (m + 1) == 0):
        vez_do_computador = False
        print ("Voce começa!")
        print ("")
    else:
        print ("Computador começa!")
        print ("")

    while n > 0:
        
        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            vez_do_computador = False
            print("O Computador tirou {} peças.".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            vez_do_computador = True
            print("Você tirou {} peças.".format(jogada))
            
        n = n - jogada

        if (n == 0):
            print ("")
        else:
            print("Agora restam {} peças no tabuleiro.\n".format(n))
        
    if vez_do_computador:
        print("Fim do jogo! Você ganhou!")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!")
        return 0

def campeonato():
    
    jogador_vitima = 0
    computador = 0

    i = 0
    while (i < 3):
        i = i + 1

        if (i == 1):
            print ("Primeira rodada")
        if (i == 2):
            print ("Segunda rodada")
        if (i == 3):
            print ("Terceira rodada")
                
        vencedor = partida()
        
        if vencedor == 1:
            jogador_vitima = jogador_vitima + 1
        else:
            computador = computador + 1

    print ("")        
    print("Placar: Você  {} x {}  Computador".format(jogador_vitima, computador))

while tipo_de_jogo == 0:
    
    print ("Bem-vindo ao jogo do NIM! Escolha:")
    print(" ")
    print ("1 - para jogar uma partida isolada")
    print ("2 - para jogar um campeonato")
    
    tipo_de_jogo = int(input("Digite a sua escolha: "))
    print(" ")

    if tipo_de_jogo == 1:
        print("Voce escolheu partida isolada!")
        partida()
        break
    if tipo_de_jogo == 2:
        print("Voce escolheu um campeonato!")
        campeonato()
        break
