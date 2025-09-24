#Entradas

valor = float(input("Insira o valor da sua hora: "))
horas = int(input("Insira a quantidade de horas trabalhadas no mês: "))

salario = valor*horas

if salario <= 900:
            ir = 0
            porcentagem = 0
if salario <=1500:
    ir = salario*0.05
    porcentagem = 5
if salario <=2500:
    ir = salario *0.1
    porcentagem = 10
else:
    ir = salario*0.20
    porcentagem = 20

inss = salario*0.1
sindicato = salario*0.03
fgts = salario*0.11

desconto = ir+inss+sindicato

liquido = salario - desconto

print(f'Salário bruto = {salario}')
print(f"Inss = {inss}")
print(f"FGTS = {fgts}")
print(f"Desconto = {desconto}")