path_libreria = "./archivos-texto/libreria.txt"
lista_librerias = []

class libreria(object):
    libro = []
    def __init__(self, nombre=None, direccion=None, telefono=None, libro=[]):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.libro = libro

    def agregar_libro(self, nuevo_libro):
        self.libro.append(nuevo_libro)
        return 'Libro agregado'

def crear_libreria():
    nombre = input('Ingresa un nombre: ')
    direccion = input('Ingresa una direccion: ')
    telefono = input('Ingresa un telefono: ')
    lista_librerias.append(libreria(nombre, direccion, telefono, []))
    return 'Creado con exito'

def insertar_libro(nombre_a_buscar):
    nombre = input('Ingrese un nombre: ')
    anio = int(input('Ingrese un anio: '))
    for data in lista_librerias:
        if data.nombre == nombre_a_buscar:
            libro = {
                'nombre': nombre,
                'anio': anio
            }
            arreglo_libros = data.libro
            arreglo_libros.append(libro)
    return 'Libro agregado con exito'

def editar_libro(nombre_a_buscar, campo ,nuevo_dato):
    for data in lista_librerias:
        if data.nombre == nombre_a_buscar:
            data.libro[0][campo] = nuevo_dato
    return 'Libro editado con exito'

def editar_libreria(nombre_a_buscar, campo, nuevo_dato):
    for data in lista_librerias:
        if data.nombre == nombre_a_buscar:
            if campo == 'nombre':
                data.nombre = nuevo_dato
            elif campo == 'telefono':
                data.telefono = nuevo_dato
            else:
                data.direccion = nuevo_dato
    return 'Libreria editada con exito'


def eliminar_libreria(nombre_a_buscar):
    contador = 0
    for data in lista_librerias:
        if data.nombre == nombre_a_buscar:
            lista_librerias.pop(contador)
        contador += 1
    return 'Libreria eliminadda'

def escribir_archivo(path):
    for data in lista_librerias:
        datos = {
            'nombre': data.nombre,
            'direccion': data.direccion,
            'telefono': data.telefono,
            'libros': data.libro
        }
        archivo = open(path, 'a')
        archivo.write(str(datos))
    archivo.close()
    return 'Escrito en archivo libreria.txt'



def menu():
    opcion = None
    while (opcion != 0):
        print("********************************")
        print("Libreria POLICRUSH")
        print("Escoge una opcion del menu:")
        print("1) Crear libreria\n2) Agregar libro\n3) Editar Libro\n4) Editar libreria\n5) Eliminar libreria\n6) Escribir datos en txt\n0) Salir")
        print("*********************************")
        opcion = int(input("Seleccione una opcion: "))
        print("*************************************")
        if (opcion == 1):
            print(crear_libreria())
        elif (opcion == 2):
            libreria_recepcion = input('Libreria donde quiere insertar el libro: ')
            print(insertar_libro(libreria_recepcion))
        elif (opcion == 3):
            libreria_recepcion = input('Libreria donde quiere insertar el libro: ')
            campo_modificar = input('Campo que desea modificar: ')
            nuevo_dato = input('Nuevo dato: ')
            print(editar_libro(libreria_recepcion, campo_modificar,nuevo_dato))
        elif(opcion == 4):
            libreria_recepcion = input('Libreria donde quiere insertar el libro: ')
            campo_modificar = input('Campo que desea modificar: ')
            nuevo_dato = input('Nuevo dato: ')
            print(editar_libreria(libreria_recepcion, campo_modificar, nuevo_dato))
        elif (opcion == 5):
            libreria_recepcion = input('Libreria donde quiere insertar el libro: ')
            print(eliminar_libreria(libreria_recepcion))
        elif (opcion == 6):
            print(escribir_archivo(path_libreria))
        elif (opcion == 0):
            print("Adios")
        else:
            print("Errooor")
            opcion = 0


menu()