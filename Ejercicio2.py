class Tarea:
    def __init__(self, descripcion:str, prioridad:int, fecha_vencimiento:str):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha = fecha_vencimiento
    
    def __str__(self):
        return f"\n Tarea: {self.descripcion}, Prioridad: {self.prioridad}, Fecha de vencimiento: {self.fecha}"


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
    
class Lista:
    def __init__(self):
        self.objeto = None

    def agregar_tarea(self, item):
        newNode = Node(item)
        newNode.next = self.objeto
        self.objeto = newNode

    def listar_tareas(self):
        actual = self.objeto
        while actual is not None:
            print(actual.data, end=" ")
            actual = actual.next

    def elimina_tarea(self, position):
        if self.objeto is None:
            print("La lista esta vacia")
        else:
            actual = self.objeto
            previous = None
            count = 1
            while actual.next is not None and count < position:
                previous = actual
                actual = actual.next
                count+= 1
            if actual == self.objeto:
                self.objeto = actual.next
                del actual
            else: 
                previous.next = actual.next
                del actual

    def mostrar_por_descripcion(self, descripcion):
        if self.objeto is None:
            print("La lista está vacía")
            return
        
        actual = self.objeto
        encontrado = False
        while actual is not None:
            if actual.data.descripcion == descripcion:
                print(actual.data)
                encontrado = True
            actual = actual.next
        
        if not encontrado:
            print("No se encontró ninguna tarea con esa descripción.")

    def completar_tarea(self, position):
        if self.objeto is None:
            print("La lista esta vacia")
        else:
            actual = self.objeto
            previous = None
            count = 1
            while actual.next is not None and count < position:
                previous = actual
                actual = actual.next
                count+= 1
            if actual == self.objeto:
                self.objeto = actual.next
                print(f"la tarea {actual.data.descripcion} se ha completado y pasara a ser eliminada de la lista")
                del actual
            else: 
                previous.next = actual.next
                print(f"la tarea {actual.data.descripcion} se ha completado y pasara a ser eliminada de la lista")
                del actual



tarea1 = Tarea("Lavar los platos", 1, "19 de septiembre del 2024")
tarea2 = Tarea("Ordenar cuarto", 3, "20 de septiembre del 2024")
tarea3 = Tarea("Sacar la basura", 2, "21 de septiembre del 2024")
tarea4 = Tarea("Hacer el mercador", 1, "22 de septiembre del 2024")

# Creacion de una lista
lista_tarea = Lista()

#Agregar tareas
lista_tarea.agregar_tarea(tarea1)
lista_tarea.agregar_tarea(tarea2)
lista_tarea.agregar_tarea(tarea3)
lista_tarea.agregar_tarea(tarea4)

#Elimina una tarea por su posicion
lista_tarea.elimina_tarea(1)

#Muestra todas las tareas de la lista
lista_tarea.listar_tareas()

#Busca una tarea por su descripcion
lista_tarea.mostrar_por_descripcion("Sacar la basura")

# Completamos una tarea
lista_tarea.completar_tarea(3)
