def calcular_media(numeros)
    total = sum(numeros)
    media = total / len(numeros)
    return media

notas = [7, 8, 9, 10]
print(calcular_media(notas))

