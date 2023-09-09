nombre = input("introduzca su nombre: ")

contador_letras = 0
for letra in nombre:
    if letra.isalpha():
        contador_letras += 1

nombre_mayusculas = nombre.upper()
print(f"{nombre_mayusculas} tiene {contador_letras} letras.")