dia = int(input("Insira o dia: "))
if dia>31 or dia<1:
    print("Data inválida.")
else:
    mes = int(input("Insira o mês: "))
if mes>12 or mes<1:
    print("Data inválida.")
elif mes>12 or mes>0:
    ano = int(input("Insira o ano: "))

if mes==2 and dia>29 and (ano%4 == 0 and ano%100 != 0) or (ano%400 == 0):
    print(f"Data inválida.")
else:
    print(f"{dia}/{mes}/{ano}")

if mes == 2 and dia>28 and (ano%4 != 0 and ano%100 == 0) or (ano%400 != 0):
    print("Data inválida.")
else:
    print(f"{dia}/{mes}/{ano}")

if mes == 4 or mes == 6 or mes == 8 or mes == 11 and dia>30:
    print("Data inválida.")
else:
    print(f"{dia}/{mes}/{ano}")



