import numpy as np
from tensorflow.keras import models
from PIL import Image

# Cargar el modelo previamente entrenado
model = models.load_model('fashion_mnist_model.h5')  # Cambia esto a la ruta de tu modelo

# Función para cargar y preprocesar imágenes
def load_and_preprocess_image(image_path):
    img = Image.open(image_path).convert('L')  # Convertir a escala de grises
    img = img.resize((28, 28))  # Cambiar tamaño a 28x28
    img_array = np.array(img) / 255.0  # Normalizar
    img_array = img_array.reshape((1, 28, 28, 1))  # Añadir dimensiones para el modelo
    return img_array

# Realizar predicciones en una imagen
def predict_image(image_path):
    processed_image = load_and_preprocess_image(image_path)
    predictions = model.predict(processed_image)
    predicted_class = np.argmax(predictions, axis=1)
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    print("La clase predicha es:", class_names[predicted_class[0]])

# Ejemplo de uso para predecir la clase de una imagen
image_path = './pantalon.jpg'  # Cambia esto por la ruta de tu imagen
predict_image(image_path)
