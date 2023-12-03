matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

for fila in matriz:
    print(fila)

suma = sum(matriz[i][i] for i in range(len(matriz)))

multiplicacion = 1
for i in range(len(matriz)):
    multiplicacion *= matriz[i][i]

print("el resultado de la suma es: ", suma)
print("el resultado de la multiplicacion es: ", multiplicacion)
