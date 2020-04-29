def eprimo (k):
    fator = 2
    if k == 2:
       return True

    while k % fator != 0 and fator <= k/2:
        fator = fator + 1
    if k % fator != 0:
        return True
    else:
        return False

