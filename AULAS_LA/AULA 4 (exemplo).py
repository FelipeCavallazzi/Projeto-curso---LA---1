#aula
#funcao
#rede neural

#Imports
import numpy as np

X=np.random.rand(5)
W=np.random.rand(5)
b=1
v=0
beta=0.25
a=0

def juncaoAditiva():
    u=0


    for i in range(len(X)):
        v=X[i]*W[i]
        u=u+v


    u=u-b
    return u

def main():
    z=juncaoAditiva()
    a= -1 *beta*z
    y= 1/(1+(np.exp(a)))
    print(f"A saída do neurônio é: {y}")
    if (z>=0):
        y=1
        print(f"A rede neural foi ativada com valor igual a: {y}")
    elif(z<0):
        y=0
        print(f"A rede neural foi desativada com valor igual a: {y}")

if __name__ == "__main__":
    main()