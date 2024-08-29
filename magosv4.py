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
       Diccionario de objetos
        Elemento	                Tipo        	Descripción
        ************************************************************************************************************
       
        Variables		
        *********
        v_nomArchivo	            str	        Nombre del archivo de texto a leer.
        dict_personajes	            dict    	Diccionario que almacena los personajes y sus clasificaciones.
        lst_magos	                list    	Lista de nombres de los magos.
        lst_cientificos	            list    	Lista de nombres de los científicos.
        lst_otros	                list    	Lista de nombres de otros personajes.
        lst_grandiosos	            list    	Lista de nombres de magos con el prefijo "El gran".
        v_limpiarPantalla	        bool    	Flag para controlar si se limpia la pantalla.
        v_cont	                    str	        Variable para almacenar la respuesta del usuario si desea continuar.
        
        Funciones		
        *********
        f_limpiar_pantalla()     	function	Limpia la pantalla de la consola.
        f_leer_archivo()	        function	Lee un archivo de texto y crea un diccionario.
        f_clasificar_personajes()   function	Clasifica los personajes en diferentes categorías.
        f_hacer_grandioso()	        function	Agrega el prefijo "El gran" a los nombres de los magos.
        f_imprimir_nombres()	    function	Imprime los nombres de una lista.
        f_imprimir_todos()	        function	Imprime todos los personajes con su clasificación.
        f_imprimir_magos()	        function	Imprime solo los nombres de los magos.
        f_imprimir_grandiosos()	    function	Imprime los nombres de los magos con el prefijo.
        f_imprimir_lista_final()   	function	Imprime todos los personajes después de agregar el prefijo.
        f_menu()                   	function	Genera menu.

        Explicación de las columnas:

        Elemento: Nombre de la variable o función.
        Tipo: Tipo de dato (str, int, float, list, dict, function, etc.).
        Descripción: Qué hace o almacena el objeto.
            - Librerías utilizadas:
                1) Tabulate, permite mostrar datos tabulados y agregar formateos personalizados
                2) OS, permite acceder a comandos del S.O, por ejemplo, para limpiar la pantalla
    - Guía de estilos y nomenclatura:
        1) Para una mejor identificación, se han agregado prefijos a los objetos:
            f_   : Para funciones
            lst_ : Para listas
            v_   : Para variables
            dict_: Para diccionarios
        2) Notación: Además del prefijo, todos los nombres de objetos, inician con la primera palabra 
        en minúscula y la segunda con la primera letra en mayúscula, ejemplo: "unEjemplo".        
    - Consideraciones especiales:
        1) Cada función incluye docstrings, con indicación de:
            a) Su Propósito o qué hace.
            b) Parámetros que recibe.
            c) Qué retorna.
Autor              : Jota Cordova (jotacordovaj.io@gmail.com)
Fecha de creación  : 16/08/2024
Última modificación: 29/08/2024 (Autor)
Versión: 4.0.0

Historial de versiones para consola:
    1.0.0 (16/08/2024): Versión inicial. Corre el programa, el diccionario viene en el código 
                        y muestra todo sin control. 
    2.0.0 (18/08/2024): Agrega menú.
    2.0.1 (19/08/2024): Corrige opciones del menú
    3.0.0 (20/08/2024): Agrega ingesta de datos desde un archivo externo CSV.
    4.0.0 (26/08/2024): Agrega más opciones al menú, otras mejoras usando OS, cambia notación funciones.

Historial de versiones para web:
    1.0.0 (22/08/2024): Versión inicial. Configuraciones y resolver problemas de seguridad. 
    1.0.1 (29/08/2024): Se corrigen algunos problemas menores, se habilita readme.html, readme.pdf, actualiza y realizan pruebas. 
    
Mejoras programadas:    

    * Agregar interactivamente un nuevo personaje al archivo externo (csv, txt o base de datos).

Licencia: Dominio público
"""

# Librerias importadas
# ************************
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
    """
    Presenta un menú interactivo al usuario para mostrar listas de personajes.

    Permite al usuario seleccionar entre las siguientes opciones:
    - opc 1= Imprime el listado original de personajes.
    - opc 2= Imprime sólo los magos sin prefijo.
    - opc 3= Imprime sólo los magos con prefijo 'El gran mago'.
    - opc 4= Imprime la lista de científicos.
    - opc 5= Imprime la lista de otros personajes.
    - opc 6= Imprime la lista completa modificada.
    - opc 7= Sale del programa.

    El menú se repite hasta que el usuario elige la opción de salir.

    Parámetros: No recibe parámetros (None)

    Retorna: Ejecuta la acción seleccionada y despliega el resultado
    """
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
            print("Esta es la lista de magos modificada, con prefijo 'El gran mago': ")
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
