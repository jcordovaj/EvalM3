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
Última modificación: 20/08/2024 (Autor)
Versión: 3.0.0

Historial de versiones:
    1.0.0 (16/08/2024): Versión inicial. Corre el programa, el diccionario viene en el código 
                        y muestra todo sin control. 
    2.0.0 (18/08/2024): Agrega menú.
    2.0.1 (19/08/2024): Corrige opciones del menú
    3.0.0 (20/08/2024): Agrega ingesta de datos desde un archivo externo CSV.
    3.1.0 (26/08/2024): Agrega ingesta de datos desde un archivo externo TXT y más opciones al menu, cambia notación funciones.

Licencia: Dominio público
"""

# Librerias importadas
# ************************
import tabulate
from flask import Flask, render_template, request

app = Flask(__name__)

def f_leerArchivo(v_nomArchivo):
    """
    Lee un archivo de texto, crea un diccionario con nombre y clasificación,
    omite encabezados

    Parámetros: Recibe un archivo o, un path o ruta al archivo

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

def f_clasificarPersonajes(v_dic):
    """
    Separa los personajes según su clasificación.

    Parámetros: Recibe un diccionario con un nombre (key) y
    una clasificación (value)

    Salida: Genera 3 listas, una por clasificación
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

def f_crear_dic_final(lst_grandiosos, lst_cientificos, lst_otros):
    """
    Crea un diccionario de personajes a partir de las listas proporcionadas.

    Parámetros:
        lst_grandiosos  : Lista de magos grandiosos.
        lst_cientificos : Lista de científicos.
        lst_otros       : Lista de personajes de otra clasificación.

    Retorna:
        Un diccionario donde las claves son las clasificaciones ("Mago", "Científico", "Otro")
        y los valores son listas de nombres de personajes.
    """

    personajes = []
    for mago in lst_grandiosos:
        personajes.append({'nombre': mago, 'clasificacion': 'Mago'})
    for cientifico in lst_cientificos:
        personajes.append({'nombre': cientifico, 'clasificacion': 'Científico'})
    for otro in lst_otros:
        personajes.append({'nombre': otro, 'clasificacion': 'Otro'})
    return personajes
    
# Parámetros para ejecución del programa
v_nomArchivo                          = "personajes.txt"
dict_personajes                       = f_leerArchivo(v_nomArchivo)
lst_magos, lst_cientificos, lst_otros = f_clasificarPersonajes(dict_personajes)
lst_grandiosos                        = f_hacerGrandioso(lst_magos)
v_limpiarPantalla                     = True  # Inicializamos un flag para limpiar la pantalla

#   M E N U
#   *******
  
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        opcion_seleccionada = request.form['selector']
        if opcion_seleccionada == 'option1':
            personajes = []
            for nombre, clasificacion in dict_personajes.items():
                personajes.append({'nombre': nombre, 'clasificacion': clasificacion})
        elif opcion_seleccionada == 'option2':
            personajes = []
            for mago in lst_magos:
                personajes.append({'nombre': mago, 'clasificacion': 'Mago'})
        elif opcion_seleccionada == 'option3':
            personajes = []
            for mago in lst_grandiosos:
                personajes.append({'nombre': mago, 'clasificacion': 'Mago'})
        elif opcion_seleccionada == 'option4':
            personajes = f_crear_dic_final(lst_grandiosos, lst_cientificos, lst_otros)
        elif opcion_seleccionada == 'option5':
            personajes = []
        return render_template('menu.html', personajes=personajes)
    else:
        personajes = []
        return render_template('menu.html', personajes=personajes)

if __name__ == '__main__':
    app.run(debug=True)    