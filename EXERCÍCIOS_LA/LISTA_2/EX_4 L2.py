while True:
    letra = input("Insira uma letra: ")

    if len(letra)>1:
        print(f"{letra} não é uma letra. ")
        continue

    if letra.lower() not in ("a","e","i","o","u"):
        print(f"{letra.capitalize()} é consoante.")
    else:
        print(f"{letra.capitalize()} é vogal.")
    break