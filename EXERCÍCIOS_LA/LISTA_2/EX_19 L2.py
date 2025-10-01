num = int(input("Insira um número inteiro menor que 1.000: "))
if num>1000:
    print("Número inválido.")
else:
    centena = num//100
    dezena = (num%100)//10
    unidade = num%10

    lista = []

    if centena>0:
        lista.append(f"{centena} centenas")

    if dezena>0:
        lista.append(f"{dezena} dezenas")

    if unidade>0:
        lista.append(f"{unidade} unidades")

    if num == 0:
        lista.append("0 unidades ")

        if len(lista)>1:
            resultado = ", ".join(lista[:-1]) + " e " + lista[-1]
        else:
            resultado = lista[0]

        print(f"{num} = {resultado}")
