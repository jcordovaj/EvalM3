# Entrega Final Módulo 3 Bootcamp Full Stack Python

## Sistema Harry Potter: El único Gran Mago
 Ejericicio para clasificación de Personajes

### Descripción del proyecto

* **Objetivo:** Clasificar y manipular una lista de personajes.
* **Funcionalidades:**
    * Lectura de archivo externo.
    * Creación de diccionario.
    * Clasificación de personajes.
    * Modificación de nombres de magos.
    * Generación de reportes o listados.
* **Tecnologías:** Python, Tabulate, OS
* **Estructura del código:**
    * Uso de funciones con docstrings.
    * Nomenclatura clara y consistente.

### Detalles técnicos

* **Estructura de datos:** Diccionario para almacenar personajes.
* **Algoritmos:** Clasificación simple basada en valores de diccionario.
* **Librerías:**
    * **Tabulate:** Para formatear tablas de salida.
    * **OS:** Para interactuar con el sistema operativo (limpiar pantalla).

### Historial de versiones
* **1.0.0 (16/08/2024):** Versión inicial.
* **2.0.0 (18/08/2024):** Agrega menú.
* **2.0.1 (19/08/2024):** Corrige opciones del menú.
* **3.0.0 (20/08/2024):** Agrega ingesta de datos desde un archivo externo.

### Código

```python
# Aquí pegarías el código Python formateado con Markdown

### Diccionario de objetos

Elemento

Tipo

Descripción

**Variables**

v\_nomArchivo

str

Nombre del archivo de texto a leer.

dict\_personajes

dict

Diccionario que almacena los personajes y sus clasificaciones.

lst\_magos

list

Lista de nombres de los magos.

lst\_cientificos

list

Lista de nombres de los científicos.

lst\_otros

list

Lista de nombres de otros personajes.

lst\_grandiosos

list

Lista de nombres de magos con el prefijo "El gran".

v\_limpiarPantalla

bool

Flag para controlar si se limpia la pantalla.

v\_cont

str

Variable para almacenar la respuesta del usuario si desea continuar.

**Funciones**

f\_limpiarPantalla()

function

Limpia la pantalla de la consola.

f\_leerArchivo()

function

Lee un archivo de texto y crea un diccionario.

f\_clasificarPersonajes()

function

Clasifica los personajes en diferentes categorías.

f\_hacerGrandioso()

function

Agrega el prefijo "El gran" a los nombres de los magos.

f\_imprimirNombres()

function

Imprime los nombres de una lista.

f\_imprimirTodos()

function

Imprime todos los personajes con su clasificación.

f\_imprimirMagos()

function

Imprime solo los nombres de los magos.

f\_imprimirGrandiosos()

function

Imprime los nombres de los magos con el prefijo.

f\_imprimirFinal()

function

Imprime todos los personajes después de agregar el prefijo.

Exportar a Hojas de cálculo

**Explicación de las columnas:**

-   **Elemento:** Nombre de la variable o función.
-   **Tipo:** Tipo de dato (str, int, float, list, dict, function, etc.).
-   **Descripción:** Explicación concisa de qué hace o almacena el elemento.

**Consideraciones adicionales:**

-   **Completitud:** Asegúrate de incluir todas las variables y funciones relevantes.
-   **Claridad:** Usa un lenguaje claro y conciso para describir cada elemento.
-   **Consistencia:** Mantén una estructura y formato consistente en todo el diccionario.
-   **Actualización:** Mantén el diccionario actualizado a


