votos = [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
 
print ("Enquete: Quem foi o melhor jogador?")        
 
i = 1
while i != 0:
    voto = int(input("Numero do jogador (0=fim)---> "))
    if voto == 0:
        i = voto
    else:
        votos[voto - 1] = votos[voto - 1] + 1
        i = i
 
print ("\nResultado da votacao")
 
i = 0
while i < len(votos):
    print ("Camisa numero",(i+1),"--->",votos[i],"votos")
    i = i + 1
