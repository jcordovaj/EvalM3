import tabulate, os, platform
from colorama import init

def f_limpiar_pantalla():
    """
    Limpia la pantalla de las salidas anteriores
    
    Parámetros: Ninguno (None), se ejecuta directamente
    
    Retorna: Limpia la pantalla
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def f_leer_archivo(v_nomArchivo):
    """
    Lee un archivo de texto, crea un diccionario con los 
    nombres y clasificaciones, omite encabezados
    
    Parámetros: Recibe un nombre de archivo, un path 
    o ruta al archivo
    
    Retorna: Un diccionario con los elementos del archivo
    """
    dict_personajes = {}
    with open(v_nomArchivo, 'r', encoding='utf-8') as v_archivo:
        # Forzamos que salte la primera línea para omitir los encabezados
        next(v_archivo)
        for v_linea in v_archivo:
            v_nombre, v_clasificacion            = v_linea.strip().split(',') # Usando los métodos strip y split, limpiamos las cadena de texto 
            dict_personajes[v_nombre.strip('"')] = v_clasificacion.strip('"') #  Elimina las comillas dobles
    return dict_personajes

def f_clasificar_personajes(v_dic):
    """
    Separa los personajes según su clasificación.
    
    Parámetros: Recibe un diccionario con un nombre (key) y
    una clasificación (value) 
    
    Retorna: Genera 3 listas, una por categoria
    """
    lst_magos       = []
    lst_cientificos = []
    lst_otros       = []
    for v_nombre, v_clasificacion in v_dic.items():
        if v_clasificacion   == "Mago":
            lst_magos.append(v_nombre)
        elif v_clasificacion == "Científico":
            lst_cientificos.append(v_nombre)
        else:
            lst_otros.append(v_nombre)  # Los restantes, por defecto, quedan en la lista "Otros"
    return lst_magos, lst_cientificos, lst_otros

def f_hacer_grandioso(v_listaMagos):
    """
    Agrega el prefijo 'El gran' a los nombres de los magos.
    
    Parámetros: Recibe una lista
    
    Retorna: Un objeto lista modificado concatenando elementos
    """
    lst_grandiosos = ["El gran " + v_mago for v_mago in v_listaMagos]
    return lst_grandiosos

def f_imprimir_nombres(v_listaAny):
    """
    Imprime los nombres de una lista cualquiera.
    
    Parámetros: Recibe una lista cualquiera
    
    Retorna: Imprime la lista que se le pase como parámetro
    """
    for v_comodin in v_listaAny:
        print(v_comodin)

def f_imprimir_todos(dict_personajes):
    """
    Imprime los nombres de los personajes (las claves del diccionario)
    en una tabla.

    Parámetros: Un diccionario donde las claves son los nombres 
    de los personajes.

    Retorna: None (Imprime la tabla directamente)
    """
    lst_nombres_personajes = list(dict_personajes.keys())            # Usando el método "keys, creamos una lista con las claves del diccionario
    data = [[v_nombre] for v_nombre in lst_nombres_personajes]       # Ahora pordemos armar una lista de listas para formatear la tabla
    print(tabulate.tabulate(data, headers=["Nombre del Personaje"])) # Usando tabulate armamos el documento y agregamos el encabezado antes de imprimir

def f_imprimir_magos(v_listaMagos):
    """
    Imprime sólo los nombres de los magos
    
    Parámetros: Recibe 1 objeto lista
    
    Retorna: Imprime 1 lista
    """
    f_imprimir_nombres(v_listaMagos)

def f_imprimir_grandiosos(v_listaGrandiosos):
    """
    Imprime los nombres de los magos con el prefijo.
        
    Parámetros: Recibe 1 objeto lista
    
    Retorna: Imprime 1 lista
    """
    f_imprimir_nombres(v_listaGrandiosos)

def f_imprimir_lista_final(lst_grandiosos, lst_cientificos, lst_otros):
    """
    Imprime todos los personajes después de agregar prefijo.
    
    Parámetros: Recibe 3 listas
    
    Retorna: Imprime las 3 listas por pantalla 
    """
    print("Los magos grandiosos son:")
    print(24*"-")
    f_imprimir_nombres(lst_grandiosos)
    print("\nCientíficos destacados:")
    print(22*"-")
    f_imprimir_nombres(lst_cientificos)
    print("\nOtros personajes importantes de la historia:")
    print(43*"-")
    f_imprimir_nombres(lst_otros)

# Parámetros bloque principal del programa
v_nomArchivo                          = "personajes.txt"
dict_personajes                       = f_leer_archivo(v_nomArchivo)
lst_magos, lst_cientificos, lst_otros = f_clasificar_personajes(dict_personajes)
lst_grandiosos                        = f_hacer_grandioso(lst_magos)
    
def f_menu():
    while True:
        f_limpiar_pantalla()
        print("Menú:")
        print("Opción (1): Imprimir listado original de personajes")
        print("Opción (2): Imprimir sólo los Magos sin prefijo")
        print("Opción (3): Imprimir sólo los Magos con prefijo 'El gran mago'")
        print("Opción (4): Imprimir la lista de Científicos")
        print("Opción (5): Imprimir la lista de Otros personajes")
        print("Opción (6): Imprimir lista completa modificada")
        print("Opción (7): Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            f_limpiar_pantalla()
            print("")
            print("Este es el listado original de personajes: ")
            print(41*"=")
            f_imprimir_todos(dict_personajes)
        elif opcion == 2:
            f_limpiar_pantalla()
            print("")
            print("Estos son sólo los magos, sin modificar: ")
            print(39*"=")
            f_imprimir_magos(lst_magos)
        elif opcion == 3:
            f_limpiar_pantalla()
            print("")
            print("Esta es la lista de magos modificada, con prefijo 'El gram mago': ")
            print(64*"=")
            f_imprimir_grandiosos(lst_grandiosos)
        elif opcion == 4:
            f_limpiar_pantalla()
            print("")
            print("Esta es la lista de 'Científicos': ")
            print(33*"=")
            f_imprimir_nombres(lst_cientificos)
        elif opcion == 5:
            f_limpiar_pantalla()
            print("")
            print("Esta es la lista de 'Otros' personajes: ")
            print(38*"=")
            f_imprimir_nombres(lst_otros)           
        elif opcion == 6:
            f_limpiar_pantalla()
            print("")
            print("Este es el listado final de personajes: ")
            print(38*"=")
            f_imprimir_lista_final(lst_grandiosos, lst_cientificos, lst_otros)
        elif opcion == 7:
            break
        else:
            print("Opción inválida")

        if input("¿Desea continuar? (s/n): ").lower() != 's':
            break

if __name__ == "__main__":
    if platform.system() == "Windows":
        init()
    f_menu()