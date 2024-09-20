class Animal:
    def __init__(self, nombre:str, raza:str, peso: float, edad: int, tipo:str, sexo:str):
        self.nombre = nombre
        self.raza = raza
        self.peso = peso
        self.edad = edad
        self.tipo = tipo
        self.sexo = sexo

    def __eq__(self, duplicado):
        return self.nombre == duplicado.nombre and self.tipo == duplicado.tipo
    
    def __str__(self):
        return f"El animal {self.nombre} de raza {self.raza} pesa {self.peso} kg, edad de {self.edad} años, tipo {self.tipo} y sexo {self.sexo}"


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class Lista:
    def __init__(self):
        self.objeto = None

    def imprimirLista(self):
        actual = self.objeto
        while actual is not None:
            print(actual.data)
            actual = actual.next

    def agregarAnimal(self, item):
        actual = self.objeto
        while actual is not None:
            if actual.data == item: 
                print(f"El animal {item.nombre} ya existe en la lista.")
                return
            actual = actual.next
        
        newNode = Node(item)
        if self.objeto is None:
            self.objeto = newNode
        else:
            actual = self.objeto
            while actual.next is not None:
                actual = actual.next
            actual.next = newNode


animal1 = Animal("Gabriel", "Chihuahua", 5.2, 3, "Perro", "Masculino")
animal2 = Animal("Juan", "Grizzly", 300, 9, "Oso", "Masculino")
animal3 = Animal("Josefa", "Chimpance", 50.2, 7, "Mono", "Femenino")

lista_animales = Lista()
lista_animales.agregarAnimal(animal1)
lista_animales.agregarAnimal(animal2)
lista_animales.agregarAnimal(animal3)

lista_animales.imprimirLista()
