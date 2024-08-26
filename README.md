# ENTREGA FINAL MÓDULO 3 BOOTCAMP FULL STACK PYTHON

## Sistema Harry Potter es el único Gran Mago
  Ejercicio para clasificación de Personajes

### Descripción del proyecto

* **Objetivo:** Clasificar y manipular una lista de personajes.
* **Funcionalidades:**
    1) Lee un archivo externo en formato txt.
    2) Convierte los datos a un diccionario.
    3) Convierte el diccionario en 3 listas, según su valor.
    4) Agrega prefijo "El gran Mago" a personajes de lista "Magos"
    5) Genera lista con todos los personajes antes de ser modificados.
    6) Genera la lista de los "Magos" modificada con el prefijo "El gran mago"
    7) Genera lista con todos los personajes, incluyendo los modificados con su prefijo
    8) (Pendiente próxima versión) Agrega un nuevo personaje al archivo txt, en formato clave:valor (nombre:clasificación)
* **Dependencias externas:**
  
      1) Archivo externo: "personajes.txt", permite escalabilidad al proyecto.
       
* **Tecnologías:**
    * Python==3.12.15
    * Tabulate==0.9.0  
* **Estructura del código:**
    * Cada función incluye docstrings, con indicación de:
      
      a) Su Propósito o qué hace.
      
      b) Parámetros que recibe.

      c) Lo qué retorna.
    
### Detalles técnicos

* **Estructura de datos:** Diccionario para almacenar personajes.
* **Algoritmos:** Clasificación ordenamiento y búsqueda de valores utilizando los métodos de la clase diccionario y listas.
* **Librerías:**
    * **Tabulate:** Para formatear tablas de salida.
    * **OS:** Para interactuar con el sistema operativo (limpiar pantalla).

### Historial de versiones
* **1.0.0 (16/08/2024):** Versión inicial.
* **2.0.0 (18/08/2024):** Agrega menú.
* **2.0.1 (19/08/2024):** Corrige opciones del menú.
* **3.0.0 (20/08/2024):** Agrega ingesta de datos desde un archivo externo.

### Código (PENDIENTE)

```python
# Pendiente, agregar código Python en formato MD
```

### Diccionario de objetos

| Elemento | Tipo | Descripción |
|---|---|---|
| Variables |  |  |
| v_nomArchivo | str | Nombre del archivo de texto a leer. |
| dict_personajes | dict | Diccionario que almacena los personajes y sus clasificaciones. |
| lst_magos | list | Lista de nombres de los magos. |
| lst_cientificos | list | Lista de nombres de los científicos. |
| lst_otros | list | Lista de nombres de otros personajes. |
| lst_grandiosos | list | Lista de nombres de magos con el prefijo "El gran". |
| v_limpiarPantalla | bool | Flag para controlar si se limpia la pantalla. |
| v_cont | str | Variable para almacenar la respuesta del usuario si desea continuar. |
| Funciones |  |  |
| f_limpiarPantalla()/f_limpiar_pantalla() | function | Limpia la pantalla de la consola. |
| f_leerArchivo()/f_leer_archivo() | function | Lee un archivo de texto y crea un diccionario. |
| f_clasificarPersonajes()/f_clasificar_personajes() | function | Clasifica los personajes en diferentes categorías. |
| f_hacerGrandioso()/f_hacer_grandioso() | function | Agrega el prefijo "El gran" a los nombres de los magos. |
| f_imprimirNombres()/f_imprimir_nombres() | function | Imprime los nombres de una lista. |
| f_imprimirTodos()/f_imprimir_todos() | function | Imprime todos los personajes con su clasificación. |
| f_imprimirMagos()/f_imprimir_magos() | function | Imprime solo los nombres de los magos. |
| f_imprimirGrandiosos()/f_imprimir_grandiosos() | function | Imprime los nombres de los magos con el prefijo. |
| f_imprimirFinal()/f_imprimir_lista_final() | function | Imprime todos los personajes después de agregar el prefijo. |
| f_menu() | function | Muestra el menú |

Nota: En la versión 3.1, se cambió la notación de las funciones, coherente con "snake_case" Python.

**Explicación de las columnas:**

-   **Elemento:** Nombre de la variable o función.
-   **Tipo:** Tipo de dato (str, int, float, list, dict, function, etc.).
-   **Descripción:** Qué hace o almacena el objeto.

**Consideraciones adicionales:**
    Guía de estilos y nomenclatura:
    
      1) Para una mejor identificación, se han agregado prefijos a los objetos:
      
          f_   : Para funciones
          lst_ : Para listas
          v_   : Para variables
          dict_: Para diccionarios
          
      2) Notación: Además del prefijo, todos los nombres de objetos, inician con la primera 
                   palabra en minúscula y la segunda con la primera letra en mayúscula, 
                   ejemplo: "unEjemplo"
                   
      3) Se trata de mantener coherencia con PEP8      

Author             : Jota Cordova (jotacordovaj.io@gmail.com)

Fecha de creación  : 16/08/2024

Última modificación: 21/08/2024

Versión            : 3.0.0

**Historial de versiones**
   
    1.0.0 (16/08/2024): Versión inicial. Corre el programa, el diccionario se encuentra embebido
                        viene en el código y muestra todo sin control, cumple el objetivo básico.
                        
    2.0.0 (18/08/2024): Agrega menú y algunas interacciones.
    
    2.0.1 (19/08/2024): Corrige opciones del menú.
    
    3.0.0 (30/08/2024): Agrega ingesta de datos desde un archivo CSV externo.

    3.1.0 (26/08/2024): Agrega una versión con más opciones y lectura desde archivo TXT.

**Próximo release:**    
    
    4.0.0 (30/08/2024): Agregar un nuevo personaje modificando el archivo de texto.
