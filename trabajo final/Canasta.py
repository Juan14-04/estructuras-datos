import numpy as np
from tensorflow.keras import models
from PIL import Image

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

# Cargar el modelo previamente entrenado
try:
    model = models.load_model('fashion_mnist_model.h5')
except Exception as e:
    print(f"Error al cargar el modelo: {e}")

# Función para cargar y preprocesar imágenes
def load_and_preprocess_image(image_path):
    try:
        img = Image.open(image_path).convert('L')  # Convertir a escala de grises
        img = img.resize((28, 28))  # Cambiar tamaño a 28x28
        img_array = np.array(img) / 255.0  # Normalizar
        img_array = img_array.reshape((1, 28, 28, 1))  # Añadir dimensiones para el modelo
        return img_array
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")
        return None

# Realizar predicciones en una imagen
def predict_image(image_path):
    processed_image = load_and_preprocess_image(image_path)
    if processed_image is not None:
        predictions = model.predict(processed_image)
        predicted_class = np.argmax(predictions, axis=1)
        class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                       'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
        print("La clase predicha es:", class_names[predicted_class[0]])

# Instanciar la clase canasta
canasta = Canasta() 

# Bucle para utilizar los operadores
while True:
    operador = input("¿Qué operador desea utilizar? (push, pop, peek, isEmpty, predict, mostrar, salir): ")

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

    elif operador == 'predict':
        if canasta.isEmpty():
            print("La canasta está vacía, no se puede predecir.")
        else:
            prenda = canasta.top()  # Obtener la prenda en la cima para predecir
            # Supongamos que la prenda tiene un nombre de archivo correspondiente
            image_path = f'./{prenda}.jpg'  # Cambiar según cómo se nomenclen las imágenes
            predict_image(image_path)

    elif operador == 'mostrar':
        canasta.mostrar()

    elif operador == 'salir':
        print("Se salió de la canasta")
        canasta.mostrar()
        break

    else:
        print("Operador no válido")
