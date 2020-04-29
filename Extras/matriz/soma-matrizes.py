def soma_matrizes(m1, m2):
    if len(m1) != len(m2) or len(m1[0])!=len(m2[0]):
        return False
    else:
        linhas = len(m1) # Conta quantas linhas existem
        colunas = len(m1[0]) # Conta quantos elementos têm em uma linha
        C = criar_matriz_zeros(linhas,colunas)
        
        for i in range(linhas):
            for j in range(colunas):
                C[i][j] = A[i][j] + B[i][j]
        return C
