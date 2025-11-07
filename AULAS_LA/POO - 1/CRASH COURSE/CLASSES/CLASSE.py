# Criando a classe dog

class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+ " está sentado.")
            #Simula um cachorro sentado

    def roll_over(self):
        print(self.name.title()+ " está rolando!")

# Criando instância

my_dog = Dog("natan", 10)
print("My dog's name is " + my_dog.name.title()+ ".")
print("My dog is "+ str(my_dog.age)+ " years old.")
my_dog.sit()
my_dog.roll_over()

#Apenas o nome da variável precisa ser diferente, os valores podem ser iguais

your_dog = Dog("luke", 8)
print("\nSeu cachorro é o "+ your_dog.name.title() + "." )
print("My dog is "+str(my_dog.age)+" years old.")
your_dog.sit()
your_dog.roll_over()

