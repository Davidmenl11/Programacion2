matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

mInvertida = matriz[::-1]

sumaR = sum(mInvertida[i][i] for i in range(len(mInvertida)))

MultiR = 1
for i in range(len(mInvertida)):
    MultiR *= mInvertida[i][i]

print("la Suma al revés es: ", SumaR)
print("la multiplicacion al revés: ", MultiR)
