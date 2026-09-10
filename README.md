#  Proyecto Final M4: Pokédex Virtual Interactiva

##  Información del Estudiante
* **Nombre:** Javier Márquez Ureña
* **Materia:** Fundamentos de Python - Módulo 4
* **Institución:** Ucamp

---

##  Descripción del Proyecto
Esta aplicación es un consultor biónico avanzado que funciona como una **Pokédex Virtual** conectada en tiempo real con los servidores globales de la **PokeAPI**. 

El sistema cuenta con un menú interactivo en la terminal decorado con códigos de escape ANSI y está diseñado con un manejo robusto de excepciones para garantizar la inmunidad total a fallos.

##  Características Técnicas Desarrolladas
* **Consumo de API:** Peticiones HTTP GET estables mediante la librería `requests`.
* **Validación de Errores:** Control estricto de códigos HTTP (Error 404 para entidades no encontradas).
* **Persistencia de Datos:** Almacenamiento y actualización automática en un archivo físico local llamado `pokedex.json`.
* **Manejo de Excepciones:** Bloques `try-except` para capturar ingresos vacíos o datos no numéricos.

---

###  Instrucciones de Ejecución
Ejecuta el archivo directamente en la terminal nativa de tu sistema operativo utilizando el comando:
```bash
python pokedex.py
```
