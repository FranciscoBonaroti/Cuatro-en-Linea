def TableroVacio ():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        ]

def ContenidoColumna (nrocolumna, tablero):
    columna = []
    for row in tablero:
        celda = row[nrocolumna - 1]
        columna.append(celda)
    return columna 

def ContenidoFila (nrofila, tablero):
    if nrofila == 0:
        nrofila = 1
    return tablero[nrofila - 1]
def Filardas (tablero):
    filas = []
    for c in range(6):
        filas += ContenidoFila(c+1, tablero)
    return filas

def Columnardas (tablero):
    columnas = []
    for x in range(7):
        columnas += ContenidoColumna (x+1, tablero)
    return columnas

def soltarFichaEnColumna (ficha, column, tablero):
        for row in range(6, 0, -1):
                if tablero[row - 1][column - 1] == 0:
                        tablero[row -1][column -1] = ficha
                        return 
def CompletarTableroOrden (secuencia, tablero):
    t = 0
    for a in secuencia:
        if t % 2 == 0:
            soltarFichaEnColumna(1, a, tablero)
        else:
            soltarFichaEnColumna(2, a, tablero)
        t+=1
    return tablero