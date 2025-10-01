preco_g = 2.5
preco_a = 1.9

combustivel = input("Escolha entre álcool e gasolina. (A-álcool, G-gasolina)")


litros_a = float(input("Quantos litros de álcool? "))
litros_g = float(input("Quantos litros de gasolina? "))

if litros_a<=20:
    desconto_a=0.03*litros_a
else:
    desconto_a=0.05*litros_a

if litros_g<=20:
    desconto_g=0.04*litros_g
else:
    desconto_g=0.06*litros_g


total_a = (preco_a*litros_a)-desconto_a
total_g = (preco_g*litros_g)-desconto_g

print(total_a)
print(total_g)