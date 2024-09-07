a = int(input('la variable a equivale: '))
b = int(input("la variable b equivale: "))

suma = 0
while a > 0: # control de ciclo
    suma += b #hacemos la operacion de suma
    a -= 1  #reducimos la variable de control a 0
print(suma)
