#Declarações


#Entradas
salario=float(input("Insira o salário do colaborador: "))

if salario<=280.00:
    reajuste = salario+salario*0.2
    porcentagem = 20
if salario>280:
    reajuste = salario+salario*0.15
    porcentagem = 15
if salario>700:
    reajuste = salario+salario*0.10
    porcentagem = 10
if salario>1500:
    reajuste = salario+salario*0.05
    porcentagem = 5

aumento = salario*(porcentagem/100)

#Saída
print(f"Salário antes do reajuste: {salario}R$")
print(f"O percentual de aumento aplicado foi de {porcentagem}%")
print(f"O valor do aumento é de {aumento}R$")
print(f"O valor do novo salário é de {reajuste}R$")

