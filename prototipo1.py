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
