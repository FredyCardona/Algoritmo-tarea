frase = input("introduzca una frase: ")

vocal = input("introduzca una vocal en minúscula: ")

if vocal in 'aeiou':
    frase_modificada = frase.replace(vocal, vocal.upper())

    print("Frase con la vocal en mayúscula:", frase_modificada)
else:
    print("introduzca una vocal válida en minúscula (a, e, i, o, u).")
