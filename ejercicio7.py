correo_original = input("introduzca su correo electrónico: ")

indice_arroba = correo_original.find('@')

if indice_arroba != -1:
    nombre_usuario = correo_original[:indice_arroba]

    nuevo_correo = nombre_usuario + "@ceu.es"

    print("Nuevo correo electrónico:", nuevo_correo)
else:
    print("El correo electrónico no tiene un formato válido (falta la arroba).")
