edad = 22
edad = int(input("Introduce tu edad: "))

if edad < 18:
  print("Lo siento, no puedes entrar. Debes ser mayor de 18 años.")
else:
  print("Bienvenido!")

# preguntar el nombre y mostrar en pantalla la edad y el nombre 
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
print("Hola", nombre, "tienes", edad, "años")