matriz=[[0,0],[0,0]]
determinante=0
fila=0
columna=0

for fila in range (0,2):
    for columna in range(0,2):
        matriz[fila][columna]= float (input(f'Teclea la posicion fila {fila}, columna {columna}:'))

determinante = matriz[0][0] * matriz[1][1] - matriz[1][0] * matriz[0][1]

print(f'La solucion del determinante de la matriz es :{determinante}')