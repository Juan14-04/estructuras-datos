import tensorflow as tf 
import numpy as np 
from PIL import Image 
import os 

class Canasta:
    def __init__(self):
        self.items = [] 
         
    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        limite = 10
        if len(self.items) < limite:
            self.items.append(item)
            print("Prenda agregada:", item)
        else:
            print(f"La canasta está llena. Contiene {len(self.items)} prendas.")

    def pop(self):
        if not self.isEmpty():
            prenda = self.items.pop(0)
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

modelo = tf.keras.applications.MobileNetV2(weights='imagenet')

def reconocer_prenda(url_imagen):
    try:
       
        img = Image.open(url_imagen).resize((224, 224))

       
        img_array = np.array(img) / 255
        print(f'Matriz de la imagen {img_array}') 

        
        img_array = np.expand_dims(img_array, axis=0)
        print(f'Matriz expasion {img_array}') 

        
        predicciones = modelo.predict(img_array)

       
        resultado = tf.keras.applications.mobilenet_v2.decode_predictions(predicciones, top=1)[0][0][1]

        return resultado
    
    
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")
        return None


canasta = Canasta() 


while True:
    operador = input("¿Qué operador desea utilizar? (push, pop, peek, isEmpty, salir): ")

    if operador == 'push':
        imagen = input("Ingrese la ruta de la imagen a agregar: ")
        if os.path.isfile(imagen):
            prenda = reconocer_prenda(imagen)
            if prenda:
                canasta.push(prenda)
        else:
            print("La URL que ingresaste no existe en tu equipo. Valida que si exista esa ruta en tu computador")

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
        print("Se salió de la canasta")
        canasta.mostrar() 
        break
