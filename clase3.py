ingresototal = int(input("definir el numero maximo de ingreso: "))
n = 0
while n < ingresototal:
   
    bvalido= int(input("ingrese el 1 si es valido y el 2 si es invailido: "))
    if bvalido == 1:
        print("boleto es valido")
        n= n + 1
    else :
        print("boleto invalido")
       
print("no se permite mas ingreso")
   