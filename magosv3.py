# coding=utf-8
# Author: Jorge Córdova

#*******************************************************************************
#*                                                                             *
#*              ENTREGA FINAL MÓDULO 3 BOOTCAMP FULL STACK PYTHON              *
#*                 Sistema Harry Potter es el único Gran Mago                  *
#*                                                                             *
#*******************************************************************************

"""
Título del módulo: Identificar y clasificar Personajes.

Descripción:
    - Funcionalidades principales:
        1) Lee un archivo externo en formato txt.
        2) Convierte los datos a un diccionario.
        3) Convierte diccionario en 3 listas, según su valor.
        4) Agrega prefijo "El gran Mago " a personajes de lista "Magos"
        5) Genera lista con todos los personajes antes de ser modificados.
        6) Genera la lista de los "Magos" modificada con el prefijo "El gran mago"
        7) Genera lista con todos los personajes, incluyendo los modifcados y su prefijo
        Pendiente: 8) Agrega un nuevo personaje, llave:valor (nombre:clasificación) 
    - Dependencias externas:
        1) Archivo externo "personajes.txt", permite escalabilidad al proyecto.
    - Diccionario de funciones:
        1) Fx 1
        2) Fx 2
        3) Fx 3
        4) Fx 4
        5) Fx 1
        6) Fx 2 
    - Librerías utilizadas:
        1) Tabulate, permite mostrar datos tabulados y agregar formateos personalizados
        2) OS, permite acceder a comandos del S.O, por ejemplo, para limpiar la pantalla
    - Guía de estilos y nomenclatura:
        1) Para una mejor identificación, se han agregado prefijos a los objetos:
            f_   : Para funciones
            lst_ : Para listas
            v_   : Para variables
            dict_: Para diccionarios
        2) Notación: Además del prefijo, todos los nombres de objetos, inician con la primera palabra en minúscula y la segunda con la primera letra en mayúscula, ejemplo: "unEjemplo".        
    - Consideraciones especiales:
        1) Cada función incluye docstrings, con indicación de:
            a) Su Propósito o qué hace.
            b) Parámetros que recibe.
            c) Qué retorna.
Autor              : Jota Cordova (jotacordovaj.io@gmail.com)
Fecha de creación  : 16/08/2024
Última modificación: 20/08/2024 (Autor)
Versión: 3.0.0

Historial de versiones:
    1.0.0 (16/08/2024): Versión inicial. Corre el programa, el diccionario viene en el código 
                        y muestra todo sin control. 
    2.0.0 (18/08/2024): Agrega menú.
    2.0.1 (19/08/2024): Corrige opciones del menú
    3.0.0 (20/08/2024): Agrega ingesta de datos desde un archivo externo.

Licencia: Dominio público
"""

# Librerias importadas
# ************************
import tabulate, os # Tabulate permite mostrar datos en un formato tabular
                    # y más atractivo. OS permite acceder a comandos de sistema
                    # operativo. 

def f_limpiarPantalla():
    """
    Limpia la pantalla de las salidas anteriores
    
    Parámetros: None, se ejecuta directamente
    
    Retorna: Limpia la pantalla
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def f_leerArchivo(v_nomArchivo):
    """
    Lee un archivo de texto, crea un diccionario con nombre y clasificación, 
    omite encabezados
    
    Parámetros: Recibe un archivo o, un path o ruta al archivo
    
    Retorna: Un diccionario con los elementos del archivo
    """
    dict_personajes = {}
    with open(v_nomArchivo, 'r') as v_archivo:
        # Forzamos que salte la primera línea para omitir los encabezados
        next(v_archivo)
        for v_linea in v_archivo:
            v_nombre, v_clasificacion            = v_linea.strip().split(',') # Usando los métodos strip y split, limpiamos las cadena de texto 
            dict_personajes[v_nombre.strip('"')] = v_clasificacion.strip('"') #  Elimina las comillas dobles
    return dict_personajes

def f_clasificarPersonajes(v_dic):
    """
    Separa los personajes según su clasificación.
    
    Parámetros: Recibe un diccionario con un nombre (key) y
    una clasificación (value) 
    
    Salida: Genera 3 listas, una por categoria
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
            lst_otros.append(v_nombre)  # Por defecto, los restantes quedan en la lista "Otros"
    return lst_magos, lst_cientificos, lst_otros

def f_hacerGrandioso(v_listaMagos):
    """
    Agrega el prefijo 'El gran' a los nombres de los magos.
    
    Parámetros: Recibe una lista
    
    Retorna: Un objeto lista modificado concatenando elementos
    """
    lst_grandiosos = ["El gran " + v_mago for v_mago in v_listaMagos]
    return lst_grandiosos

def f_imprimirNombres(v_listaAny):
    """
    Imprime los nombres de una lista.
    
    Parámetros: Recibe una lista cualquiera
    
    Retorna: Imprime la lista que se le pase como parámetro
    """
    for v_comodin in v_listaAny:
        print(v_comodin)

def f_imprimirTodos(lst_magos, lst_cientificos, lst_otros):
    """
    Imprime todos los personajes con su clasificación.
    
    Parámetros: Recibe 3 obsjetos lista
    
    Retorna: Imprime 3 listas por pantalla
    """
    lst_data = []
    for v_mago in lst_magos:
        lst_data.append(["Mago", v_mago])
    for v_cientifico in lst_cientificos:
        lst_data.append(["Científico", v_cientifico])
    for v_otro in lst_otros:
        lst_data.append(["Otro", v_otro])
    print(tabulate.tabulate(lst_data, headers=["Clasificación", "Nombre"]))

def f_imprimirMagos(v_listaMagos):
    """
    Imprime sólo los nombres de los magos
    
    Parámetros: Recibe 1 obsjeto lista
    
    Retorna: Imprime 1 lista
    """
    f_imprimirNombres(v_listaMagos)

def f_imprimirGrandiosos(v_listaGrandiosos):
    """
    Imprime los nombres de los magos con el prefijo.
        
    Parámetros: Recibe 1 objeto lista
    
    Retorna: Imprime 1 lista
    """
    
    f_imprimirNombres(v_listaGrandiosos)

def f_imprimirFinal(lst_grandiosos, lst_cientificos, lst_otros):
    """
    Imprime todos los personajes después de agregar prefijo.
    
    Parámetros: Recibe 3 listas
    
    Retorna: Imprime las 3 listas por pantalla 
    
    """
    print("Magos grandiosos:")
    f_imprimirNombres(lst_grandiosos)
    print("\nCientíficos:")
    f_imprimirNombres(lst_cientificos)
    print("\nOtros:")
    f_imprimirNombres(lst_otros)

# Ejecución principal del programa
v_nomArchivo                          = "personajes.txt"
dict_personajes                       = f_leerArchivo(v_nomArchivo)
lst_magos, lst_cientificos, lst_otros = f_clasificarPersonajes(dict_personajes)
lst_grandiosos                        = f_hacerGrandioso(lst_magos)
v_limpiarPantalla                     = True  # Inicializamos un flag para limpiar la pantalla

while True:
    if v_limpiarPantalla:
        f_limpiarPantalla()
    print("\nMenú:")
    print(53*"-")
    print("1. Imprimir todos los personajes con su clasificación")
    print("2. Imprimir solo los Magos")
    print("3. Imprimir los magos con el prefijo 'El gran'")
    print("4. Imprimir la lista final con todos los personajes")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        print('\033[H\033[J', end='')  # Código de escape "ANSI" para forzar el limpiar la pantalla
        print("La lista completa de personajes es: ")
        print(34*"=")
        f_imprimirTodos(lst_magos, lst_cientificos, lst_otros)
    elif opcion == 2:
        print('\033[H\033[J', end='')
        print("La lista de magos sin modificar es: ")
        print(34*"=")
        f_imprimirMagos(lst_magos)
    elif opcion == 3:
        print('\033[H\033[J', end='')
        print("La lista de magos modificada es: ")
        print(31*"=")
        f_imprimirGrandiosos(lst_grandiosos)
    elif opcion == 4:
        print('\033[H\033[J', end='')
        print("Los personajes agrupados por clasificación son: ")
        print(47*"=")
        f_imprimirFinal(lst_grandiosos, lst_cientificos, lst_otros)
    elif opcion == 5:
        break
    else:
        print('\033[H\033[J', end='')
        print("")
        print("Opción inválida")
    
    v_cont = input("¿Desea continuar? (s/n): ")
    if (v_cont.lower() == 's'):
        print('\033[H\033[J', end='')  # ANSI escape code para limpiar la pantalla
        v_limpiarPantalla = True #v_cont.lower() == 's'  # Actualizar el flag
    else:
        v_limpiarPantalla = False
