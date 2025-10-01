while True:
    um = float(input("Insira o primeiro número: "))
    dois = float(input("Insira o segundo número: "))
    op = input("Qual a operação que deve ser realizada? ")

#Cálculos do result
    if op not in ("+", "-", "*", "/"):
        print("Operação inválida! Tente novamente. ")
        continue

    if op == ("+"):
        result = um + dois

    elif op == ("-"):
        result = um - dois

    elif op == ("*"):
        result = um * dois
    elif op == ("/"):
         result = um / dois



#Ver inteiro
    if result == int(result):
         a = (f"{result} é inteiro")
    else:
        a = (f"{result} é decimal")

#Ver positivo
    if result >0:
        b = ("positivo")
    elif result == 0:
        b = ("nulo")
    else:
        b = ("negativo")

#Ver par
    if result%2>0:
        c = (f"ímpar. ")
    else:
        c  = (f"par. ")

    print(f"{a}, {b} e {c}")
    break
