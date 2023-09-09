precio = input("introduzca el precio del producto en euros con dos decimales): ")

if precio.count('.') == 1:
    try:
        euros, centimos = map(int, precio.split('.'))
        print("Euros:", euros)
        print("Céntimos:", centimos)
    except ValueError:
        print("El precio introducido no es válido.")
else:
    print("El precio introducido no tiene el formato correcto debe incluir un punto decimal).")