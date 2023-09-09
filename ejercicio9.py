fecha_nacimiento = input("introduzca su fecha de nacimiento en formato dd/mm/aaaa: ")

partes = fecha_nacimiento.split('/')

if len(partes) != 3:
    print("El formato de la fecha no es válido.")
else:
    dia, mes, anio = partes

    if not dia.isdigit() or not mes.isdigit() or not anio.isdigit():
        print("La fecha debe contener solo números enteros.")
    else:
        dia, mes, anio = int(dia), int(mes), int(anio)

        if 1 <= dia <= 31 and 1 <= mes <= 12:
            print("Día:", dia)
            print("Mes:", mes)
            print("Año:", anio)
        else:
            print("La fecha no es válida.")