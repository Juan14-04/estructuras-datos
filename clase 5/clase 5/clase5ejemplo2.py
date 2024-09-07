def multiplicacion (a:int, b:int) -> int:
    if a == 0:
        return 0
    return(b + multiplicacion(a-1,b))
print(multiplicacion(2, 3))