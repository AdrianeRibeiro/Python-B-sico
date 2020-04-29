import math
x1 = float(input("Digite a primeira coordenada do primeiro ponto:"))
y1 = float(input("Digite a segunda coordenada do primeiro ponto:"))
x2 = float(input("Digite a primeira coordenada do segundo ponto:"))
y2 = float(input("Digite a segunda coordenada do segundo ponto:"))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) 

if (distancia >= 10):
    print ("longe")
else:
    print ("perto")
