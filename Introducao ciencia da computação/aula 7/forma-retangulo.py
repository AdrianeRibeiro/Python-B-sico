largura = int(input("digite a largura:"))
altura = int(input("digite a altura:"))

l = 1
a = 1
while a <= altura:
    while l < largura:
        print ("#", end = "")
        l = l + 1
    print ("#")
    a = a + 1
    l = 1
