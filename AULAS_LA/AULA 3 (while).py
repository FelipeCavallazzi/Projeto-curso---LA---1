#3

lado_a=int(input("Insira o valor de um lado: "))
lado_b=int(input("Insira o valor de um lado: "))
lado_c=int(input("Insira o valor de um lado: "))

MAIOR=max(lado_a , lado_b, lado_c)

if (lado_a> lado_b> lado_c):
    lado_a = maior
    if(lado_b>lado_c):
        lado_b = maior
    else:
        lado_c = maior



if (lado_a <= 0 or lado_b <= 0 or lado_c <= 0):
    print("Os lados devem ser maiores que zero.")
elif (lado_a + lado_b <= lado_c) or (lado_a + lado_c <= lado_b) or (lado_b + lado_c <= lado_a):
    print("Os valores informados não formam um triângulo.")
else:

    if lado_a == lado_b == lado_c:
        print("O triângulo é equilátero.")
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("O triângulo é isósceles.")
    else:
        print(f"O triângulo é escaleno e seu maior lado é {MAIOR}.")