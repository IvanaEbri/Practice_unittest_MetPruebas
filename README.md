# Práctica de UnitTest en Python - Métodología de pruebas
 
Esta práctica de **Unittest** en Python se enmarca en el contexto académico de la carrera de Tecnicatura en Desarrollo de Software. Forma parte del proceso de aprendizaje, donde se aborda la creación de pruebas unitarias utilizando el marco de trabajo estándar de pruebas unitarias. La implementación se centra en el desarrollo de un módulo de backend en Python, realizado como práctica propia para fortalecer los conocimientos adquiridos durante la formación académica.

## Contenido

1. [Contexto Académico](#contexto-académico)
2. [Elección de Desarrollo](#elección-de-desarrollo)
3. [Módulo o Lógica del Negocio Desarrollada](#módulo-o-lógica-del-negocio-desarrollada)
4. [Elección del Módulo de Pruebas](#elección-del-módulo-de-pruebas)
5. [Desarrollo del Módulo de la Aplicación](#desarrollo-del-módulo-de-la-aplicación-según-el-requerimiento-funcional)
6. [Conclusión](#conclusión)



## Contexto Académico

En el marco académico de la Tecnicatura en Desarrollo de Software, esta práctica de Unittest en Python surge como una oportunidad para aplicar los conocimientos teóricos adquiridos en las aulas. Integrada como parte del proceso formativo, esta experiencia ofrece un enfoque práctico que complementa los fundamentos teóricos de la carrera. La implementación del módulo de backend se convierte así en una valiosa contribución al aprendizaje, proporcionando una perspectiva realista de los desafíos y decisiones que los desarrolladores enfrentan en el mundo profesional del desarrollo de software.

## Elección de Desarrollo

### Lenguaje 
**Python**

### Área de Trabajo
**Back-end**

### Módulo de pruebas
**Unittest**

### Entorno de desarrollo
**Visual Studio Code**

## Módulo o lógica del negocio desarrollada

Se desarrolló el módulo que conecta, lee y almacena la información enviada por el usuario por medio de la aplicación y los registros recibidos en el centro de gestión para su análisis, procesamiento y accionar frente a las emergencias reportadas, dadas las condiciones de desarrollo se optó por interpretar las imágenes como direcciones URL, por lo tanto, en la base de datos constan como un varchar

## Elección del módulo de pruebas

Se eligió la herramienta unittest dado que es el marco de trabajo estándar para realizar pruebas unitarias en Python. Está incluido en la biblioteca estándar del lenguaje y está diseñada para facilitar la creación y ejecución de pruebas de manera eficiente. 
Proporciona las siguientes ventajas y características en la creación de pruebas unitarias:
1. **Su estructura es modular:** Permite la creación de conjuntos de pruebas organizados y modulares mediante clases y métodos específicos para cada prueba.
2. **Cuenta con assertions integradas:** Ofrece una amplia gama de métodos de aserción predefinidos para poder evaluar que los resultados de las pruebas sean los esperados. Por ejemplo, `assertEqual`, `assertTrue`, `assertFalse`, etcétera.
3. **Fixture para pruebas:** Permite el uso de métodos de configuración y limpieza antes y después de las pruebas, lo que garantiza un entorno de prueba consistente y controlado.
4. **Es nativo de Python:** Por lo que se puede descubrir automáticamente pruebas en un conjunto de archivos o directorios y garantiza la compatibilidad entre el lenguaje y el módulo, lo que simplifica la ejecución de todas las pruebas disponibles.
5. **Integrable con otros marcos y herramientas:** Aunque es el marco de pruebas unitarias estándar en Python, puede integrarse con otros marcos de pruebas o herramientas de ejecución de pruebas para adaptarse a necesidades más específicas.

En resumen, **unittest** es una elección sólida para realizar pruebas unitarias en Python debido a su integración directa con el lenguaje, su estructura modular y sus capacidades para verificar y validar el comportamiento de las funciones y clases en un entorno controlado.

## Desarrollo del módulo de la aplicación según el requerimiento funcional

Dada la amplitud del requerimiento presentado se optó por trabajar sobre el intercambio y almacenaje de datos entre el usuario y la aplicación y entre esta y el centro de gestión que la recibirá.

## Conclusión

En conclusión, la herramienta **Unittest** emerge como una pieza fundamental en el desarrollo de software al permitir la prueba de unidades aisladas de código para garantizar su correcto funcionamiento. Aunque la aplicación de Unittest puede parecer directa, la verdadera complejidad se encuentra en la planificación y creación de casos de prueba efectivos. Definir exhaustivamente estos casos implica anticipar una variedad de situaciones, desde las más simples hasta las más complejas. El proceso, aunque crucial, puede ser considerablemente más extenso que la escritura del propio código. Además, la implementación de la lógica de verificación de estos casos demanda un entendimiento detallado del código, lo que añade una capa adicional de complejidad y esfuerzo. En última instancia, la eficacia de Unittest radica en la minuciosidad y dedicación invertidas en la elaboración de pruebas exhaustivas y su implementación precisa en el proceso de desarrollo de software.