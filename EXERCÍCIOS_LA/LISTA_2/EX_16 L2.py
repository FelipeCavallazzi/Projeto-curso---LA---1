a = float(input("Insira o valor de a: "))
if a == 0:
    print("Se a = 0 a equação não é de segundo grau. ")
elif a !=0:
    b = float(input("Insira o valor de b: "))
    c = float(input("Insira o valor de c: "))



delta = (b**2)-4*a*c
if delta<0:
    print("A equação não tem raíz pois delta é menor que 0.")
else:
    raiz_um =  (-b+delta**0.5)/2*a
    raiz_dois =  (-b-delta**0.5)/2*a

    if delta==0:
        print("Há apenas uma raiz.")
        print(f"Raíz um = {raiz_um} ")
    else:
         print("Há mais que uma raíz.")
