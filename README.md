# Practice_unittest_MetPruebas
 Practica de unittest en python
 
Elección de desarrollo: Back-end
Lenguaje: Python
Módulo de pruebas: Unittest
Entorno de desarrollo: Visual Studio Code
Módulo o lógica del negocio desarrollada: se desarrolló el módulo que conecta, lee y almacena
la información enviada por el usuario por medio de la aplicación y los registros recibidos en el
centro de gestión para su análisis, procesamiento y accionar frente a las emergencias reportadas,
dadas las condiciones de desarrollo se optó por interpretar las imágenes como direcciones URL,
por lo tanto, en la base de datos constan como un varchar
Elección del módulo de pruebas:
Se eligió la herramienta unittest dado que es el marco de trabajo estándar para realizar pruebas
unitarias en Python. Está incluido en la biblioteca estándar del lenguaje y está diseñada para
facilitar la creación y ejecución de pruebas de manera eficiente.
Proporciona las siguientes ventajas y características en la creación de pruebas unitarias:
1. Su estructura es modular: Permite la creación de conjuntos de pruebas organizados y
modulares mediante clases y métodos específicos para cada prueba.
2. Cuenta con assertions integradas: Ofrece una amplia gama de métodos de aserción
predefinidos para poder evaluar que los resultados de las pruebas sean los esperados. Por
ejemplo, “assertEqual”, “assertTrue”, “assertFalse”, etcétera.
3. Fixture para pruebas: Permite el uso de métodos de configuración y limpieza antes y
después de las pruebas, lo que garantiza un entorno de prueba consistente y controlado.
4. Es nativo de Python: Por lo que se puede descubrir automáticamente pruebas en un
conjunto de archivos o directorios y garantiza la compatibilidad entre el lenguaje y el
módulo, lo que simplifica la ejecución de todas las pruebas disponibles.
5. Integrable con otros marcos y herramientas: Aunque es el marco de pruebas unitarias
estándar en Python, puede integrarse con otros marcos de pruebas o herramientas de
ejecución de pruebas para adaptarse a necesidades más específicas.
En resumen, unittest es una elección sólida para realizar pruebas unitarias en Python debido a su
integración directa con el lenguaje, su estructura modular y sus capacidades para verificar y validar
el comportamiento de las funciones y clases en un entorno controlado.
Desarrollo del módulo de la aplicación según el requerimiento funcional:
Dada la amplitud del requerimiento presentado se optó por trabajar sobre el intercambio y
almacenaje de datos entre el usuario y la aplicación y entre esta y el centro de gestión que la
recibirá.