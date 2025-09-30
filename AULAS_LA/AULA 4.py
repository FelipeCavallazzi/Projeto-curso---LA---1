#funçõs

a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
c=0

def soma(a, b):
    return a + b

def main():
    a = int(input('digite valor de a: '))
    b = int(input('digite valor de b: '))

    d = soma(a, b)
    e = d + 1

    print("Soma:", d)
    print("Soma + 1:", e)

if __name__ == '__main__':
    main()