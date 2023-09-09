numero_telefono = input("introduzca su número de teléfono con el formato +34-XXXXXXXXX-XX: ")

try:
    numero_principal = numero_telefono[4:-3]
    print("Número principal:", numero_principal)
except IndexError:
    print("El número de teléfono no tiene el formato válido.")