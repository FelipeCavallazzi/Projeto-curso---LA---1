kg_maca = float(input("Quantos quilos de maçã? "))
kg_morango = float(input("Quantos quilos de morango? "))

kg_total = kg_maca + kg_morango

if kg_maca<= 5:
    ppkg_maca=2.5
else:
    ppkg_maca=2.2


if kg_morango<=5:
    ppkg_morango = 1.8
else:
    ppkg_morango = 1.5

p_maca = kg_maca*ppkg_maca
p_morango = kg_morango*ppkg_morango

preco_i = p_maca+p_morango

if kg_total>8 or preco_i>25:
     preco_f = preco_i - (preco_i*0.1)
else:
    preco_f = preco_i

print(f"Cliente adquiriu {kg_maca}KG de maçã.")
print(f"Cliente adquiriu {kg_morango}KG de morango.")
print(f"Cliente deve pagar {preco_f}R$")



