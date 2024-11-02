import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# Cargar el conjunto de datos Fashion MNIST
fashion_mnist = datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Normalizar las imágenes
train_images = train_images / 255.0
test_images = test_images / 255.0

# Definir el modelo
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10)  # 10 clases
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_images, train_labels, epochs=10)

# Guardar el modelo
model.save('fashion_mnist_model.h5')  # Guarda el modelo en formato HDF5