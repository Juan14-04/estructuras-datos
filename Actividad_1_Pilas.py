class Canasta:
    def init(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        limite = 10
        if len(self.items) < limite:
            self.items.append(item)
            print("Prenda agregada:", item)
        else:
            print("La canasta está llena")

    def pop(self):
        if not self.isEmpty():
            prenda = self.items.pop()
            print("Prenda eliminada:", prenda)
        else:
            print("La canasta está vacía")

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


canasta = Canasta() 

while True:
    operador = input("¿Qué operador desea utilizar? (push, pop, peek, isEmpty, salir): ")

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
