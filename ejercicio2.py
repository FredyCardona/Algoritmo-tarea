nombre_completo = input("introduzca su nombre completo: ")

palabras = nombre_completo.split()

nombres_cap = [palabra.capitalize() for palabra in palabras]

print("Nombre en minúsculas:", nombre_completo.lower())
print("Nombre en mayúsculas:", nombre_completo.upper())
print("Nombre con la primera letra en mayúscula:", ' '.join(nombres_cap))