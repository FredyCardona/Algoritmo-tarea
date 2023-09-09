nombre = input("introduzca su nombre: ")
while True:
    try:
        numero = int(input("introduzca un numero entero: "))
        break  
    except ValueError:
        print("introduzca un número entero válido.")

nombres_repetidos = [nombre] * numero
for nombre_repetido in nombres_repetidos:
    print(nombre_repetido)