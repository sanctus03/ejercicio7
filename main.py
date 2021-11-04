#EJERCICIO 7

lista_nombre= []
while True:
    nombre= input("Nombre: ")
    if nombre == "fin":
        break
    telefono= input("Número de teléfono: ")
    linea= {}
    linea["Nombre: "]= nombre
    linea["Teléfono: "]= telefono
    lista_nombre.append(linea)
print("Lista nombre: \n", lista_nombre)