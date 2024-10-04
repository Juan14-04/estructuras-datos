class Canasta:
    def _init_(self):
        self.items = [] 
         
    # Creamos la funcion isEmpty que valida si esta vacio
    def isEmpty(self):
        return len(self.items) == 0

    # Creamos la funcion push para agregar prendas a la canasta
    def push(self, item):
        limite = 10
        # Validamos que no estemos agregando mas del limite
        if len(self.items) < limite:
            self.items.append(item)
            print("Prenda agregada:", item)
        else:
            print("La canasta está llena")

    #Creamos la funcion pop para eliminar la primera prenda en entrar a la canasta
    def pop(self):
        # Validamos que no este vacia la canasta para poder eliminar prendas
        if not self.isEmpty():
            prenda = self.items.pop(0)
            print("Prenda eliminada:", prenda)
        else:
            print("La canasta está vacía")

    # Creamps la funcion top para ver que prenda esta al final de la canasta
    def top(self):
        if not self.isEmpty():
            return self.items[-1] 
        else:
            print("La canasta está vacía")
            return None

    def mostrar(self):
        if not self.isEmpty():
            print("Contenido de la canasta:", self.items)
        else:
            print("La canasta está vacía")

# Instancie la clase canasta
canasta = Canasta() 


# Bucle para utilizar los operadodres
while True:
    # Input para obtener el operador a utilizar
    operador = input("¿Qué operador desea utilizar? (push, pop, peek, isEmpty, salir): ")

    # En estos if validamos que si se este eligiendo bien entre las opcuiones 
    if operador == 'push':
        prenda = input("Ingrese la prenda a agregar: ")
        canasta.push(prenda)

    elif operador == 'pop':
        canasta.pop()

    elif operador == 'peek':
        peek = canasta.top()
        if peek:
            print("Prenda en la cima:", peek)

    elif operador == 'isEmpty':
        if canasta.isEmpty():
            print("La canasta está vacía")
        else:
            print("La canasta no está vacía")

    elif operador == 'salir':
        print("Se salio de la canasta")
        canasta.mostrar()
        break

    else:
        print("Operador no válido")
