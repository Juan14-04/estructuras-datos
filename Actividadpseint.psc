Algoritmo Cesta
    Definir canasta Como Cadena
    Definir operador Como Cadena
    Definir prenda Como Cadena
    Definir cantidad Como Entero
    cantidad <- 5
    Dimensionar canasta(10)
    canasta[1] <- 'Camisa'
    canasta[2] <- 'Pantalones'
    canasta[3] <- 'Chaqueta'
    canasta[4] <- 'Zapatos'
    canasta[5] <- 'Bufanda'
    Mientras Verdadero Hacer
        Escribir '¿Qué operador desea utilizar? (push, pop, peek o isEmpty)'
        Leer operador
        Según operador Hacer
            'push':
                Si cantidad<10 Entonces
                    Escribir 'Ingrese la prenda a agregar:'
                    Leer prenda
                    cantidad <- cantidad+1
                    canasta[cantidad] <- prenda
                    Escribir 'Prenda agregada:', prenda
                SiNo
                    Escribir 'La canasta está llena'
                FinSi
            'pop':
                Si cantidad>0 Entonces
                    Escribir 'Prenda eliminada:', canasta[cantidad]
                    cantidad <- cantidad-1
                SiNo
                    Escribir 'La canasta está vacía'
                FinSi
            'peek':
                Si cantidad>0 Entonces
                    Escribir 'Prenda en la cima:', canasta[cantidad]
                SiNo
                    Escribir 'La canasta está vacía'
                FinSi
            'isEmpty':
                Si cantidad=0 Entonces
                    Escribir 'La canasta está vacía'
                SiNo
                    Escribir 'La canasta no está vacía'
                FinSi
            De Otro Modo:
                Escribir 'Operador no válido'
        FinSegún
    FinMientras
FinAlgoritmo
